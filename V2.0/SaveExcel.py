import xlwt

def Save(username):
    wb = xlwt.Workbook()
    ws = wb.add_sheet('A Test Sheet')
    ws.write(0, 0, "工号")
    ws.write(0, 1, "姓名")
    ws.write(0, 2, "签到时间")
    ws.write(0, 3, "是否迟到(早退)")
    for i, id in enumerate(username):
        ws.write(i + 1, 0, str(id[0]))
        ws.write(i + 1, 1, id[1])
        ws.write(i + 1, 2, id[2])
        ws.write(i + 1, 3, id[3])

    wb.save(r'考勤日志('+id[1]+').xls')