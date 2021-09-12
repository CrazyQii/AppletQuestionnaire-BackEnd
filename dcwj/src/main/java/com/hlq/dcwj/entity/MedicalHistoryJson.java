package com.hlq.dcwj.entity;

/**
 * @Program: MedicalHistoryJson
 * @Description: 个人病史
 * @Author: HanLinqi
 * @Date: 2021/09/12 23:22:34
 */
public class MedicalHistoryJson {
    /** 家人是否有症状 */
    private String familySymptoms;
    /** 导致耳鸣原因 */
    private String tinnitusReason;
    /** 慢性疾病 */
    private String chronicDisease;

    public String getFamilySymptoms() {
        return familySymptoms;
    }

    public void setFamilySymptoms(String familySymptoms) {
        this.familySymptoms = familySymptoms;
    }

    public String getTinnitusReason() {
        return tinnitusReason;
    }

    public void setTinnitusReason(String tinnitusReason) {
        this.tinnitusReason = tinnitusReason;
    }

    public String getChronicDisease() {
        return chronicDisease;
    }

    public void setChronicDisease(String chronicDisease) {
        this.chronicDisease = chronicDisease;
    }

    @Override
    public String toString() {
        return "MedicalHistoryJson{" +
                "familySymptoms='" + familySymptoms + '\'' +
                ", tinnitusReason='" + tinnitusReason + '\'' +
                ", chronicDisease='" + chronicDisease + '\'' +
                '}';
    }
}
