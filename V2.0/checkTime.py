import sqlite3

conn = sqlite3.connect("inspurer.db")  # 建立数据库连接
cur = conn.cursor()  # 得到游标对象

cur.execute("select id,name,datetime,late from logcat ")

username = cur.fetchall()
timestart = '2019-12-23'
endtime = '2019-12-25'
for username in username:

    time = username[2][1:username[2].index(" ")]
    if timestart <= time <= endtime:
        print(username)
    else:
        print("2")
