#coding:utf-8
# 问卷模型

from . import db

class Questionnaire(db.Model):
    # 问卷类型
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
    # 问卷题目
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
    # 不同问卷的题目分数
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
        
class SleepQues(db.Model):
    # 表6的调查问卷
    __tablename__ = 'tb_ques_sleep'
    id = db.Column(db.String(255), doc="id", nullable=True)
    content = db.Column(db.String(255), doc="标题",  primary_key=True)
    questionnaire_id = db.Column(db.String(255), doc="问卷id")
    q1 = db.Column(db.String(255), doc="问题1", nullable=True)
    q2 = db.Column(db.String(255), doc="问题2", nullable=True)
    q3 = db.Column(db.String(255), doc="问题3", nullable=True)
    q4 = db.Column(db.String(255), doc="问题4", nullable=True)
    q5 = db.Column(db.String(255), doc="问题5", nullable=True)
    
    def to_json(self):
        return {
            'id': self.id,
            'content': self.content,
            'questionnaire_id': self.questionnaire_id,
            'q1': self.q1,
            'q2': self.q2,
            'q3': self.q3,
            'q4': self.q4,
            'q5': self.q5
        }