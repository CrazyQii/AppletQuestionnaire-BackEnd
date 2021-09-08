package com.hlq.dcwj.entity;

import org.springframework.format.annotation.DateTimeFormat;

import javax.persistence.*;
import java.io.Serializable;
import java.util.Date;

@Entity
@Table(name = "DCWJ_BASE_INFO")
public class BaseInfo implements Serializable {

    @GeneratedValue
    @Id
    @Column(name = "ID", nullable = false, unique = true)
    private Long id;

    /** 姓名 */
    @Column(name = "NAME", nullable = false)
    private String name;

    /** 性别 */
    @Column(name = "GENDER", nullable = false)
    private String gender;

    /** 出生年月 */
    @DateTimeFormat(pattern = "yyyy-MM-dd HH:mm:ss")
    @Column(name = "BIRTH", nullable = false)
    private Date birth;

    /** 教育程度 */
    @Column(name = "EDUCATION", nullable = false)
    private String education;

    /** 耳鸣发生的位置 */
    @Column(name = "TINNITUS_POSITION", nullable = false)
    private String tinnitusPosition;

    /** 耳鸣发生了时间 */
    @Column(name = "TINNITUS_TIME", nullable = false)
    private Integer tinnitusTime;

    /** 耳鸣一次持续时间 */
    @Column(name = "TINNITUS_DURING", nullable = false)
    private String tinnitusDuring;

    /** 耳鸣发生环境 */
    @Column(name = "TINNIUS_ENV", nullable = false)
    private String tinnitusEnv;

    /** 耳鸣音调 */
    @Column(name = "TINNIUS_TONE", nullable = false)
    private String tinnitusTone;

    /** 耳鸣响度 */
    @Column(name = "TINNIUS_FEEL", nullable = false)
    private String tinnitusFeel;

    /** openId 外键 */
    @OneToOne(cascade = CascadeType.ALL)  // 级联删除
    @JoinColumn(name = "ACCOUNT_ID")
    private Account account;

    public Long getId() {
        return id;
    }

    public void setId(Long id) {
        this.id = id;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public String getGender() {
        return gender;
    }

    public void setGender(String gender) {
        this.gender = gender;
    }

    public Date getBirth() {
        return birth;
    }

    public void setBirth(Date birth) {
        this.birth = birth;
    }

    public String getEducation() {
        return education;
    }

    public void setEducation(String education) {
        this.education = education;
    }

    public String getTinnitusPosition() {
        return tinnitusPosition;
    }

    public void setTinnitusPosition(String tinnitusPosition) {
        this.tinnitusPosition = tinnitusPosition;
    }

    public Integer getTinnitusTime() {
        return tinnitusTime;
    }

    public void setTinnitusTime(Integer tinnitusTime) {
        this.tinnitusTime = tinnitusTime;
    }

    public String getTinnitusDuring() {
        return tinnitusDuring;
    }

    public void setTinnitusDuring(String tinnitusDuring) {
        this.tinnitusDuring = tinnitusDuring;
    }

    public String getTinnitusEnv() {
        return tinnitusEnv;
    }

    public void setTinnitusEnv(String tinnitusEnv) {
        this.tinnitusEnv = tinnitusEnv;
    }

    public String getTinnitusTone() {
        return tinnitusTone;
    }

    public void setTinnitusTone(String tinnitusTone) {
        this.tinnitusTone = tinnitusTone;
    }

    public String getTinnitusFeel() {
        return tinnitusFeel;
    }

    public void setTinnitusFeel(String tinnitusFeel) {
        this.tinnitusFeel = tinnitusFeel;
    }

    public Account getAccount() {
        return account;
    }

    public void setAccount(Account account) {
        this.account = account;
    }

    @Override
    public String toString() {
        return "BaseInfo{" +
                "id=" + id +
                ", name='" + name + '\'' +
                ", gender='" + gender + '\'' +
                ", birth=" + birth +
                ", education='" + education + '\'' +
                ", tinnitusPosition='" + tinnitusPosition + '\'' +
                ", tinnitusTime=" + tinnitusTime +
                ", tinnitusDuring='" + tinnitusDuring + '\'' +
                ", tinnitusEnv='" + tinnitusEnv + '\'' +
                ", tinnitusTone='" + tinnitusTone + '\'' +
                ", tinnitusFeel='" + tinnitusFeel + '\'' +
                ", account=" + account +
                '}';
    }
}
