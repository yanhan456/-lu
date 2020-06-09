# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '修改签到时间.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!
import sqlite3

from PyQt5 import QtCore, QtGui, QtWidgets




class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(371, 171)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.timeEdit = QtWidgets.QTimeEdit(self.centralwidget)
        self.timeEdit.setGeometry(QtCore.QRect(20, 30, 201, 31))
        self.timeEdit.setObjectName("timeEdit")
        self.timeEdit_2 = QtWidgets.QTimeEdit(self.centralwidget)
        self.timeEdit_2.setGeometry(QtCore.QRect(20, 70, 201, 31))
        self.timeEdit_2.setObjectName("timeEdit_2")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(230, 30, 101, 31))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(230, 70, 101, 31))
        self.pushButton_2.setObjectName("pushButton_2")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 371, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.pushButton.clicked.connect(self.Work_Sign)
        self.pushButton_2.clicked.connect(self.Worktime_end)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "上班签到时间"))
        self.pushButton_2.setText(_translate("MainWindow", "下班签到时间"))


    def Work_Sign(self):
        from PyQt5.QtWidgets import QMessageBox, QWidget
        widget = QWidget()
        worktime = self.timeEdit.text()
        index=worktime.index(":")

        if index == 1:
            worktime = "0"+worktime+":00"
        if  index == 2:
            worktime = worktime + ":00"
        conn = sqlite3.connect('inspurer.db')
        cur = conn.cursor()
        sql = "update time set worktime=%r where worktime" % (worktime)
        cur.execute(sql)
        conn.commit()
        QMessageBox.information(widget, '信息提示框', '上班签到时间修改成功')




    def Worktime_end(self):
        from PyQt5.QtWidgets import QMessageBox, QWidget
        widget = QWidget()
        workend = self.timeEdit_2.text()
        index = workend.index(":")
        if index == 1:
            workend = "0" + workend + ":00"
        if index == 2:
            workend = workend + ":00"
        conn = sqlite3.connect('inspurer.db')
        cur = conn.cursor()
        sql = "update time set endtime=%r where endtime" % (workend)
        cur.execute(sql)
        conn.commit()
        QMessageBox.information(widget, '信息提示框', '下班签到时间修改成功')





import sys
from PyQt5.QtWidgets import QApplication, QMainWindow



def WorkTimeWindow():
    app = QApplication(sys.argv)    # 新建一个QT应用,sys.argv参数是一个列表，从命令行输入参数。
    myWin = QMainWindow()           # 新建一个QT窗口
    ui = Ui_MainWindow()            # 创建生成的UI主窗口对象
    ui.setupUi(myWin)               # 设置在主窗口上显示UI控件
    myWin.show()                    # 显示窗口
    app.exec_()          # 退出应用
    myWin.close()

if __name__ == '__main__':
    WorkTimeWindow()
