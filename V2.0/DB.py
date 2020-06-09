# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'DB.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!
import sqlite3

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(287, 142)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(20, 10, 131, 21))
        self.label.setObjectName("label")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(20, 40, 141, 31))
        self.lineEdit.setObjectName("lineEdit")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(170, 40, 81, 31))
        self.pushButton.setObjectName("pushButton")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 287, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.pushButton.clicked.connect(self.delete_user)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "输入要删除的工号"))
        self.pushButton.setText(_translate("MainWindow", "确定删除"))

    def delete_user(self):
        from PyQt5.QtWidgets import QMessageBox, QWidget
        widget = QWidget()
        userid = self.lineEdit.text()
        print(userid)
        conn = sqlite3.connect('inspurer.db')
        cur = conn.cursor()

        sql = "delete from worker_info where id=%s " % (userid)
        rows = cur.execute(sql)
        # if rows > 0:
        QMessageBox.information(widget, '信息提示框', '删除成功')
        # else:
        #     QMessageBox.information(widget, '信息提示框', '工号不存在')
        # dir = PATH_FACE + self.name
        # for file in os.listdir(dir):
        #     os.remove(dir + "/" + file)
        #     print("已删除已录入人脸的图片", dir + "/" + file)
        # os.rmdir(PATH_FACE + self.name)
        # print("已删除已录入人脸的姓名文件夹", dir)
        # else:
        #     QMessageBox.information(widget, '信息提示框', '删除工号不存在')
        conn.commit()
        cur.close()
        conn.close()
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow

def DBWindow():
    app = QApplication(sys.argv)  # 新建一个QT应用,sys.argv参数是一个列表，从命令行输入参数。
    myWin = QMainWindow()  # 新建一个QT窗口
    ui = Ui_MainWindow()  # 创建生成的UI主窗口对象
    ui.setupUi(myWin)  # 设置在主窗口上显示UI控件
    myWin.show()  # 显示窗口
    app.exec_()  # 退出应用
    myWin.close()

if __name__ == '__main__':
    DBWindow()