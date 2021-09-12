package com.hlq.dcwj.repository;

import com.hlq.dcwj.entity.Account;
import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.stereotype.Repository;

/**
 * @Program: AccountRepository
 * @Description: 账户JPA
 * @Author: HanLinqi
 * @Date: 2021/09/12 20:53:47
 */
@Repository
public interface AccountRepository  extends JpaRepository<Account, Long> {
}
