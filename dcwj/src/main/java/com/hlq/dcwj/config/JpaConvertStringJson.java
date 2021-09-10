package com.hlq.dcwj.config;

import com.alibaba.fastjson.JSON;

import javax.persistence.AttributeConverter;


/**
 * @Program: JpaConvertStringJson
 * @Description: Jpa自动转换Json和String格式的数据
 * @Author: HanLinqi
 * @Date: 2021/09/09 10:38:14
 */

public class JpaConvertStringJson implements AttributeConverter<Object, String> {

    @Override
    public String convertToDatabaseColumn(Object o) {
        return o == null ? null : JSON.toJSONString(o);
    }

    @Override
    public Object convertToEntityAttribute(String s) {
        return s == null ? null : JSON.parse(s);
    }
}
