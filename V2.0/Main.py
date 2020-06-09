import sys
from PyQt5.QtWidgets import QApplication, QMainWindow

from QTmain import Ui_MainWindow

def MainWindow():
    app = QApplication(sys.argv)    # 新建一个QT应用,sys.argv参数是一个列表，从命令行输入参数。
    myWin = QMainWindow()           # 新建一个QT窗口
    ui = Ui_MainWindow()            # 创建生成的UI主窗口对象
    ui.setupUi(myWin)               # 设置在主窗口上显示UI控件
    myWin.show()                    # 显示窗口
    app.exec_()          # 退出应用
    myWin.close()



if __name__ == "__main__":
    MainWindow()