#coding:utf-8
# 账户模型

from . import db

class Account(db.Model):
    __tablename__ = 'tb_account'
    nickname = db.Column(db.String(255), doc="昵称", nullable=True)
    openid = db.Column(db.String(255), doc="openid",  primary_key=True)
    session_key = db.Column(db.String(255), doc="session_key", nullable=True)
    is_admin = db.Column(db.String(255), doc="账户角色", nullable=True)
    avatar = db.Column(db.String(255), doc="头像", nullable=True)
    finish_time = db.Column(db.String(255), doc="完成答卷时间")
    regist_time = db.Column(db.String(255), doc="注册时间", nullable=True)
    
    def to_json(self):
        return {
            'nickname': self.nickname,
            'openid': self.openid,
            'session_key': self.session_key,
            'is_admin': self.is_admin,
            'avatar': self.avatar,
            'finish_time': self.finish_time,
            'regist_time': self.regist_time
        }
        
class BaseInfo(db.Model):
    __tablename__ = 'tb_baseInfo'
    openid = db.Column(db.String(255), doc='openid', primary_key=True)
    name = db.Column(db.String(255), doc='', nullable=True)
    date = db.Column(db.String(255), doc='', nullable=True)
    culture = db.Column(db.String(255), doc='', nullable=True)
    erMing = db.Column(db.String(255), doc='', nullable=True)
    during = db.Column(db.String(255), doc='', nullable=True)
    keeping = db.Column(db.String(255), doc='', nullable=True)
    env = db.Column(db.String(255), doc='', nullable=True)
    voice = db.Column(db.String(255), doc='', nullable=True)
    feel = db.Column(db.String(255), doc='', nullable=True)
    
    def to_json(self):
        return {
            'openid': self.openid,
            'name': self.name,
            'date': self.date,
            'culture': self.culture,
            'erMing': self.erMing,
            'during': self.during,
            'keeping': self.keeping,
            'env': self.env,
            'voice': self.voice,
            'feel': self.feel
        }
        
class Record(db.Model):
    __tablename__ = 'tb_record'
    openid = db.Column(db.String(255), doc="账户id", primary_key=True)
    finish_time = db.Column(db.String(255), doc="完成答卷时间")
    score_1 = db.Column(db.String(255), doc="")
    score_2_1 = db.Column(db.String(255), doc="")
    score_2_2 = db.Column(db.String(255), doc="")
    score_2_3 = db.Column(db.String(255), doc="")
    score_3 = db.Column(db.String(255), doc="")
    score_4_1 = db.Column(db.String(255), doc="")
    score_4_2 = db.Column(db.String(255), doc="")
    score_4_3 = db.Column(db.String(255), doc="")
    score_4_4 = db.Column(db.String(255), doc="")
    score_4_5 = db.Column(db.String(255), doc="")
    
    def to_json(self):
        return {
            'openid': self.openid,
            'finish_time': self.finish_time,
            'score_1': self.score_1,
            'score_2_1': self.score_2_1,
            'score_2_2': self.score_2_2,
            'score_2_3': self.score_2_3,
            'score_3': self.score_3,
            'score_4_1': self.score_4_1,
            'score_4_2': self.score_4_2,
            'score_4_3': self.score_4_3,
            'score_4_4': self.score_4_4,
            'score_4_5': self.score_4_5
        }
    