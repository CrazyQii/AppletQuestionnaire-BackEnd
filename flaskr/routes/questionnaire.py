from flask import Blueprint, request
from models.questionnaire import Questionnaire, Option, OptionSelect, SleepQues
from models.account import Record, Account, HistDisease, BaseInfo
from models import db
from utils import resp
import datetime

from flask import Blueprint

questionnaire_bp = Blueprint('questionnaire', __name__, url_prefix='/ques')


@questionnaire_bp.route('/list', methods=['POST'])
def get_question():
    """ 根据问卷id生成对应的问卷 """
    result = {'code': 200, 'msg': 'ok', 'data': {}}
    try:
        req = request.get_json()
        print(req)
        if 'id' not in req:
            raise Exception('args error！')
        
        if str(req['id']) == '6':
            # 问卷6信息获取
            ques = db.session.query(Questionnaire).filter(
                Questionnaire.id == req['id']).first().to_json()
            ques['option'] = []
            opts = db.session.query(SleepQues).all()
            for opt in opts:
                opt = opt.to_json()
                ques['option'].append(opt)
        else:
            # 问卷1-5信息获取
            ques = db.session.query(Questionnaire).filter(
                Questionnaire.id == req['id']).first().to_json()
            opts = db.session.query(Option).filter(
                Option.questionnaire_id == ques['id']).all()
            ques['option'] = []
            # 问卷题目
            for opt in opts:
                opt = opt.to_json()
                opt_sel = db.session.query(OptionSelect).filter(
                    OptionSelect.questionnaire_id == ques['id']).all()
                opt['select'] = []
                # 选择答案
                for sel in opt_sel:
                    opt['select'].append(sel.to_json())
                ques['option'].append(opt)
        result['data'] = ques
    except Exception as e:
        result['code'] = 500
        result['msg'] = f'get questionnaire error:{e}'
    finally:
        return resp(result['code'], result['msg'], result['data'])


@questionnaire_bp.route('/record', methods=['POST'])
def post_record():
    """ 提交答题记录到数据库 """
    result = {'code': 200, 'msg': 'ok', 'data': {}}
    try:
        req = request.get_json()
        if 'openid' not in req:
            raise Exception('参数错误！')

        answer1 = req['answer1']
        answer2 = req['answer2']
        answer3 = req['answer3']
        answer4 = req['answer4']
        answer5 = req['answer5']
        answer6 = req['answer6']
        score_1 = getScore(1, answer1)['score_1']
        score_2 = getScore(2, answer2)['score_2']
        score_3 = getScore(3, answer3)['score_3']
        score_4 = getScore(4, answer4)['score_4']
        score_5 = getScore(5, answer5)['score_5']
        score_6 = getScoreSleep(answer6)

        finish_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        record = Record(score_1=score_1,
                        score_2_1=score_2['score_2_1'],
                        score_2_2=score_2['score_2_2'],
                        score_2_3=score_2['score_2_3'],
                        score_3=score_3,
                        score_4_1=score_4['score_4_1'],
                        score_4_2=score_4['score_4_2'],
                        score_4_3=score_4['score_4_3'],
                        score_4_4=score_4['score_4_4'],
                        score_4_5=score_4['score_4_5'],
                        score_5_1=score_5['score_5_1'],
                        score_5_2=score_5['score_5_2'],
                        score_5_3=score_5['score_5_3'],
                        score_6=score_6,
                        openid=req['openid'],
                        finish_time=finish_time)

        account = db.session.query(Account).filter(
            Account.openid == req['openid']).first()
        account.finish_time = finish_time
        
        db.session.add(record)
        db.session.commit()

        result['data'] = record.to_json()
    except Exception as e:
        result['code'] = 500
        result['msg'] = f'post record error:{e}'
    finally:
        return resp(result['code'], result['msg'], result['data'])


@questionnaire_bp.route('/advise', methods=['GET'])
def get_advise():
    """ 根据分数生成用户建议 """
    result = {'code': 200, 'msg': 'ok', 'data': []}
    try:
        req = request.args
        if 'openid' not in req:
            raise Exception('args error！')
        record = db.session.query(Record).filter(
            Record.openid == req['openid']).first()
        
        if record is None:
            raise Exception('get None data from database!')
        record = record.to_json()
        
        result['data'] = {
            'ad1': advise(1, record['score_1']),
            'ad2': advise(2, record['score_2_1'], record['score_2_2'], record['score_2_3']),
            'ad3': advise(3, record['score_3']),
            'ad4': advise(4, record['score_4_1'], record['score_4_2'], record['score_4_3'], record['score_4_4'], record['score_4_5']),
            'ad5': advise(5, record['score_5_1'], record['score_5_2'], record['score_5_3']),
            'ad6': advise(6, record['score_6'])
        }
    except Exception as e:
        result['code'] = 500
        result['msg'] = f'get advise error:{e}'
    finally:
        return resp(result['code'], result['msg'], result['data'])

@questionnaire_bp.route('/histDisease', methods=['GET'])
def get_histDisease():
    result = {'code': 200, 'msg': 'ok', 'data': []}
    try:
        req = request.args
        if 'openid' not in req:
            raise Exception('args error！')
        histDisease = db.session.query(HistDisease).filter(
            HistDisease.openid == req['openid']).first()
        baseInfo = db.session.query(BaseInfo).filter(
            BaseInfo.openid == req['openid']).first()
        
        
        if histDisease is None or baseInfo is None:
            raise Exception('get None data from database!')
        result['data'] = {
            'histDisease': histDisease.to_json(),
            'baseInfo': baseInfo.to_json()
        }
    except Exception as e:
        result['code'] = 500
        result['msg'] = f'get advise error:{e}'
    finally:
        return resp(result['code'], result['msg'], result['data'])

############################################
# 辅助函数
############################################


def getScore(questionnaire_id: int, answer: list):
    # 获取分数函数，较为复杂，且和数据库未对应
    score = 0
    score_2_1, score_2_2, score_2_3 = 0, 0, 0
    score_3 = 0
    score_4_1, score_4_2, score_4_3, score_4_4, score_4_5 = 0, 0, 0, 0, 0
    score_5_1, score_5_2, score_5_3 = 0, 0, 0
    try:
        if questionnaire_id == 1:
            # 问卷1
            for i in answer:
                if i == 1:
                    score += 4
                elif i == 2:
                    score += 2
        elif questionnaire_id == 2:
            # 问卷2
            for index, item in enumerate(answer):
                if index in [1, 6, 8, 11, 12, 14, 18]:
                    if item == 5:
                        score_2_1 += 1
                    elif item == 6:
                        score_2_1 += 2
                    elif item == 7:
                        score_2_1 += 3
                elif index in [2, 4, 7, 9, 15, 19, 20]:
                    if item == 5:
                        score_2_2 += 1
                    elif item == 6:
                        score_2_2 += 2
                    elif item == 7:
                        score_2_2 += 3
                elif index in [3, 5, 10, 13, 16, 17, 21]:
                    if item == 5:
                        score_2_3 += 1
                    elif item == 6:
                        score_2_3 += 2
                    elif item == 7:
                        score_2_3 += 3
            score_2_1 *= 2
            score_2_2 *= 2
            score_2_3 *= 2
        elif questionnaire_id == 3:
            # 问卷3
            for i in answer:
                if i == 9:
                    score_3 += 1
                elif i == 10:
                    score_3 += 2
                elif i == 11:
                    score_3 += 3
                elif i == 12:
                    score_3 += 4
        elif questionnaire_id == 4:
            # 问卷4
            for index, item in enumerate(answer):
                if index in [1, 6, 11, 16, 21, 26, 31, 36]:
                    if index == 36:
                        if item == 14:
                            score_4_1 += 5
                        elif item == 15:
                            score_4_1 += 4
                        elif item == 16:
                            score_4_1 += 3
                        elif item == 17:
                            score_4_1 += 2
                        elif item == 18:
                            score_4_1 += 1
                    else:
                        if item == 14:
                            score_4_1 += 1
                        elif item == 15:
                            score_4_1 += 2
                        elif item == 16:
                            score_4_1 += 3
                        elif item == 17:
                            score_4_1 += 4
                        elif item == 18:
                            score_4_1 += 5
                elif index in [2, 7, 12, 17, 22, 27, 32, 37]:
                    if index == 34:
                        if item == 14:
                            score_4_2 += 5
                        elif item == 15:
                            score_4_2 += 4
                        elif item == 16:
                            score_4_2 += 3
                        elif item == 17:
                            score_4_2 += 2
                        elif item == 18:
                            score_4_2 += 1
                    else:
                        if item == 14:
                            score_4_2 += 1
                        elif item == 15:
                            score_4_2 += 2
                        elif item == 16:
                            score_4_2 += 3
                        elif item == 17:
                            score_4_2 += 4
                        elif item == 18:
                            score_4_2 += 5
                elif index in [3, 8, 13, 18, 23, 28, 33, 38]:
                    if index in [8, 13, 18]:
                        if item == 14:
                            score_4_3 += 5
                        elif item == 15:
                            score_4_3 += 4
                        elif item == 16:
                            score_4_3 += 3
                        elif item == 17:
                            score_4_3 += 2
                        elif item == 18:
                            score_4_3 += 1
                    else:
                        if item == 14:
                            score_4_3 += 1
                        elif item == 15:
                            score_4_3 += 2
                        elif item == 16:
                            score_4_3 += 3
                        elif item == 17:
                            score_4_3 += 4
                        elif item == 18:
                            score_4_3 += 5
                elif index in [4, 9, 14, 19, 24, 29, 34, 39]:
                    if item == 14:
                        score_4_4 += 1
                    elif item == 15:
                        score_4_4 += 2
                    elif item == 16:
                        score_4_4 += 3
                    elif item == 17:
                        score_4_4 += 4
                    elif item == 18:
                        score_4_4 += 4
                elif index in [5, 10, 15, 20, 25, 30, 35, 40]:
                    if index in [5, 15]:
                        if item == 14:
                            score_4_5 += 5
                        elif item == 15:
                            score_4_5 += 4
                        elif item == 16:
                            score_4_5 += 3
                        elif item == 17:
                            score_4_5 += 2
                        elif item == 18:
                            score_4_5 += 1
                    else:
                        if item == 14:
                            score_4_5 += 1
                        elif item == 15:
                            score_4_5 += 2
                        elif item == 16:
                            score_4_5 += 3
                        elif item == 17:
                            score_4_5 += 4
                        elif item == 18:
                            score_4_5 += 4
        elif questionnaire_id == 5:
            # 问卷5
            for index, item in enumerate(answer):
                if index in [3, 5, 6, 7, 9, 10]:
                    if item == 19:
                        score_5_1 += 1
                    elif item == 20:
                        score_5_1 += 2
                    elif item == 21:
                        score_5_1 += 3
                    elif item == 22:
                        score_5_1 += 4
                    elif item == 23:
                        score_5_1 += 5
                elif index in [4, 11, 12]:
                    if item == 19:
                        score_5_2 += 1
                    elif item == 20:
                        score_5_2 += 2
                    elif item == 21:
                        score_5_2 += 3
                    elif item == 22:
                        score_5_2 += 4
                    elif item == 23:
                        score_5_2 += 5
                elif index in [1, 2, 8]:
                    if item == 19:
                        score_5_3 += 1
                    elif item == 20:
                        score_5_3 += 2
                    elif item == 21:
                        score_5_3 += 3
                    elif item == 22:
                        score_5_3 += 4
                    elif item == 23:
                        score_5_3 += 5
        return {
            'score_1': score,
            'score_2': {
                'score_2_1': score_2_1,
                'score_2_2': score_2_2,
                'score_2_3': score_2_3
            },
            'score_3': score_3,
            'score_4': {
                'score_4_1': score_4_1,
                'score_4_2': score_4_2,
                'score_4_3': score_4_3,
                'score_4_4': score_4_4,
                'score_4_5': score_4_5
            },
            'score_5': {
                'score_5_1': score_5_1,
                'score_5_2': score_5_2,
                'score_5_3': score_5_3
            }
        }
    except Exception as e:
        print('获取分数总和错误!' + e)

def getScoreSleep(answer: list):
    # 问卷6分数反馈
    a, b, c, d, e, f, g = 0, 0, 0, 0, 0, 0, 0
    # A睡眠质量
    a = getA(answer[14])
    # B
    b = getB(answer[1], answer[4])
    # C
    c = getC(answer[3])
    # D
    d = getD(answer[0], answer[2], answer[3])
    # E
    e = getE(answer[5: 14])
    # F
    f = getF(answer[15])
    # G
    g = getG(answer[16], answer[17])
    
    PSQI = a + b + c + d + e + f + g
    return PSQI

def getA(param0: str):
    if param0 == '0':
        return 0
    elif param0 == '1':
        return 1
    elif param0 == '2':
        return 2
    elif param0 == '3':
        return 3
    else:
        return 0

def getB(param1: str, param4: str):
    param1 = int(param1)
    score = 0
    if param1 <= 15:
        score += 0
    elif param1 >= 16 and param1 <= 30:
        score += 1
    elif param1 >= 31 and param1 < 60:
        score += 2
    elif param1 >= 60:
        score += 3
        
    if param4 == '0':
        score += 0
    elif param4 == '1':
        score += 1
    elif param4 == '2':
        score += 2
    elif param4 == '3':
        score += 3
        
    if score == 0:
        return 0
    elif score == 1 or score == 2:
        return 1
    elif score == 3 or score == 4:
        return 2
    elif score == 5 or score == 6:
        return 3
    
def getC(param3: str):
    param3 = float(param3)
    if param3 > 7:
        return 0
    elif param3 <= 7 or param3 > 6:
        return 1
    elif param3 <= 6 or param3 > 5:
        return 2
    elif param3 <= 5:
        return 3 
    
def getD(param0: str, param2: str, param3: str):
    start_h, start_m = int(param0.split(':')[0]), int(param0.split(':')[1])
    end_h, end_m = int(param2.split(':')[0]), int(param2.split(':')[1])
    
    during_h = end_h - start_h
    if during_h < 0:
        during_h += 24
    during_m = end_m - start_m
    if during_m < 0:
        during_m += 60
        during_h -= 1
    
    percent = float(param3) / (during_h + during_m / 60)
    
    if percent >= 0.85:
        return 0
    elif percent >= 0.75 and percent < 0.85:
        return 1
    elif percent >= 0.65 and percent < 0.75:
        return 2
    elif percent < 0.65: 
        return 3
    else:
        return 0
    
def getE(params: list):
    score = 0
    for param in params:
        if param == '0':
            score += 0
        elif param == '1':
            score += 1
        elif param == '2':
            score += 2
        elif param == '3':
            score += 3
    if score == 0:
        return 0
    elif score >= 1 and score <= 9:
        return 1
    elif score >= 10 and score <= 18:
        return 2
    elif score >= 19 and score <= 27:
        return 3
    else:
        return 0    
    
def getF(param15: str):
    if param15 == '0':
        return 0
    elif param15 == '1':
        return 1
    elif param15 == '2':
        return 2
    elif param15 == '3':
        return 3
        
def getG(param16: str, param17: str):
    score = 0
    if param16 == '0':
        score += 0
    elif param16 == '1':
        score += 1
    elif param16 == '2':
        score += 2
    elif param16 == '3':
        score += 3
        
    if param17 == '0':
        score += 0
    elif param17 == '1':
        score += 1
    elif param17 == '2':
        score += 2
    elif param17 == '3':
        score += 3
    
    if score == 0:
        return 0
    elif score == 1 or score == 2:
        return 1
    elif score == 3 or score == 4:
        return 2
    elif score == 5 or score == 6:
        return 3
    
def advise(questionnaire_id: int, *args):
    # 生成表1-5的建议
    if questionnaire_id == 1:
        score = args[0]
        if score >= 0 and score <= 16:
            return '您的耳鸣等级为轻微，只有在安静环境下可以听到耳鸣声'
        elif score >= 18 and score <= 36:
            return '您的耳鸣等级为轻度，耳鸣易被周围环境声音掩盖，容易因为其他事情忘记耳鸣'
        elif score >= 38 and score <= 56:
            return '您的耳鸣等级为中度，耳鸣在有背景声时也能觉察，但仍然可以进行日常生活和工作'
        elif score >= 58 and score <= 76:
            return '您的耳鸣等级为重度，您总是可以听到耳鸣声，影响睡眠及日常生活与工作'
        elif score >= 78 and score <= 100:
            return '您的耳鸣等级为灾难，经常听到耳鸣声，干扰睡眠，对日常各种活动造成灾难'
        else:
            return '暂无对应的结果'
    elif questionnaire_id == 2:
        tmp_str_1, tmp_str_2, tmp_str_3 = '', '', ''
        score_2_1 = args[0]
        score_2_2 = args[1]
        score_2_3 = args[2]

        if score_2_1 <= 14:
            tmp_str_1 = '压力量表中您的得分为正常'
        elif score_2_1 >= 15 and score_2_1 <= 18:
            tmp_str_1 = '压力量表显示您具有轻度压力'
        elif score_2_1 >= 19 and score_2_1 <= 25:
            tmp_str_1 = '压力量表显示您具有中度压力'
        elif score_2_1 >= 26 and score_2_1 <= 33:
            tmp_str_1 = '压力量表显示您具有重度压力'
        elif score_2_1 >= 34:
            tmp_str_1 = '压力量表显示您具有非常大的压力'
        else:
            tmp_str_1 = '暂无对应结果'

        if score_2_2 <= 7:
            tmp_str_2 = '焦虑量表中您的得分为正常'
        elif score_2_2 >= 8 and score_2_2 <= 9:
            tmp_str_2 = '焦虑量表显示您具有轻度焦虑'
        elif score_2_2 >= 10 and score_2_2 <= 14:
            tmp_str_2 = '焦虑量表显示您具有中度焦虑'
        elif score_2_2 >= 15 and score_2_2 <= 19:
            tmp_str_2 = '焦虑量表显示您具有重度焦虑'
        elif score_2_2 >= 20:
            tmp_str_2 = '焦虑量表显示您具有非常大的焦虑'
        else:
            tmp_str_2 = '暂无对应结果'

        if score_2_3 <= 9:
            tmp_str_3 = '抑郁量表中您的得分为正常'
        elif score_2_3 >= 10 and score_2_3 <= 13:
            tmp_str_3 = '抑郁量表显示您具有轻度抑郁'
        elif score_2_3 >= 14 and score_2_3 <= 20:
            tmp_str_3 = '抑郁量表显示您具有中度抑郁'
        elif score_2_3 >= 21 and score_2_3 <= 27:
            tmp_str_3 = '抑郁量表显示您具有重度抑郁'
        elif score_2_3 >= 28:
            tmp_str_3 = '抑郁量表显示您具有非常大的抑郁'
        else:
            tmp_str_3 = '暂无对应结果'

        return tmp_str_1 + '/' + tmp_str_2 + '/' + tmp_str_3
    elif questionnaire_id == 3:
        score = args[0]
        return f'您当前的焦虑敏感性得分为{score}分'
    elif questionnaire_id == 4:
        score_4_1 = args[0]
        score_4_2 = args[1]
        score_4_3 = args[2]
        score_4_4 = args[3]
        score_4_5 = args[4]
        return f'您在神经质方面得分{score_4_1}分。得分越高，表示情绪越稳定；/ 您在严谨性方面得分{score_4_2}分。得分越高，责任心越强。/ 您在宜人性方面得分{score_4_3}分。得分越高，性格越随和。/ 您在开放性方面得分{score_4_4}分。得分越高，性格越开朗，态度开放，容易接受新事物。/ 您在外向性方面得分{score_4_5}分。得分越高，性格越外向。'
    elif questionnaire_id == 5:
        score_5_1 = args[0]
        print(score_5_1)
        score_5_2 = args[1]
        score_5_3 = args[2]
        return f'您在预期性行为方面得分为{score_5_1}分 / 您在抑制性行为方面得分为{score_5_2}分 / 您在预期性情绪方面得分为{score_5_3}分'
    elif questionnaire_id == 6:
        score = args[0]
        return f'您的睡眠质量评分为 { score } 分'
    else:
        return '暂无对应建议'
    