package com.hlq.dcwj.repository;

import com.hlq.dcwj.entity.Question;
import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.stereotype.Repository;

import java.util.List;

/**
 * @Program: QuestionRepository
 * @Description: 选项Jpa
 * @Author: HanLinqi
 * @Date: 2021/09/12 22:55:07
 */
@Repository
public interface QuestionRepository extends JpaRepository<Question, Long> {
}
