package com.hlq.dcwj.vo;

import com.hlq.dcwj.entity.Question;
import com.hlq.dcwj.entity.Questionnaire;

import java.io.Serializable;

/**
 * @Program: QuestionnaireVo
 * @Description: 问卷vo，实现多表联查
 * @Author: HanLinqi
 * @Date: 2021/09/13 00:28:24
 */
public class QuestionnaireVo implements Serializable {
    /** 问卷大类 */
    private Questionnaire questionnaire;
    /** 问卷题目 */
    private Question question;

    public QuestionnaireVo() {}

    public QuestionnaireVo(Questionnaire questionnaire) {
        Question question = new Question();
        this.questionnaire = questionnaire;
        this.question = question;
    }

    public QuestionnaireVo(Questionnaire questionnaire, Question question) {
        this.questionnaire = questionnaire;
        this.question = question;
    }

    public Questionnaire getQuestionnaire() {
        return questionnaire;
    }

    public void setQuestionnaire(Questionnaire questionnaire) {
        this.questionnaire = questionnaire;
    }

    public Question getQuestion() {
        return question;
    }

    public void setQuestion(Question question) {
        this.question = question;
    }
}
