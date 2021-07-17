#coding:utf-8
# 问卷模型

from . import db

class Questionnaire(db.Model):
    __tablename__ = 'tb_questionnaire'
    id = db.Column(db.String(255), doc="id", nullable=True)
    title = db.Column(db.String(255), doc="标题",  primary_key=True)
    score = db.Column(db.String(255), doc="总分", nullable=True)
    publish_time = db.Column(db.String(255), doc="完成答卷时间")
    
    def to_json(self):
        return {
            'id': self.id,
            'title': self.title,
            'score': self.score,
            'publish_time': self.publish_time
        }
        
class Option(db.Model):
    __tablename__ = 'tb_option'
    id = db.Column(db.String(255), doc="id", nullable=True)
    content = db.Column(db.String(255), doc="标题",  primary_key=True)
    questionnaire_id = db.Column(db.String(255), doc="问卷id")
    
    def to_json(self):
        return {
            'id': self.id,
            'content': self.content,
            'questionnaire_id': self.questionnaire_id
        }
        
class OptionSelect(db.Model):
    __tablename__ = 'tb_option_select'
    id = db.Column(db.String(255), doc="id", nullable=True)
    content = db.Column(db.String(255), doc="标题",  primary_key=True)
    questionnaire_id = db.Column(db.String(255), doc="问卷id")
    score = db.Column(db.String(255), doc="总分", nullable=True)
    
    
    def to_json(self):
        return {
            'id': self.id,
            'content': self.content,
            'questionnaire_id': self.questionnaire_id,
            'score': self.score
        }