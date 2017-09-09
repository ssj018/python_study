#!/usr/bin/env python
#--coding:UTF-8--


import pymysql

db=pymysql.connect("localhost","root","","mysql")
cursor=db.cursor()

cursor.execute("select host,user,password from user")

data=cursor.fetchall()
try:
    cursor.execute("update user set password=passwd('root') where host='localhost' ")
    cursor.commit()
except Exception:
    #cursor.rollback()
    db.rollback()
cursor.execute("select host,user,password from user")
data2=cursor.fetchall()


db.close()
print data
print data2
