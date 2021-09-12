package com.hlq.dcwj.entity;

/**
 * @Program: AnswerJson
 * @Description: 正确答案
 * @Author: HanLinqi
 * @Date: 2021/09/12 23:27:04
 */
public class AnswerJson {
    /** 结果参数1 */
    private String answer1;
    /** 结果分数1 */
    private Integer answerScore1;
    /** 结果参数2 */
    private String answer2;
    /** 结果分数2 */
    private Integer answerScore2;
    /** 结果参数3 */
    private String answer3;
    /** 结果分数3 */
    private Integer answerScore3;
    /** 结果参数4 */
    private String answer4;
    /** 结果分数4 */
    private Integer answerScore4;

    public String getAnswer1() {
        return answer1;
    }

    public void setAnswer1(String answer1) {
        this.answer1 = answer1;
    }

    public Integer getAnswerScore1() {
        return answerScore1;
    }

    public void setAnswerScore1(Integer answerScore1) {
        this.answerScore1 = answerScore1;
    }

    public String getAnswer2() {
        return answer2;
    }

    public void setAnswer2(String answer2) {
        this.answer2 = answer2;
    }

    public Integer getAnswerScore2() {
        return answerScore2;
    }

    public void setAnswerScore2(Integer answerScore2) {
        this.answerScore2 = answerScore2;
    }

    public String getAnswer3() {
        return answer3;
    }

    public void setAnswer3(String answer3) {
        this.answer3 = answer3;
    }

    public Integer getAnswerScore3() {
        return answerScore3;
    }

    public void setAnswerScore3(Integer answerScore3) {
        this.answerScore3 = answerScore3;
    }

    public String getAnswer4() {
        return answer4;
    }

    public void setAnswer4(String answer4) {
        this.answer4 = answer4;
    }

    public Integer getAnswerScore4() {
        return answerScore4;
    }

    public void setAnswerScore4(Integer answerScore4) {
        this.answerScore4 = answerScore4;
    }

    @Override
    public String toString() {
        return "AnswerJson{" +
                "answer1='" + answer1 + '\'' +
                ", answerScore1=" + answerScore1 +
                ", answer2='" + answer2 + '\'' +
                ", answerScore2=" + answerScore2 +
                ", answer3='" + answer3 + '\'' +
                ", answerScore3=" + answerScore3 +
                ", answer4='" + answer4 + '\'' +
                ", answerScore4=" + answerScore4 +
                '}';
    }
}
