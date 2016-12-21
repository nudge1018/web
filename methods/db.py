#!/usr/bin/python3
#coding:utf-8

import pymysql

conn = pymysql.connect(host="localhost", user="root", password="allinone", db="qiwsirtest",port=3306, charset="utf8")

cur = conn.cursor()
