package com.hlq.dcwj.repository;

import com.hlq.dcwj.entity.Account;
import org.junit.jupiter.api.Test;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.boot.test.context.SpringBootTest;

import javax.annotation.Resource;

import java.util.Date;
import java.util.Optional;

import static org.junit.jupiter.api.Assertions.*;

@SpringBootTest
class AccountRepositoryTest {
    @Autowired
    AccountRepository accountRepository;

    @Test
    public void baseQueryTest() {
        Account account = new Account();
        account.setNickName("hlq");
        account.setOpenId("op");
        account.setAvatar("avatar");
        account.setRegisterTime(new Date());
        account.setLastLoginTime(new Date());
        account.setSessionKey("123");
        account.setRole("admin");
        account.setFinishStatus(false);
        accountRepository.save(account);
        Optional<Account> account1 =  accountRepository.findById(account.getId());
        System.out.println(account1);
        // 如果存在，删除该数据
        account1.ifPresent(value -> accountRepository.deleteById(value.getId()));

    }
}