# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Add_records.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import sqlite3


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(654, 227)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(30, 100, 121, 31))
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(160, 100, 121, 31))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_3.setGeometry(QtCore.QRect(450, 100, 121, 31))
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(40, 70, 61, 20))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(170, 70, 72, 15))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(310, 70, 72, 15))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(460, 70, 72, 15))
        self.label_4.setObjectName("label_4")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(450, 140, 121, 31))
        self.pushButton.setObjectName("pushButton")
        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(30, 10, 121, 31))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.dateTimeEdit = QtWidgets.QDateTimeEdit(self.centralwidget)
        self.dateTimeEdit.setGeometry(QtCore.QRect(290, 100, 151, 31))
        self.dateTimeEdit.setObjectName("dateTimeEdit")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 654, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.pushButton.clicked.connect(lambda :self.Add_record(MainWindow))
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "工号"))
        self.label_2.setText(_translate("MainWindow", "姓名"))
        self.label_3.setText(_translate("MainWindow", "日期"))
        self.label_4.setText(_translate("MainWindow", "状态"))
        self.pushButton.setText(_translate("MainWindow", "保存"))
        self.comboBox.setItemText(0, _translate("MainWindow", "上班考勤"))
        self.comboBox.setItemText(1, _translate("MainWindow", "下班考勤"))

    def Add_record(self, MainWindow):
        user_id = self.lineEdit.text()
        user_name = self.lineEdit_2.text()
        timestart = self.dateTimeEdit.text()
        # timestart = "1"
        state = self.lineEdit_3.text()
        type = self.comboBox.currentIndex()
        print(user_name, user_id, timestart, state,type)
        conn = sqlite3.connect("inspurer.db")  # 建立数据库连接
        cur = conn.cursor()  # 得到游标对象
        if type == 0:
            cur.execute("insert into logcat (id,name,datetime,late) values(?,?,?,?)",
                        (user_id,user_name,timestart,state))
            print("写日志成功")
        if type == 1:
            cur.execute("insert into later_work (id,name,datetime,late) values(?,?,?,?)",
                        (user_id,user_name,timestart,state))
            print("写下班日志成功")
        QtWidgets.QMessageBox.information(MainWindow, "提示信息", "保存成功", QtWidgets.QMessageBox.Ok)
        cur.close()
        conn.commit()
        conn.close()

import sys
from PyQt5.QtWidgets import QApplication, QMainWindow

def AddWindow():
    app = QApplication(sys.argv)  # 新建一个QT应用,sys.argv参数是一个列表，从命令行输入参数。
    myWin = QMainWindow()  # 新建一个QT窗口
    ui = Ui_MainWindow()  # 创建生成的UI主窗口对象
    ui.setupUi(myWin)  # 设置在主窗口上显示UI控件
    myWin.show()  # 显示窗口
    app.exec_()  # 退出应用
    myWin.close()

if __name__ == '__main__':
    AddWindow()