from flask import Blueprint, request
from models.questionnaire import Questionnaire, Option, OptionSelect
from models.account import Record, Account
from models import db
from utils import resp
import datetime

from flask import Blueprint

questionnaire_bp = Blueprint('questionnaire', __name__, url_prefix='/ques')


@questionnaire_bp.route('/list', methods=['GET'])
def get_question():
    result = {'code': 200, 'msg': 'ok', 'data': {}}
    try:
        req = request.args
        if 'id' not in req:
            raise Exception('参数错误！')
        # 问卷类型
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
        result['msg'] = f'问卷错误:{e}'
    finally:
        return resp(result['code'], result['msg'], result['data'])


@questionnaire_bp.route('/record', methods=['POST'])
def get_record():
    result = {'code': 200, 'msg': 'ok', 'data': {}}
    try:
        req = request.get_json()
        if 'openid' not in req:
            raise Exception('参数错误！')

        answer1 = req['answer1']
        answer2 = req['answer2']
        answer3 = req['answer3']
        answer4 = req['answer4']
        score_1 = getScore(1, answer1)['score_1']
        score_2 = getScore(2, answer2)['score_2']
        score_3 = getScore(3, answer3)['score_3']
        score_4 = getScore(4, answer4)['score_4']

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
        result['msg'] = f'分数错误:{e}'
    finally:
        return resp(result['code'], result['msg'], result['data'])


@questionnaire_bp.route('/advise', methods=['GET'])
def get_advise():
    result = {'code': 200, 'msg': 'ok', 'data': []}
    try:
        req = request.args
        if 'openid' not in req:
            raise Exception('参数错误！')
        record = db.session.query(Record).filter(
            Record.openid == req['openid']).first()
        if record is None:
            raise Exception('答题数据记录获取失败!')
        record = record.to_json()
        result['data'] = {
            'ad1': advise(1, record['score_1']),
            'ad2': advise(2, record['score_2_1'], record['score_2_2'], record['score_2_3']),
            'ad3': advise(3, record['score_3']),
            'ad4': advise(4, record['score_4_1'], record['score_4_2'], record['score_4_3'], record['score_4_4'], record['score_4_5'])
        }
    except Exception as e:
        result['code'] = 500
        result['msg'] = f'分数错误:{e}'
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
    try:
        if questionnaire_id == 1:
            for i in answer:
                if i == 1:
                    score += 4
                elif i == 2:
                    score += 2
        elif questionnaire_id == 2:
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
            }
        }
    except Exception as e:
        print('获取分数总和错误!' + e)


def advise(questionnaire_id: int, *args):
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
    else:
        return '暂无对应建议'
