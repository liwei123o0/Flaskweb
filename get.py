# -*- coding: utf-8 -*-
#! /usr/bin/env python
from flask import Flask,render_template,request,jsonify
from mysqlutile import Mysql
import json
app = Flask(__name__)

#十分钟实时数据
@app.route("/mysqlsel",methods=["GET","POST"])
def get():
    a = selmysql()
    a = a[0]+",%s"%a[1]+",%s"%a[2]+",%s"%a[3]+",%s"%a[4]+",%s"%a[5]+",%s"%a[6]+",%s"%a[7]+",%s"%a[8]+",%s"%a[9]
    return a
@app.route("/")
def index():
    return render_template("index.html")
@app.route("/jk")
def JKmysql():
    return render_template("mysqlmini.html")
@app.route("/zl")
def ZLmysql():
    return render_template("mysql.html")
@app.route("/mysqljk")
def mysqljk():
    return render_template("mysqljk.html")
#实时10分钟数据入库量
def selmysql():
    data =[]
    My = Mysql(host="10.6.2.121")
    My.conDB()
    for i in range(10,110,10):
        rkl= My.selDB(u"SELECT COUNT(*) FROM scrapy.news WHERE INSERT_TIME>=NOW()-INTERVAL %d MINUTE AND  INSERT_TIME< NOW() - INTERVAL %d MINUTE"%(i,i-10))[0][0]
        data.append(str(rkl))
    My.closeDB()
    return data
#获取当天总入库量
@app.route("/mysql",methods=["GET","POST"])
def mysql():
    sql = Mysql(host="10.6.2.121")
    sql.conDB()
    #获取当天入库量
    allnews = sql.selDB(u"SELECT SQLNUM FROM echarts.user WHERE TYPE='ALLDAYNEWS'")[0][0]
    allbbs  = sql.selDB(u"SELECT SQLNUM FROM echarts.user WHERE TYPE='ALLDAYBBS'")[0][0]
    all     = sql.selDB(u"SELECT SQLNUM FROM echarts.user WHERE TYPE='ALLDAY'")[0][0]
    #获取上周入库量
    allweeknews = sql.selDB(u"SELECT SQLNUM FROM echarts.user WHERE TYPE='ALLWEEKNEWS'")[0][0]
    allweekbbs  = sql.selDB(u"SELECT SQLNUM FROM echarts.user WHERE TYPE='ALLWEEKBBS'")[0][0]
    allweek     = sql.selDB(u"SELECT SQLNUM FROM echarts.user WHERE TYPE='ALLWEEK'")[0][0]
    #获取上月入库量
    allmonthnews = sql.selDB(u"SELECT SQLNUM FROM echarts.user WHERE TYPE='ALLMONTHNEWS'")[0][0]
    allmonthbbs  = sql.selDB(u"SELECT SQLNUM FROM echarts.user WHERE TYPE='ALLMONTHBBS'")[0][0]
    allmonth     = sql.selDB(u"SELECT SQLNUM FROM echarts.user WHERE TYPE='ALLMONTH'")[0][0]
    #获取当年入库总量
    allyearnews = sql.selDB(u"SELECT SQLNUM FROM echarts.user WHERE TYPE='ALLYEARNEWS'")[0][0]
    allyearbbs  = sql.selDB(u"SELECT SQLNUM FROM echarts.user WHERE TYPE='ALLYEARBBS'")[0][0]
    allyear     = sql.selDB(u"SELECT SQLNUM FROM echarts.user WHERE TYPE='ALLYEAR'")[0][0]
    data={
        "allrkl":"[%s,%s,%s]"%(allnews,allbbs,all),
        "allweek":"[%s,%s,%s]"%(allweeknews,allweekbbs,allweek),
        "allmonth":"[%s,%s,%s]"%(allmonthnews,allmonthbbs,allmonth),
        "allyear":"[%s,%s,%s]"%(allyearnews,allyearbbs,allyear)
        }
    sql.closeDB()
    print data
    return jsonify(data)
if __name__ =="__main__":
    app.run(host="0.0.0.0",port=80,debug=True)
    # print mysql()