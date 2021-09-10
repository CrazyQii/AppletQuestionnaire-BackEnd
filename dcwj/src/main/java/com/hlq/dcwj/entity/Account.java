package com.hlq.dcwj.entity;

import org.springframework.format.annotation.DateTimeFormat;

import javax.persistence.*;
import java.io.Serializable;
import java.util.Date;

/**
 * @Program: Account
 * @Description: 小程序账户基本信息存储，不需要用户输入任何信息，自动获取
 * @Author: HanLinqi
 * @Date: 2021/09/09 10:35:14
 */

@Entity
@Table(name = "DCWJ_ACCOUNT")
public class Account implements Serializable {

    /** id */
    @GeneratedValue
    @Id
    @Column(name = "ID", nullable = false, unique = true)
    private Long id;

    /** 昵称 */
    @Column(name = "NICK_NAME", nullable = false)
    private String nickName;

    /** 账号opendid */
    @Column(name = "OPEND_ID", nullable = false)
    private String openId;

    /** 账号session key */
    @Column(name = "SESSION_KEY", nullable = false)
    private String sessionKey;

    /** 账号角色 */
    @Column(name = "ROLE", nullable = false)
    private String role;

    /** 微信头像 */
    @Column(name = "AVATAR")
    private String avatar;

    /** 问卷完成状态 */
    @Column(name = "FINISH_STATUS", nullable = false)
    private Boolean finishStatus;

    /** 注册时间 */
    @DateTimeFormat(pattern = "yyyy-MM-dd HH:mm:ss")
    @Column(name = "REGISTER_TIME", nullable = false)
    private Date registerTime;

    /** 最后一次登录时间 */
    @DateTimeFormat(pattern = "yyyy-MM-dd HH:mm:ss")
    @Column(name = "LAST_LOGIN_TIME", nullable = false)
    private Date lastLoginTime;

    public Long getId() {
        return id;
    }

    public void setId(Long id) {
        this.id = id;
    }

    public String getNickName() {
        return nickName;
    }

    public void setNickName(String nickName) {
        this.nickName = nickName;
    }

    public String getOpenId() {
        return openId;
    }

    public void setOpenId(String openId) {
        this.openId = openId;
    }

    public String getSessionKey() {
        return sessionKey;
    }

    public void setSessionKey(String sessionKey) {
        this.sessionKey = sessionKey;
    }

    public String getRole() {
        return role;
    }

    public void setRole(String role) {
        this.role = role;
    }

    public String getAvatar() {
        return avatar;
    }

    public void setAvatar(String avatar) {
        this.avatar = avatar;
    }

    public Boolean getFinishStatus() {
        return finishStatus;
    }

    public void setFinishStatus(Boolean finishStatus) {
        this.finishStatus = finishStatus;
    }

    public Date getRegisterTime() {
        return registerTime;
    }

    public void setRegisterTime(Date registerTime) {
        this.registerTime = registerTime;
    }

    public Date getLastLoginTime() {
        return lastLoginTime;
    }

    public void setLastLoginTime(Date lastLoginTime) {
        this.lastLoginTime = lastLoginTime;
    }

    @Override
    public String toString() {
        return "Account{" +
                "id=" + id +
                ", nickName='" + nickName + '\'' +
                ", openId='" + openId + '\'' +
                ", sessionKey='" + sessionKey + '\'' +
                ", role='" + role + '\'' +
                ", avatar='" + avatar + '\'' +
                ", finishStatus=" + finishStatus +
                ", registerTime=" + registerTime +
                ", lastLoginTime=" + lastLoginTime +
                '}';
    }
}
