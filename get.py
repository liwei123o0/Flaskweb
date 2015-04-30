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
@app.route("/mysql",methods=["GET","POST"])
def mysqldata():
    return mysql()

@app.route("/")
def index():
    return render_template("index.html")
@app.route("/jk")
def JKmysql():
    return render_template("mysqlmini.html")
@app.route("/zl")
def ZLmysql():
    return render_template("mysql.html")

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

def mysql():
    data=[]
    sql = Mysql(host="10.6.2.121")
    sql.conDB()
    allnews = sql.selDB(u"SELECT SQLNUM FROM echarts.user WHERE TYPE='ALLDAYNEWS'")
    allbbs  = sql.selDB(u"SELECT SQLNUM FROM echarts.user WHERE TYPE='ALLDAYBBS'")
    all     = sql.selDB(u"SELECT SQLNUM FROM echarts.user WHERE TYPE='ALLDAY'")
    data.append(int(allnews[0][0]))
    data.append(int(allbbs[0][0]))
    data.append(int(all[0][0]))
    sql.closeDB()
    return str(data)

if __name__ =="__main__":
    app.run(host="0.0.0.0",port=80,debug=True)
    # mysql()