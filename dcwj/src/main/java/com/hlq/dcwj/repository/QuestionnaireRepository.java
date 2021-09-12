package com.hlq.dcwj.repository;

import com.hlq.dcwj.entity.Questionnaire;
import com.hlq.dcwj.vo.QuestionnaireVo;
import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.data.jpa.repository.Query;
import org.springframework.stereotype.Repository;

/**
 * @Program: QuestionnaireRepository
 * @Description: 查询调查问卷大类Jpa
 * @Author: HanLinqi
 * @Date: 2021/09/12 22:52:26
 */
@Repository
public interface QuestionnaireRepository extends JpaRepository<Questionnaire, Long> {

    @Query(value = "SELECT new com.hlq.dcwj.vo.QuestionnaireVo(questionnaire, question) FROM Questionnaire questionnaire, Question question WHERE  questionnaire.id = question.questionnaire.id")
    public QuestionnaireVo findQuestionnaire();
}
