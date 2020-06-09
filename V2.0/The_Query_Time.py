# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'The_Query_Time.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!
import sqlite3
from PyQt5.QtWidgets import QTableWidgetItem
from PyQt5 import QtCore, QtGui, QtWidgets
from datetime import datetime
import xlwt

from SaveExcel2 import SaveTime


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(748, 644)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.dateEdit = QtWidgets.QDateEdit(self.centralwidget)
        self.dateEdit.setGeometry(QtCore.QRect(30, 20, 101, 31))
        self.dateEdit.setObjectName("dateEdit")
        self.dateEdit_2 = QtWidgets.QDateEdit(self.centralwidget)
        self.dateEdit_2.setGeometry(QtCore.QRect(140, 20, 101, 31))
        self.dateEdit_2.setObjectName("dateEdit_2")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(30, 0, 72, 15))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(140, 0, 72, 15))
        self.label_2.setObjectName("label_2")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(440, 80, 151, 31))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(600, 560, 141, 31))
        self.pushButton_2.setObjectName("pushButton_2")
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(30, 120, 561, 471))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(4)
        self.tableWidget.setRowCount(20)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(0, 0, item)
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(30, 80, 401, 31))
        self.lineEdit.setObjectName("lineEdit")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(30, 60, 131, 16))
        self.label_3.setObjectName("label_3")
        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(250, 20, 101, 31))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox_2 = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_2.setGeometry(QtCore.QRect(360, 20, 121, 31))
        self.comboBox_2.setObjectName("comboBox_2")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 748, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.pushButton.clicked.connect(lambda: self.Attendance_log(MainWindow))
        self.pushButton_2.clicked.connect(lambda :self.SaveExecl(MainWindow))
        self.comboBox.activated['int'].connect(MainWindow.update)
        self.comboBox_2.activated['int'].connect(MainWindow.update)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "开始时间"))
        self.label_2.setText(_translate("MainWindow", "结束时间"))
        self.pushButton.setText(_translate("MainWindow", "查询"))
        self.pushButton_2.setText(_translate("MainWindow", "打印"))
        item = self.tableWidget.verticalHeaderItem(0)
        item.setText(_translate("MainWindow", "1"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "工号"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "姓名"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "签到时间"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "是否迟到(或早退)"))
        __sortingEnabled = self.tableWidget.isSortingEnabled()
        self.tableWidget.setSortingEnabled(False)
        self.tableWidget.setSortingEnabled(__sortingEnabled)
        self.label_3.setText(_translate("MainWindow", "输入工号或名字"))
        self.comboBox.setItemText(0, _translate("MainWindow", "搜索名字"))
        self.comboBox.setItemText(1, _translate("MainWindow", "搜索工号"))
        self.comboBox_2.setItemText(0, _translate("MainWindow", "上班考勤日志"))
        self.comboBox_2.setItemText(1, _translate("MainWindow", "下班考勤日志"))

    def Attendance_log(self,MainWindow):
        i = self.comboBox.currentIndex()

        if i == 0:
            i2 = self.comboBox_2.currentIndex()

            name = self.lineEdit.text()

            conn = sqlite3.connect("inspurer.db")  # 建立数据库连接
            cur = conn.cursor()  # 得到游标对象
            if i2 == 0:
                cur.execute("select id,name,datetime,late from logcat where name='%s'" % (name))
            if i2 == 1:
                cur.execute("select id,name,datetime,late from later_work where name='%s'" % (name))
            username = cur.fetchall()

            timestart = self.dateEdit.text()
            endtime = self.dateEdit_2.text()
            time = datetime.strptime(timestart, '%Y/%m/%d')  # 根据字符串本身的格式进行转换
            timestart = time.strftime('%Y-%m-%d')
            # print(timestart)
            time = datetime.strptime(endtime, '%Y/%m/%d')  # 根据字符串本身的格式进行转换
            endtime = time.strftime('%Y-%m-%d')
            # print(endtime)

            self.tableWidget.clearContents()  # 删除数据
            if username:
                x = 0
                for username in username:
                    QueryTime = username[2][1:username[2].index(" ")]
                    if timestart <= QueryTime <= endtime:
                        print(username)
                        id = QTableWidgetItem(str(username[0]))
                        self.tableWidget.setItem(x, 0, id)

                        name = QTableWidgetItem(str(username[1]))
                        self.tableWidget.setItem(x, 1, name)

                        timeword = QTableWidgetItem(str(username[2]))
                        self.tableWidget.setItem(x, 2, timeword)

                        situation = QTableWidgetItem(str(username[3]))
                        self.tableWidget.setItem(x, 3, situation)
                        x = x + 1
                    # elif username is None:
                    #     QtWidgets.QMessageBox.information(MainWindow, "提示信息", "时间区间没有记录", QtWidgets.QMessageBox.Ok)
            else:
                QtWidgets.QMessageBox.information(MainWindow, "提示信息", "姓名不存在", QtWidgets.QMessageBox.Ok)

        if i == 1:
            i2 = self.comboBox_2.currentIndex()

            id = self.lineEdit.text()

            conn = sqlite3.connect("inspurer.db")  # 建立数据库连接
            cur = conn.cursor()  # 得到游标对象
            if i2 == 0:
                cur.execute("select id,name,datetime,late from logcat where id='%s'" % (id))
            if i2 == 1:
                cur.execute("select id,name,datetime,late from later_work where id='%s'" % (id))
            userid = cur.fetchall()

            timestart = self.dateEdit.text()
            endtime = self.dateEdit_2.text()
            time = datetime.strptime(timestart, '%Y/%m/%d')  # 根据字符串本身的格式进行转换
            timestart = time.strftime('%Y-%m-%d')
            # print(timestart)
            time = datetime.strptime(endtime, '%Y/%m/%d')  # 根据字符串本身的格式进行转换
            endtime = time.strftime('%Y-%m-%d')
            # print(endtime)

            self.tableWidget.clearContents()
            if userid:
                x = 0
                for username in userid:
                    QueryTime = username[2][1:username[2].index(" ")]
                    if timestart <= QueryTime <= endtime:
                        print(username)
                        id = QTableWidgetItem(str(username[0]))
                        self.tableWidget.setItem(x, 0, id)

                        name = QTableWidgetItem(str(username[1]))
                        self.tableWidget.setItem(x, 1, name)

                        timeword = QTableWidgetItem(str(username[2]))
                        self.tableWidget.setItem(x, 2, timeword)

                        situation = QTableWidgetItem(str(username[3]))
                        self.tableWidget.setItem(x, 3, situation)
                        x = x + 1
                    # elif username is None:
                    #     QtWidgets.QMessageBox.information(MainWindow, "提示信息", "时间区间没有记录", QtWidgets.QMessageBox.Ok)
            else:
                QtWidgets.QMessageBox.information(MainWindow, "提示信息", "工号不存在", QtWidgets.QMessageBox.Ok)

    def SaveExecl(self,MainWindow):
        i = self.comboBox.currentIndex()

        if i == 0:
            i2 = self.comboBox_2.currentIndex()

            name = self.lineEdit.text()

            conn = sqlite3.connect("inspurer.db")  # 建立数据库连接
            cur = conn.cursor()  # 得到游标对象
            if i2 == 0:
                cur.execute("select id,name,datetime,late from logcat where name='%s'" % (name))
            if i2 == 1:
                cur.execute("select id,name,datetime,late from later_work where name='%s'" % (name))
            username = cur.fetchall()

            timestart = self.dateEdit.text()
            endtime = self.dateEdit_2.text()
            time = datetime.strptime(timestart, '%Y/%m/%d')  # 根据字符串本身的格式进行转换
            timestart = time.strftime('%Y-%m-%d')
            # print(timestart)
            time = datetime.strptime(endtime, '%Y/%m/%d')  # 根据字符串本身的格式进行转换
            endtime = time.strftime('%Y-%m-%d')
            # print(endtime)

            self.tableWidget.clearContents()  # 删除数据
            if username:
                x = 1
                wb = xlwt.Workbook()
                ws = wb.add_sheet('A Test Sheet')
                ws.write(0, 0, "工号")
                ws.write(0, 1, "姓名")
                ws.write(0, 2, "签到时间")
                ws.write(0, 3, "是否迟到(早退)")
                for username in username:
                    QueryTime = username[2][1:username[2].index(" ")]
                    if timestart <= QueryTime <= endtime:
                        print(username)
                        ws.write(x, 0, str(username[0]))
                        ws.write(x, 1, username[1])
                        ws.write(x, 2, username[2])
                        ws.write(x, 3, username[3])
                        print("22")
                        x = x + 1
                wb.save(r'考勤日志(' + username[1] + ').xls')
                QtWidgets.QMessageBox.information(MainWindow, "提示信息", "打印成功", QtWidgets.QMessageBox.Ok)
            else:
                QtWidgets.QMessageBox.information(MainWindow, "提示信息", "名字不存在", QtWidgets.QMessageBox.Ok)


        if i == 1:
            i2 = self.comboBox_2.currentIndex()

            id = self.lineEdit.text()

            conn = sqlite3.connect("inspurer.db")  # 建立数据库连接
            cur = conn.cursor()  # 得到游标对象
            if i2 == 0:
                cur.execute("select id,name,datetime,late from logcat where id='%s'" % (id))
            if i2 == 1:
                cur.execute("select id,name,datetime,late from later_work where id='%s'" % (id))
            userid = cur.fetchall()
            timestart = self.dateEdit.text()
            endtime = self.dateEdit_2.text()
            time = datetime.strptime(timestart, '%Y/%m/%d')  # 根据字符串本身的格式进行转换
            timestart = time.strftime('%Y-%m-%d')
            # print(timestart)
            time = datetime.strptime(endtime, '%Y/%m/%d')  # 根据字符串本身的格式进行转换
            endtime = time.strftime('%Y-%m-%d')
            # print(endtime)

            self.tableWidget.clearContents()
            if userid:
                x = 1
                wb = xlwt.Workbook()
                ws = wb.add_sheet('A Test Sheet')
                ws.write(0, 0, "工号")
                ws.write(0, 1, "姓名")
                ws.write(0, 2, "签到时间")
                ws.write(0, 3, "是否迟到(早退)")
                for username in userid:
                    QueryTime = username[2][1:username[2].index(" ")]
                    if timestart <= QueryTime <= endtime:
                        print(username,333)
                        ws.write(x, 0, str(username[0]))
                        ws.write(x, 1, username[1])
                        ws.write(x, 2, username[2])
                        ws.write(x, 3, username[3])
                        
                        x = x + 1
                    wb.save(r'考勤日志(' + username[1] + ').xls')
                QtWidgets.QMessageBox.information(MainWindow, "提示信息", "打印成功", QtWidgets.QMessageBox.Ok)

            else:
                QtWidgets.QMessageBox.information(MainWindow, "提示信息", "工号不存在", QtWidgets.QMessageBox.Ok)



import sys
from PyQt5.QtWidgets import QApplication, QMainWindow

def TimeWindow():
    app = QApplication(sys.argv)  # 新建一个QT应用,sys.argv参数是一个列表，从命令行输入参数。
    myWin = QMainWindow()  # 新建一个QT窗口
    ui = Ui_MainWindow()  # 创建生成的UI主窗口对象
    ui.setupUi(myWin)  # 设置在主窗口上显示UI控件
    myWin.show()  # 显示窗口
    app.exec_()  # 退出应用
    myWin.close()

if __name__ == '__main__':
    TimeWindow()