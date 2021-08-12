#coding:utf-8
# 认证（登录/注册）路由

import requests
from flask import Blueprint, request
from models.account import Account, BaseInfo, HistDisease  # 账户模型
from models import db
from utils import resp
import datetime

from flask import Blueprint

account_bp = Blueprint('account', __name__, url_prefix='/account')

@account_bp.route('/login', methods=['POST'])
def login():
    """ 用户登录session """
    result = {'code': 200, 'msg': 'ok', 'data': {}}
    try:
        req = request.get_json()
        if 'code' not in req:
            raise Exception('code 查询失败！')
        else:
            session_key, openid = getSession(req['code'])
            if session_key is None or openid is None:
                raise Exception('session_key and openid 错误！')
            result['data'] = {'session_key': session_key, 'openid': openid}
    except Exception as e:
        result['code'] = 500
        result['msg'] = f'登录错误:{e}'
    finally:
        return resp(result['code'], result['msg'], result['data'])


@account_bp.route('/userInfo', methods=['POST'])
def post_userInfo():
    """ 用户信息获取 """
    result = {'code': 200, 'msg': 'ok', 'data': {}}
    try:
        req = request.get_json()
        user = repeat_register(req['openid'])
        if user[0]:
            account = Account(session_key=req['session_key'],
                              openid=req['openid'],
                              nickname=req['nickName'],
                              avatar=req['avatarUrl'],
                              is_admin='no',
                              regist_time=datetime.datetime.now().strftime(
                                  '%Y-%m-%d %H:%M:%S'))
            db.session.add(account)
            db.session.commit()
            result['data'] = account.to_json()
        else:
            account = db.session.query(Account).filter(
                Account.openid == req['openid']).first()
            result['data'] = account.to_json()
    except Exception as e:
        result['code'] = 500
        result['msg'] = f'登录错误:{e}'
    finally:
        return resp(result['code'], result['msg'], result['data'])


@account_bp.route('/baseInfo', methods=['POST'])
def post_baseInfo():
    """ 提交用户本人的基本信息 """
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
        result['msg'] = f'上传信息错误:{e}'
    finally:
        return resp(result['code'], result['msg'], result['data'])


@account_bp.route('/histDisease', methods=['POST'])
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
    

############################################
# 辅助函数
############################################


def repeat_register(openid: str):
    """ 判断用户是否已经存在，存在False，不存在True """
    try:
        account = db.session.query(Account).filter(
            Account.openid == openid).first()
        if account is None:
            return True, ''
        raise Exception('账号已经登录过！')
    except Exception as e:
        return False, e


def getSession(code):
    """ 小程序登录凭证接口 """
    try:
        appid = 'wx43578d7ac93df10e'
        secret = '1773faa5d65780dbdcdb470bd9fd8efa'
        auth_url = f'https://api.weixin.qq.com/sns/jscode2session?appid={appid}&secret={secret}&js_code={code}&grant_type=authorization_code'
        req = requests.get(auth_url)
        if req.status_code == 200:
            return req.json()['session_key'], req.json()['openid']
        raise Exception('getSession 函数失败！')
    except Exception as e:
        print(e)
        return None, None
