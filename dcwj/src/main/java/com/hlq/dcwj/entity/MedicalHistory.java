package com.hlq.dcwj.entity;

import javax.persistence.*;
import java.io.Serializable;

@Entity
@Table(name = "DCWJ_MEDICAL_HISTORY")
public class MedicalHistory implements Serializable {

    @GeneratedValue
    @Id
    @Column(name = "ID", nullable = false, unique = true)
    private Long id;

    /** 症状类型 */
    @Column(name = "SYMPTOM_TYPE", nullable = false)
    private String symptomType;

    /** 导致耳鸣原因 */
    @Column(name = "REASON", nullable = false)
    private String reason;

    /** 慢性疾病 */
    @Column(name = "CHRONIC_DISEASE", nullable = false)
    private String chronicDisease;

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

    public String getSymptomType() {
        return symptomType;
    }

    public void setSymptomType(String symptomType) {
        this.symptomType = symptomType;
    }

    public String getReason() {
        return reason;
    }

    public void setReason(String reason) {
        this.reason = reason;
    }

    public String getChronicDisease() {
        return chronicDisease;
    }

    public void setChronicDisease(String chronicDisease) {
        this.chronicDisease = chronicDisease;
    }

    public Account getAccount() {
        return account;
    }

    public void setAccount(Account account) {
        this.account = account;
    }

    @Override
    public String toString() {
        return "MedicalHistory{" +
                "id=" + id +
                ", symptomType='" + symptomType + '\'' +
                ", reason='" + reason + '\'' +
                ", chronicDisease='" + chronicDisease + '\'' +
                ", account=" + account +
                '}';
    }
}
