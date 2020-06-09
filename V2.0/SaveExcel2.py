import xlwt


def SaveTime(x,username):
    wb = xlwt.Workbook()
    ws = wb.add_sheet('A Test Sheet')
    ws.write(0, 0, "工号")
    ws.write(0, 1, "姓名")
    ws.write(0, 2, "签到时间")
    ws.write(0, 3, "是否迟到(早退)")
    ws.write(x + 1, 0, str(username[0]))
    ws.write(x + 1, 1, username[1])
    ws.write(x + 1, 2, username[2])
    ws.write(x + 1, 3, username[3])

    wb.save(r'考勤日志(' + username[1] + ').xls')