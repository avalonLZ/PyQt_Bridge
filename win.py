# -*- coding: utf-8 -*-

import sys
from win_bridge import *
from ohtl import *
from ohde import *
from brtl import *
from brde import *
from caculate import *
from PyQt4 import QtCore, QtGui

class MainWindow(QtGui.QMainWindow):

    def __init__(self, parent = None):
        QtGui.QMainWindow.__init__(self, parent)
        self.__ui = Ui_MainWindow()
        self.__ui.setupUi(self)

        self.__solt_init()

    def __solt_init(self):
        self.connect(self.__ui.cfg_ohtl, QtCore.SIGNAL("triggered()"), self.__click_ohtl)
        self.connect(self.__ui.cfg_ohde, QtCore.SIGNAL("triggered()"), self.__click_ohde)
        self.connect(self.__ui.cfg_brtl, QtCore.SIGNAL("triggered()"), self.__click_brtl)
        self.connect(self.__ui.cfg_brde, QtCore.SIGNAL("triggered()"), self.__click_brde)
        self.connect(self.__ui.web, QtCore.SIGNAL("triggered()"), self.__click_web)
        self.connect(self.__ui.about, QtCore.SIGNAL("triggered()"), self.__click_about)
        self.connect(self.__ui.exit, QtCore.SIGNAL("triggered()"), self.__click_exit)
        self.connect(self.__ui.caculate, QtCore.SIGNAL("triggered()"), self.__click_caculate)

    def __click_ohtl(self):
        self.__ohtlui = Dialog_ohtl()
        self.__ohtlui.setWindowFlags(QtCore.Qt.WindowMinimizeButtonHint)
        self.__ohtlui.setFixedSize(self.__ohtlui.width(), self.__ohtlui.height())
        self.__ohtlui.show()

    def __click_ohde(self):
        self.__ohdeui = Dialog_ohde()
        self.__ohdeui.setWindowFlags(QtCore.Qt.WindowMinimizeButtonHint)
        self.__ohdeui.setFixedSize(self.__ohdeui.width(), self.__ohdeui.height())
        self.__ohdeui.show()

    def __click_brtl(self):
        self.__brtlui = Dialog_brtl()
        self.__brtlui.setWindowFlags(QtCore.Qt.WindowMinimizeButtonHint)
        self.__brtlui.setFixedSize(self.__brtlui.width(), self.__brtlui.height())
        self.__brtlui.show()
        #self.__brtlui.exec_()此方法会造成之后语句阻塞,exec后的Dialog会被置顶

    def __click_brde(self):
        self.__brdeui = Dialog_brde()
        self.__brdeui.setWindowFlags(QtCore.Qt.WindowMinimizeButtonHint)
        self.__brdeui.setFixedSize(self.__brdeui.width(), self.__brdeui.height())
        self.__brdeui.show()

    def __click_web(self):
        QtGui.QMessageBox.about(self, u"经纬度换算", u"<a href='http://www.gpsspg.com/maps.htm'>请单击，打开经纬度换算Web</a>")

    def __click_caculate(self):
        self.__caculateui = Dialog_caculate()
        self.__caculateui.setWindowFlags(QtCore.Qt.WindowMinimizeButtonHint)
        self.__caculateui.setFixedSize(self.__caculateui.width(), self.__caculateui.height())
        self.__caculateui.show()

    def __click_about(self):
        QtGui.QMessageBox.about(self, u"关于", u"桥梁避碰终端配置工具\r\n"
                                             u"       2017.12.26 by:lz")

    def __click_exit(self):
        self.close()


if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    myapp = MainWindow()

    #窗口最大化按键无效
    myapp.setWindowFlags(QtCore.Qt.WindowMinimizeButtonHint)

    #锁定窗口大小
    myapp.setFixedSize(myapp.width(), myapp.height())
    myapp.show()
    app.exec_()