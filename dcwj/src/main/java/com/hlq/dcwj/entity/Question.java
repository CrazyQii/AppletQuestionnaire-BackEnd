package com.hlq.dcwj.entity;


import com.hlq.dcwj.config.JpaConvertStringJson;
import org.hibernate.annotations.TypeDef;

import javax.persistence.*;
import java.io.Serializable;

/**
 * @Program: Question
 * @Description: 调查问卷题目，题目通过Json格式进行存储
 * @Author: HanLinqi
 * @Date: 2021/09/09 10:35:14
 */

@Entity
@Table(name = "DCWJ_QUESTION")
@TypeDef(name = "JSON", typeClass = JpaConvertStringJson.class)
public class Question implements Serializable {

    @GeneratedValue
    @Id
    @Column(name = "ID", nullable = false, unique = true)
    private Long id;

    /** 题目类型 */
    @Column(name = "KIND", nullable = false)
    private String kind;

    /** 问题文本 */
    @Column(name = "TITLE", nullable = false)
    private String title;

    /** 显示选项-Json格式 */
    @Column(name = "OPTIONS", columnDefinition = "JSON")
    private String options;

    /** 正确答案-Json格式（可单选多选，可空）*/
    @Column(name = "ANSWER", columnDefinition = "JSON")
    private String answer;

    @ManyToOne(targetEntity = Questionnaire.class, cascade = {})
    //可选属性optional=false,表示questionnaire不能为空。删除選項，不影响問卷
    @JoinColumn(name = "QUESTIONNAIRE_ID")
    private Questionnaire questionnaire;

    public Long getId() {
        return id;
    }

    public void setId(Long id) {
        this.id = id;
    }

    public String getKind() {
        return kind;
    }

    public void setKind(String kind) {
        this.kind = kind;
    }

    public String getTitle() {
        return title;
    }

    public void setTitle(String title) {
        this.title = title;
    }

    public String getOptions() {
        return options;
    }

    public void setOptions(String options) {
        this.options = options;
    }

    public String getAnswer() {
        return answer;
    }

    public void setAnswer(String answer) {
        this.answer = answer;
    }

    public Questionnaire getQuestionnaire() {
        return questionnaire;
    }

    public void setQuestionnaire(Questionnaire questionnaire) {
        this.questionnaire = questionnaire;
    }

    @Override
    public String toString() {
        return "Question{" +
                "id=" + id +
                ", kind='" + kind + '\'' +
                ", title='" + title + '\'' +
                ", options='" + options + '\'' +
                ", answer='" + answer + '\'' +
                ", questionnaire=" + questionnaire +
                '}';
    }
}
