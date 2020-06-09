# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'QTmain.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!
import sqlite3

import xlrd
import xlwt
from PyQt5 import QtCore, QtWidgets

from SaveExcel import Save


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(30, 30, 471, 31))
        self.lineEdit.setObjectName("lineEdit")
        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(260, 0, 121, 31))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(30, 70, 621, 471))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(4)
        self.tableWidget.setRowCount(20)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(660, 510, 111, 31))
        self.pushButton.setObjectName("pushButton")
        self.comboBox_2 = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_2.setGeometry(QtCore.QRect(380, 0, 121, 31))
        self.comboBox_2.setObjectName("comboBox_2")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(510, 30, 141, 31))
        self.pushButton_2.setObjectName("pushButton_2")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.comboBox.activated['int'].connect(MainWindow.update)
        self.pushButton.clicked.connect(lambda :self.Excel(MainWindow))
        self.comboBox_2.activated['int'].connect(MainWindow.update)
        self.pushButton_2.clicked.connect(lambda: self.text(MainWindow))
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.comboBox.setItemText(0, _translate("MainWindow", "搜索名字"))
        self.comboBox.setItemText(1, _translate("MainWindow", "搜索工号"))
        item = self.tableWidget.verticalHeaderItem(0)
        item.setText(_translate("MainWindow", "1"))
        item = self.tableWidget.verticalHeaderItem(1)
        item.setText(_translate("MainWindow", "2"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "工号"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "姓名"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "签到时间"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "是否迟到(或早退)"))
        self.pushButton.setText(_translate("MainWindow", "打印"))
        self.comboBox_2.setItemText(0, _translate("MainWindow", "上班考勤"))
        self.comboBox_2.setItemText(1, _translate("MainWindow", "下班考勤"))
        self.pushButton_2.setText(_translate("MainWindow", "确定搜索"))

    def text(self,MainWindow):

        # print(self.lineEdit.text())
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
            print(username)
            self.tableWidget.clearContents() # 删除数据
            if username :
                from PyQt5.QtWidgets import QTableWidgetItem
                for x, origin in enumerate(username):
                    newItem = QTableWidgetItem(str(origin[0]))
                    self.tableWidget.setItem(x, 0, newItem)

                    newItem = QTableWidgetItem(origin[1])
                    self.tableWidget.setItem(x, 1, newItem)

                    newItem = QTableWidgetItem(origin[2])
                    self.tableWidget.setItem(x, 2, newItem)

                    newItem = QTableWidgetItem(origin[3])
                    self.tableWidget.setItem(x, 3, newItem)
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

            # print(userid)
            self.tableWidget.clearContents()
            if userid:
                from PyQt5.QtWidgets import QTableWidgetItem
                for x,origin in enumerate(userid):

                    newItem = QTableWidgetItem(str(origin[0]))
                    self.tableWidget.setItem(x, 0, newItem)

                    newItem = QTableWidgetItem(origin[1])
                    self.tableWidget.setItem(x, 1, newItem)

                    newItem = QTableWidgetItem(origin[2])
                    self.tableWidget.setItem(x, 2, newItem)

                    newItem = QTableWidgetItem(origin[3])
                    self.tableWidget.setItem(x, 3, newItem)
            else:
                QtWidgets.QMessageBox.information(MainWindow, "提示信息", "工号不存在", QtWidgets.QMessageBox.Ok)




    def Excel(self,MainWindow):

        # print(self.lineEdit.text())
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
            print(username)
            if username:
                Save(username)
                QtWidgets.QMessageBox.information(MainWindow, "提示信息", "打印成功", QtWidgets.QMessageBox.Ok)
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
            print(userid)
            if userid:
                Save(userid)
                QtWidgets.QMessageBox.information(MainWindow, "提示信息", "打印成功", QtWidgets.QMessageBox.Ok)
            else:
                QtWidgets.QMessageBox.information(MainWindow, "提示信息", "工号不存在", QtWidgets.QMessageBox.Ok)
            # wb = xlwt.Workbook()
            # ws = wb.add_sheet('A Test Sheet')
            # ws.write(0, 0, "工号")
            # ws.write(0, 1, "姓名")
            # ws.write(0, 2, "签到时间")
            # ws.write(0, 3, "是否早退")
            # for i, id in enumerate(username):
            #     ws.write(i + 1, 0, str(id[0]))
            #     ws.write(i + 1, 1, id[1])
            #     ws.write(i + 1, 2, id[2])
            #     ws.write(i + 1, 3, id[3])
            #
            # wb.save(r'C:\Users\lenovo\Desktop\下班考勤.xls')