package com.hlq.dcwj.entity;

import org.springframework.format.annotation.DateTimeFormat;

import javax.persistence.*;
import java.io.Serializable;
import java.util.Date;
import java.util.List;

/**
 * @Program: Questionnaire
 * @Description: 调查问卷大的类目
 * @Author: HanLinqi
 * @Date: 2021/09/09 10:35:14
 */

@Entity
@Table(name = "DCWJ_QUESIONNAIRE")
public class Questionnaire implements Serializable {

    @GeneratedValue
    @Id
    @Column(name = "ID", nullable = false, unique = true)
    private Long id;

    /** 标题 */
    @Column(name = "TITILE", nullable = false)
    private String title;

    /** 发布时间 */
    @DateTimeFormat(pattern = "yyyy-MM-dd HH:mm:ss")
    @Column(name = "PUBLISH_TIME", nullable = false)
    private Date publishTime;

    /** 問卷題目 */
    @OneToMany(mappedBy = "questionnaire", cascade = CascadeType.ALL , fetch=FetchType.LAZY)
    //级联保存、更新、删除、刷新;延迟加载。当删除用户，会级联删除该問卷的所有選項
    //拥有mappedBy注解的实体类为关系被维护端
    private List<Question> questions;

    public Long getId() {
        return id;
    }

    public void setId(Long id) {
        this.id = id;
    }

    public String getTitle() {
        return title;
    }

    public void setTitle(String title) {
        this.title = title;
    }

    public Date getPublishTime() {
        return publishTime;
    }

    public void setPublishTime(Date publishTime) {
        this.publishTime = publishTime;
    }

    public List<Question> getQuestions() {
        return questions;
    }

    public void setQuestions(List<Question> questions) {
        this.questions = questions;
    }

    @Override
    public String toString() {
        return "Questionnaire{" +
                "id=" + id +
                ", title='" + title + '\'' +
                ", publishTime=" + publishTime +
                '}';
    }
}
