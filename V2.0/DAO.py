import sqlite3

def timedao():
    usertime = []
    conn = sqlite3.connect('inspurer.db')
    cur = conn.cursor()
    cur.execute('select worktime,endtime from time')
    time = cur.fetchall()
    for time1 in time:
        usertime.append(time1[0])
        usertime.append(time1[1])

    return usertime






if __name__ == '__main__':
    timedao()