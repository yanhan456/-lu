# import WAS
# from demo import WAS
import sqlite3

from demo import WAS
# 改
# conn = sqlite3.connect('test.db')
# c = conn.cursor()
# print "Opened database successfully";
#
# c.execute("UPDATE COMPANY set SALARY = 25000.00 where ID=1")
# conn.commit()
def www():
    conn = sqlite3.connect("inspurer.db")  # 建立数据库连接
    cur = conn.cursor()  # 得到游标对象
    cur.execute('select username,password from user')
    user = cur.fetchall()
    return user
if __name__ == '__main__':
    www()