package com.hlq.dcwj.repository;

import com.alibaba.fastjson.JSON;
import com.hlq.dcwj.entity.AnswerJson;
import com.hlq.dcwj.entity.OptionsJson;
import com.hlq.dcwj.entity.Question;
import com.hlq.dcwj.entity.Questionnaire;
import com.hlq.dcwj.vo.QuestionnaireVo;
import org.junit.jupiter.api.AfterEach;
import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Test;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.boot.test.context.SpringBootTest;

import java.util.Date;
import java.util.List;
import java.util.Optional;

import static org.junit.jupiter.api.Assertions.*;

@SpringBootTest
class QuestionnaireRepositoryTest {
    @Autowired
    QuestionRepository questionRepository;

    @Autowired
    QuestionnaireRepository questionnaireRepository;

    @BeforeEach
    public void init() {
        // 创建问卷
        Questionnaire questionnaire = new Questionnaire();
        questionnaire.setId(1L);
        questionnaire.setTitle("问卷1");
        questionnaire.setPublishTime(new Date());
        questionnaireRepository.save(questionnaire);

        // 在已经添加的问卷中添加试题
        Question question = new Question();
        question.setId(1L);
        question.setQuestionnaire(questionnaire);
        question.setTitle("选题题目说明");
        question.setKind("选择题");

        // 设置显示选项
        OptionsJson optionsJson = new OptionsJson();
        optionsJson.setOption1("选项1");
        optionsJson.setOption2("选项2");
        optionsJson.setOption3("选项3");
        optionsJson.setOption4("选项4");
        question.setOptions(JSON.toJSONString(optionsJson));
        // 设置正确答案
        AnswerJson answerJson = new AnswerJson();
        answerJson.setAnswer1("选项1");
        question.setAnswer(JSON.toJSONString(answerJson));

        // 绑定问卷外键
        question.setQuestionnaire(questionnaire);
        questionRepository.save(question);
    }

    @AfterEach
    public void deleteAll() {
        // 删除创建的问卷
        questionRepository.deleteAll();
        questionnaireRepository.deleteAll();
    }

    @Test
    public void baseQueryTest() {
        // 创建问卷
        Questionnaire questionnaire = new Questionnaire();
        questionnaire.setTitle("问卷1");
        questionnaire.setPublishTime(new Date());
        questionnaireRepository.save(questionnaire);
        // 查询创建的问卷
        Optional<Questionnaire> questionnaire1 = questionnaireRepository.findById(questionnaire.getId());
        System.out.println(questionnaire1);

        // 在已经添加的问卷中添加试题
        Question question = new Question();
        question.setQuestionnaire(questionnaire);
        question.setTitle("选题题目说明");
        question.setKind("选择题");

        // 设置显示选项
        OptionsJson optionsJson = new OptionsJson();
        optionsJson.setOption1("选项1");
        optionsJson.setOption2("选项2");
        optionsJson.setOption3("选项3");
        optionsJson.setOption4("选项4");
        question.setOptions(JSON.toJSONString(optionsJson));
        // 设置正确答案
        AnswerJson answerJson = new AnswerJson();
        answerJson.setAnswer1("选项1");
        question.setAnswer(JSON.toJSONString(answerJson));
        // 绑定问卷外键
        question.setQuestionnaire(questionnaire);
        questionRepository.save(question);
        // 查询调查问卷
        questionnaire1 = questionnaireRepository.findById(questionnaire.getId());
        System.out.println(questionnaire1);
        // 查询
        System.out.println(question);


    }

    @Test
    void findQuestionnaireById() {
        QuestionnaireVo questionnaireVo = questionnaireRepository.findQuestionnaire();
        System.out.println(questionnaireVo.getQuestionnaire());
        System.out.println(questionnaireVo.getQuestion());
    }
}