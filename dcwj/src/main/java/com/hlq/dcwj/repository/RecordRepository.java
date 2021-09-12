package com.hlq.dcwj.repository;

import com.hlq.dcwj.entity.Record;
import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.stereotype.Repository;

/**
 * @Program: RecordRepository
 * @Description: 调查记录Jpa
 * @Author: HanLinqi
 * @Date: 2021/09/12 22:54:18
 */
@Repository
public interface RecordRepository extends JpaRepository<Record, Long> {
}
