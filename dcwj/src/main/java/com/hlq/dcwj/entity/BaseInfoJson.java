package com.hlq.dcwj.entity;

import java.util.Date;

/**
 * @Program: BaseInfoJson
 * @Description: 个人基本信息
 * @Author: HanLinqi
 * @Date: 2021/09/12 23:21:58
 */
public class BaseInfoJson {
    /** 姓名 */
    private String name;
    /** 性别 */
    private String gender;
    /** 出生日期 */
    private Date birth;
    /** 文化程度 */
    private String education;
    /** 耳鸣发生位置 */
    private String tinnitusPosition;
    /** 耳鸣发生几天、几年 */
    private String tinnitusTime;
    /** 耳鸣一次响多久 */
    private String tinnitusDuring;
    /** 耳鸣感知环境 */
    private String tinnitusEnv;
    /** 耳鸣音调 */
    private String tinnitusTune;
    /** 耳鸣响度 */
    private String tinnitusLoudness;

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

    public String getTinnitusTime() {
        return tinnitusTime;
    }

    public void setTinnitusTime(String tinnitusTime) {
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

    public String getTinnitusTune() {
        return tinnitusTune;
    }

    public void setTinnitusTune(String tinnitusTune) {
        this.tinnitusTune = tinnitusTune;
    }

    public String getTinnitusLoudness() {
        return tinnitusLoudness;
    }

    public void setTinnitusLoudness(String tinnitusLoudness) {
        this.tinnitusLoudness = tinnitusLoudness;
    }

    @Override
    public String toString() {
        return "BaseInfoJson{" +
                "name='" + name + '\'' +
                ", gender='" + gender + '\'' +
                ", birth=" + birth +
                ", education='" + education + '\'' +
                ", tinnitusPosition='" + tinnitusPosition + '\'' +
                ", tinnitusTime='" + tinnitusTime + '\'' +
                ", tinnitusDuring='" + tinnitusDuring + '\'' +
                ", tinnitusEnv='" + tinnitusEnv + '\'' +
                ", tinnitusTune='" + tinnitusTune + '\'' +
                ", tinnitusLoudness='" + tinnitusLoudness + '\'' +
                '}';
    }
}
