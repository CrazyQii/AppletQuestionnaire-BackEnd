#coding:utf-8
# 用户个人情况

from flask import Blueprint, request
from models.userInfo import BaseInfo, HistDisease 
from models import db
from utils import resp

from flask import Blueprint

userInfo_bp = Blueprint('userInfo', __name__, url_prefix='/userInfo')

@userInfo_bp.route('/baseInfo', methods=['GET'])
def get_baseInfo():
    """ 用户本人的基本信息 """
    result = {'code': 200, 'msg': 'ok', 'data': {}}
    try:
        req = request.args
        if 'openid' not in req:
            raise Exception('args error！')
        baseInfo = db.session.query(BaseInfo).filter(
            BaseInfo.openid == req['openid']).first()
        
        if baseInfo is None:
            raise Exception('get None data from database!')
        result['data'] = baseInfo.to_json()
    except Exception as e:
        result['code'] = 500
        result['msg'] = f'Get BaseInfo Error :{e}'
    finally:
        return resp(result['code'], result['msg'], result['data'])

@userInfo_bp.route('/baseInfo', methods=['POST'])
def post_baseInfo():
    result = {'code': 200, 'msg': 'ok', 'data': {}}
    try:
        req = request.get_json()
        baseInfo = BaseInfo(openid=req['openid'],
                            name=req['name'],
                            date=req['date'],
                            culture=req['culture'],
                            erMing=req['erMing'],
                            during=req['during'],
                            keeping=req['keeping'],
                            env=req['env'],
                            voice=req['voice'],
                            feel=req['feel'])
        db.session.add(baseInfo)
        db.session.commit()
        result['data'] = baseInfo.to_json()
    except Exception as e:
        result['code'] = 500
        result['msg'] = f'Post BaseInfo Error:{e}'
    finally:
        return resp(result['code'], result['msg'], result['data'])
    
@userInfo_bp.route('/histDisease', methods=['GET'])
def get_histDisease():
    result = {'code': 200, 'msg': 'ok', 'data': []}
    try:
        req = request.args
        if 'openid' not in req:
            raise Exception('args error！')
        histDisease = db.session.query(HistDisease).filter(
            HistDisease.openid == req['openid']).first()
        
        if histDisease is None :
            raise Exception('get None data from database!')
        result['data'] = histDisease.to_json()
    except Exception as e:
        result['code'] = 500
        result['msg'] = f'get histDisease error:{e}'
    finally:
        return resp(result['code'], result['msg'], result['data'])

@userInfo_bp.route('/histDisease', methods=['POST'])
def post_histDisease():
    """ 提交用户历史症状基本信息 """
    result = {'code': 200, 'msg': 'ok', 'data': {}}
    try:
        req = request.get_json()
        if 'openid' not in req and 'symptom' not in req and 'reason' not in req and 'self_disease' not in req:
            raise Exception('参数错误！')
        histDisease = HistDisease(openid=req['openid'],
                              symptom=req['symptom'],
                              reason=req['reason'],
                              self_disease=req['self_disease'])
        db.session.add(histDisease)
        db.session.commit()
        result['data'] = histDisease.to_json()
    except Exception as e:
        result['code'] = 500
        result['msg'] = f'提交历史信息错误:{e}'
    finally:
        return resp(result['code'], result['msg'], result['data'])