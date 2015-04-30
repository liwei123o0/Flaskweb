# -*- coding: utf-8 -*-
#! /usr/bin/env python
from mysqlutile import Mysql
u'''
查询入库量py
1.mysqlday()方法    //查询每天的总入库量
2.mysqlweek()方法   //查询上周的总入库量
3.mysqlmonth()方法  //查询上月的总入库量
4.mysqlyear()方法   //查询今年的总入库量
'''

#查询每天的总入库量
def mysqlday():
    m = Mysql(host="10.6.2.121")
    m.conDB()
    news =  m.selDB("SELECT COUNT(*) FROM scrapy.news WHERE DAY(date_format(INSERT_TIME,'%Y-%m-%d')) = DAY(now()); ")[0][0]
    bbs =   m.selDB("SELECT COUNT(*) FROM scrapy.bbs WHERE DAY(date_format(INSERT_TIME,'%Y-%m-%d')) = DAY(now()); ")[0][0]
    number = news+bbs
    print number
    # m.selDB("INSERT INTO echarts.user(TYPE,SQLNUM) VALUES('ALLDAY','%s')"%number)
    m.selDB("UPDATE echarts.user SET SQLNUM='%s' WHERE TYPE='ALLDAY'"% number)
    m.closeDB()
#查询上周的总入库量
def mysqlweek():
    m = Mysql(host="10.6.2.121")
    m.conDB()
    news =  m.selDB("SELECT COUNT(*) FROM scrapy.news WHERE YEARWEEK(date_format(INSERT_TIME,'%Y-%m-%d')) = YEARWEEK(now())-1; ")[0][0]
    bbs =   m.selDB("SELECT COUNT(*) FROM scrapy.bbs WHERE YEARWEEK(date_format(INSERT_TIME,'%Y-%m-%d')) = YEARWEEK(now())-1;")[0][0]
    number = news+bbs
    print number
    # m.selDB("INSERT INTO echarts.user(TYPE,SQLNUM) VALUES('ALLWEEK','%s')"%number)
    m.selDB("UPDATE echarts.user SET SQLNUM='%s' WHERE TYPE='ALLWEEK'"% number)
    m.closeDB()
#查询上月的总入库量
def mysqlmonth():
    m = Mysql(host="10.6.2.121")
    m.conDB()
    news =  m.selDB("SELECT COUNT(*) FROM scrapy.news WHERE DATE_FORMAT(INSERT_TIME,'%Y-%m')=DATE_FORMAT(DATE_SUB(curdate(), INTERVAL 0 MONTH),'%Y-%m'); ")[0][0]
    bbs =   m.selDB("SELECT COUNT(*) FROM scrapy.bbs WHERE DATE_FORMAT(INSERT_TIME,'%Y-%m')=DATE_FORMAT(DATE_SUB(curdate(), INTERVAL 0 MONTH),'%Y-%m');")[0][0]
    number = news+bbs
    print number
    # m.selDB("INSERT INTO echarts.user(TYPE,SQLNUM) VALUES('ALLMONTH','%s')"%number)
    m.selDB("UPDATE echarts.user SET SQLNUM='%s' WHERE TYPE='ALLMONTH'"% number)
    m.closeDB()
#查询今年的总入库量
def mysqlyear():
    m = Mysql(host="10.6.2.121")
    m.conDB()
    news =  m.selDB("SELECT COUNT(*) FROM scrapy.news WHERE YEAR(date_format(INSERT_TIME,'%Y-%m-%d')) = YEAR(now()); ")[0][0]
    bbs =   m.selDB("SELECT COUNT(*) FROM scrapy.bbs WHERE YEAR(date_format(INSERT_TIME,'%Y-%m-%d')) = YEAR(now());")[0][0]
    number = news+bbs
    print number
    # m.selDB("INSERT INTO echarts.user(TYPE,SQLNUM) VALUES('ALLYEAR','%s')"%number)
    m.selDB("UPDATE echarts.user SET SQLNUM='%s' WHERE TYPE='ALLYEAR'"% number)
    m.closeDB()
#查询每天news的总入库量
def mysqldaynews():
    m = Mysql(host="10.6.2.121")
    m.conDB()
    news =  m.selDB("SELECT COUNT(*) FROM scrapy.news WHERE DAY(date_format(INSERT_TIME,'%Y-%m-%d')) = DAY(now()); ")[0][0]
    number = news
    print number
    # m.selDB("INSERT INTO echarts.user(TYPE,SQLNUM) VALUES('ALLDAYNEWS','%s')"%number)
    m.selDB("UPDATE echarts.user SET SQLNUM='%s' WHERE TYPE='ALLDAYNEWS'"% number)
    m.closeDB()
#查询上周news的总入库量
def mysqlweeknews():
    m = Mysql(host="10.6.2.121")
    m.conDB()
    news =  m.selDB("SELECT COUNT(*) FROM scrapy.news WHERE YEARWEEK(date_format(INSERT_TIME,'%Y-%m-%d')) = YEARWEEK(now())-1; ")[0][0]
    number = news
    print number
    # m.selDB("INSERT INTO echarts.user(TYPE,SQLNUM) VALUES('ALLWEEKNEWS','%s')"%number)
    m.selDB("UPDATE echarts.user SET SQLNUM='%s' WHERE TYPE='ALLWEEKNEWS'"% number)
    m.closeDB()
#查询上月news的总入库量
def mysqlmonthnews():
    m = Mysql(host="10.6.2.121")
    m.conDB()
    news =  m.selDB("SELECT COUNT(*) FROM scrapy.news WHERE DATE_FORMAT(INSERT_TIME,'%Y-%m')=DATE_FORMAT(DATE_SUB(curdate(), INTERVAL 0 MONTH),'%Y-%m'); ")[0][0]
    number = news
    print number
    # m.selDB("INSERT INTO echarts.user(TYPE,SQLNUM) VALUES('ALLMONTHNEWS','%s')"%number)
    m.selDB("UPDATE echarts.user SET SQLNUM='%s' WHERE TYPE='ALLMONTHNEWS'"% number)
    m.closeDB()
#查询今年bbs的总入库量
def mysqlyearnews():
    m = Mysql(host="10.6.2.121")
    m.conDB()
    bbs =  m.selDB("SELECT COUNT(*) FROM scrapy.news WHERE YEAR(date_format(INSERT_TIME,'%Y-%m-%d')) = YEAR(now()); ")[0][0]
    number = bbs
    print number
    # m.selDB("INSERT INTO echarts.user(TYPE,SQLNUM) VALUES('ALLYEARNEWS','%s')"%number)
    m.selDB("UPDATE echarts.user SET SQLNUM='%s' WHERE TYPE='ALLYEARNEWS'"% number)
    m.closeDB()
#查询每天bbs的总入库量
def mysqldaybbs():
    m = Mysql(host="10.6.2.121")
    m.conDB()
    bbs =  m.selDB("SELECT COUNT(*) FROM scrapy.bbs WHERE DAY(date_format(INSERT_TIME,'%Y-%m-%d')) = DAY(now()); ")[0][0]
    number = bbs
    print number
    # m.selDB("INSERT INTO echarts.user(TYPE,SQLNUM) VALUES('ALLDAYBBS','%s')"%number)
    m.selDB("UPDATE echarts.user SET SQLNUM='%s' WHERE TYPE='ALLDAYBBS'"% number)
    m.closeDB()
#查询上周bbs的总入库量
def mysqlweekbbs():
    m = Mysql(host="10.6.2.121")
    m.conDB()
    bbs =  m.selDB("SELECT COUNT(*) FROM scrapy.bbs WHERE YEARWEEK(date_format(INSERT_TIME,'%Y-%m-%d')) = YEARWEEK(now())-1; ")[0][0]
    number = bbs
    print number
    # m.selDB("INSERT INTO echarts.user(TYPE,SQLNUM) VALUES('ALLWEEKBBS','%s')"%number)
    m.selDB("UPDATE echarts.user SET SQLNUM='%s' WHERE TYPE='ALLWEEKBBS'"% number)
    m.closeDB()
#查询上月bbs的总入库量
def mysqlmonthbbs():
    m = Mysql(host="10.6.2.121")
    m.conDB()
    bbs =  m.selDB("SELECT COUNT(*) FROM scrapy.bbs WHERE DATE_FORMAT(INSERT_TIME,'%Y-%m')=DATE_FORMAT(DATE_SUB(curdate(), INTERVAL 0 MONTH),'%Y-%m'); ")[0][0]
    number = bbs
    print number
    # m.selDB("INSERT INTO echarts.user(TYPE,SQLNUM) VALUES('ALLMONTHBBS','%s')"%number)
    m.selDB("UPDATE echarts.user SET SQLNUM='%s' WHERE TYPE='ALLMONTHBBS'"% number)
    m.closeDB()
#查询今年bbs的总入库量
def mysqlyearbbs():
    m = Mysql(host="10.6.2.121")
    m.conDB()
    news =  m.selDB("SELECT COUNT(*) FROM scrapy.bbs WHERE YEAR(date_format(INSERT_TIME,'%Y-%m-%d')) = YEAR(now()); ")[0][0]
    number = news
    print number
    # m.selDB("INSERT INTO echarts.user(TYPE,SQLNUM) VALUES('ALLYEARNEWS','%s')"%number)
    m.selDB("UPDATE echarts.user SET SQLNUM='%s' WHERE TYPE='ALLYEARNEWS'"% number)
    m.closeDB()
#测试
if __name__=="__main__":
    mysqlday()
    mysqlweek()
    mysqlmonth()
    mysqlyear()
    mysqldaynews()
    mysqlweeknews()
    mysqlmonthnews()
    mysqlyearnews()
    mysqldaybbs()
    mysqlweekbbs()
    mysqlmonthbbs()
    mysqlyearbbs()