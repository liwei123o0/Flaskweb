# -*- coding: utf-8 -*-
#! /usr/bin/env python
from mysqlutile import Mysql

#查询scrapy每天的入库总量
def mysqlnum():
    m = Mysql(host="10.6.2.121")
    m.conDB()
    news =  m.selDB("SELECT COUNT(*) FROM scrapy.news WHERE DAY(date_format(INSERT_TIME,'%Y-%m-%d')) = DAY(now())-1; ")[0][0]
    bbs =   m.selDB("SELECT COUNT(*) FROM scrapy.bbs WHERE DAY(date_format(INSERT_TIME,'%Y-%m-%d')) = DAY(now())-1; ")[0][0]
    number = news+bbs
    print number
    m.selDB("INSERT INTO echarts.user(TYPE,SQLNUM) VALUES('ALL','%s')"%number)
    m.closeDB()