package com.hlq.dcwj.entity;

/**
 * @Program: OptionsJson
 * @Description: 显示选项
 * @Author: HanLinqi
 * @Date: 2021/09/12 23:23:36
 */
public class OptionsJson {
    /** 参数1 */
    private String option1;
    /** 参数2 */
    private String option2;
    /** 参数3 */
    private String option3;
    /** 参数4 */
    private String option4;
    /** 参数5 */
    private String option5;
    /** 参数6 */
    private String option6;

    public String getOption1() {
        return option1;
    }

    public void setOption1(String option1) {
        this.option1 = option1;
    }

    public String getOption2() {
        return option2;
    }

    public void setOption2(String option2) {
        this.option2 = option2;
    }

    public String getOption3() {
        return option3;
    }

    public void setOption3(String option3) {
        this.option3 = option3;
    }

    public String getOption4() {
        return option4;
    }

    public void setOption4(String option4) {
        this.option4 = option4;
    }

    public String getOption5() {
        return option5;
    }

    public void setOption5(String option5) {
        this.option5 = option5;
    }

    public String getOption6() {
        return option6;
    }

    public void setOption6(String option6) {
        this.option6 = option6;
    }

    @Override
    public String toString() {
        return "OptionsJson{" +
                "option1='" + option1 + '\'' +
                ", option2='" + option2 + '\'' +
                ", option3='" + option3 + '\'' +
                ", option4='" + option4 + '\'' +
                ", option5='" + option5 + '\'' +
                ", option6='" + option6 + '\'' +
                '}';
    }
}
