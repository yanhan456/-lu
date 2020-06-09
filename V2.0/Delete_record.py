# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Delete_record.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import sqlite3


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(317, 213)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(30, 30, 121, 31))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(30, 90, 121, 31))
        self.lineEdit.setObjectName("lineEdit")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(160, 90, 91, 31))
        self.pushButton.setObjectName("pushButton")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(30, 70, 121, 16))
        self.label.setObjectName("label")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 317, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.pushButton.clicked.connect(self.Deleterecord)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.comboBox.setItemText(0, _translate("MainWindow", "上班考勤日志"))
        self.comboBox.setItemText(1, _translate("MainWindow", "下班考勤日志"))
        self.pushButton.setText(_translate("MainWindow", "删除"))
        self.label.setText(_translate("MainWindow", "输入要删除的工号"))

    def Deleterecord(self):
        from PyQt5.QtWidgets import QMessageBox, QWidget
        widget = QWidget()
        userid = self.lineEdit.text()
        type = self.comboBox.currentIndex()
        print(userid,type)
        conn = sqlite3.connect('inspurer.db')

        cur = conn.cursor()

        if type == 0:
            sql = "delete from logcat where id=%s " % (userid)
        if type == 1:
            sql = "delete from later_work where id=%s " % (userid)
        try:
            cur.execute(sql)
            conn.commit()
            QMessageBox.information(widget, '信息提示框', '删除成功')
        except Exception as e:
            print(e)
            QMessageBox.information(widget, '信息提示框', '工号不存在')
            conn.rollback()
        finally:
            cur.close()
            conn.close()





import sys
from PyQt5.QtWidgets import QApplication, QMainWindow

def Delete_Record():
    app = QApplication(sys.argv)  # 新建一个QT应用,sys.argv参数是一个列表，从命令行输入参数。
    myWin = QMainWindow()  # 新建一个QT窗口
    ui = Ui_MainWindow()  # 创建生成的UI主窗口对象
    ui.setupUi(myWin)  # 设置在主窗口上显示UI控件
    myWin.show()  # 显示窗口
    app.exec_()  # 退出应用
    myWin.close()

if __name__ == '__main__':
    Delete_Record()