package com.hlq.dcwj.repository;

import com.hlq.dcwj.entity.Account;
import org.springframework.data.jpa.repository.JpaRepository;

public interface AccountRepository extends JpaRepository<Account, Long> {
}
