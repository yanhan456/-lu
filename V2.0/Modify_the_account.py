# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Modify_the_account.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!
import sqlite3
from PyQt5.QtWidgets import (QMessageBox, QLineEdit)

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(228, 285)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(10, 20, 211, 31))
        self.lineEdit.setObjectName("lineEdit")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(10, 190, 211, 31))
        self.pushButton.setObjectName("pushButton")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(10, 80, 211, 31))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_2.setEchoMode(QLineEdit.Password)
        self.lineEdit_3 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_3.setGeometry(QtCore.QRect(10, 140, 211, 31))
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 0, 72, 15))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(10, 60, 72, 15))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(10, 120, 72, 15))
        self.label_3.setObjectName("label_3")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 228, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.pushButton.clicked.connect(self.Username)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "修改账号"))
        self.label.setText(_translate("MainWindow", "原账号"))
        self.label_2.setText(_translate("MainWindow", "原密码"))
        self.label_3.setText(_translate("MainWindow", "新账号"))


    def Username(self):
        from PyQt5.QtWidgets import QMessageBox, QWidget
        widget = QWidget()
        user_name = self.lineEdit.text()
        pass_word = self.lineEdit_2.text()
        w = self.lineEdit_3.text()
        print(user_name,pass_word,w)
        conn = sqlite3.connect("inspurer.db")  # 建立数据库连接
        cur = conn.cursor()  # 得到游标对象
        cur.execute('select username,password from user')
        user = cur.fetchall()
        username = []
        password = []
        for User in user:
            username.append(User[0])
            password.append(User[1])
        print(username[0])
        print(password[0])
        if user_name == str(username[0]):
            if pass_word == str(password[0]):
                update_username = self.lineEdit_3.text()
                conn = sqlite3.connect('inspurer.db')
                cur = conn.cursor()
                sql = "update user set username=%s where username" % (update_username)
                rows = cur.execute(sql)
                conn.commit()
                QMessageBox.information(widget, '信息提示框', '账号修改成功')
            else:
                QMessageBox.information(widget, '信息提示框', '原密码错误')
                return
        # 密码判断b
        else:
            QMessageBox.information(widget, '信息提示框', '原账号错误')
            return

import sys
from PyQt5.QtWidgets import QApplication, QMainWindow



def UserWindow():
    app = QApplication(sys.argv)    # 新建一个QT应用,sys.argv参数是一个列表，从命令行输入参数。
    myWin = QMainWindow()           # 新建一个QT窗口
    ui = Ui_MainWindow()            # 创建生成的UI主窗口对象
    ui.setupUi(myWin)               # 设置在主窗口上显示UI控件
    myWin.show()                    # 显示窗口
    app.exec_()          # 退出应用
    myWin.close()

if __name__ == '__main__':
    UserWindow()
