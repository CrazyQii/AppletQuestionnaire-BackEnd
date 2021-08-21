#coding:utf-8
# 用户个人信息

from . import db

class BaseInfo(db.Model):
    # 个人基础信息
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
        
class HistDisease(db.Model):
    # 病史
    __tablename__ = 'tb_hist_disease'
    openid = db.Column(db.String(255), doc="账户id", primary_key=True)
    symptom = db.Column(db.String(255), doc="家人症状")
    reason = db.Column(db.String(255), doc="导致原因")
    self_disease = db.Column(db.String(255), doc="自身慢性疾病")
    
    def to_json(self):
        return {
            'openid': self.openid,
            'symptom': self.symptom,
            'reason': self.reason,
            'self_disease': self.self_disease
        }