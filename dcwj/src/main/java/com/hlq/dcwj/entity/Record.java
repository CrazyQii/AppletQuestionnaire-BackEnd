package com.hlq.dcwj.entity;

import com.hlq.dcwj.config.JpaConvertStringJson;
import org.hibernate.annotations.TypeDef;
import org.springframework.format.annotation.DateTimeFormat;

import javax.persistence.*;
import java.io.Serializable;
import java.util.Date;


/**
 * @Program: Record
 * @Description: 用户完成问卷情况记录，复杂数据通过Json格式进行存储，外键关联Account
 * @Author: HanLinqi
 * @Date: 2021/09/09 10:35:14
 */

@Entity
@Table(name = "DCWJ_RECORD")
@TypeDef(name = "JSON", typeClass = JpaConvertStringJson.class)
public class Record implements Serializable {

    @GeneratedValue
    @Id
    @Column(name = "ID", nullable = false, unique = true)
    private Long id;

    /** 个人基本信息-Json格式 */
    @Column(name = "BASEINFO", columnDefinition = "JSON")
    private String baseInfo;

    /** 病史-Json格式 */
    @Column(name = "MEDICAL_HISTORY", columnDefinition = "JSON")
    private String MedicalHistory;

    /** 问卷得分-Json格式 */
    @Column(name = "RESULT", columnDefinition = "JSON")
    private String result;

    /** 完成时间 */
    @DateTimeFormat(pattern = "yyyy-MM-dd HH:mm:ss")
    @Column(name = "FINISH_TIME")
    private Date finishTime;

    /** 外键关联 */
    @OneToOne(cascade = CascadeType.ALL)  // 级联删除
    @JoinColumn(name = "ACCOUNT_ID")
    private Account account;

    public Long getId() {
        return id;
    }

    public void setId(Long id) {
        this.id = id;
    }

    public String getBaseInfo() {
        return baseInfo;
    }

    public void setBaseInfo(String baseInfo) {
        this.baseInfo = baseInfo;
    }

    public String getMedicalHistory() {
        return MedicalHistory;
    }

    public void setMedicalHistory(String medicalHistory) {
        MedicalHistory = medicalHistory;
    }

    public String getResult() {
        return result;
    }

    public void setResult(String result) {
        this.result = result;
    }

    public Date getFinishTime() {
        return finishTime;
    }

    public void setFinishTime(Date finishTime) {
        this.finishTime = finishTime;
    }

    public Account getAccount() {
        return account;
    }

    public void setAccount(Account account) {
        this.account = account;
    }

    @Override
    public String toString() {
        return "Record{" +
                "id=" + id +
                ", baseInfo='" + baseInfo + '\'' +
                ", MedicalHistory='" + MedicalHistory + '\'' +
                ", result='" + result + '\'' +
                ", finishTime=" + finishTime +
                ", account=" + account +
                '}';
    }
}
