package com.hlq.dcwj.entity;

import org.springframework.format.annotation.DateTimeFormat;

import javax.persistence.*;
import java.io.Serializable;
import java.util.Date;

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

    /** 试卷分数 */
    @Column(name = "SCORE", nullable = false)
    private Integer score;

    /** 发布时间 */
    @DateTimeFormat(pattern = "yyyy-MM-dd HH:mm:ss")
    @Column(name = "PUBLISH_TIME", nullable = false)
    private Date publishTime;

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

    public Integer getScore() {
        return score;
    }

    public void setScore(Integer score) {
        this.score = score;
    }

    public Date getPublishTime() {
        return publishTime;
    }

    public void setPublishTime(Date publishTime) {
        this.publishTime = publishTime;
    }

    @Override
    public String toString() {
        return "Questionnaire{" +
                "id=" + id +
                ", title='" + title + '\'' +
                ", score=" + score +
                ", publishTime=" + publishTime +
                '}';
    }
}
