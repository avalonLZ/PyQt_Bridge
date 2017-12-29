# -*- coding: utf-8 -*-

from dialog_caculate import *
from PyQt4 import QtCore, QtGui
import sys

# #设置当前系统的解码格式，即用若使用了unicode()则是用gb2312去进行解码
reload(sys)
sys.setdefaultencoding('gbk')

class Dialog_caculate(QtGui.QDialog):

    def __init__(self, parent = None):
        QtGui.QDialog.__init__(self, parent)
        self.__ui = Ui_Dialog()
        self.__ui.setupUi(self)

        self.__tool_init()
        self.__solt_init()

    def __tool_init(self):
        pass

    def __solt_init(self):
        self.connect(self.__ui.caculate, QtCore.SIGNAL("clicked()"), self.__click_caculate)
        self.connect(self.__ui.caculate_i2h, QtCore.SIGNAL("clicked()"), self.__click_caculate_i2h)

    def __click_caculate(self):
        self.__str_slat = str(self.__ui.slat.text())
        self.__str_slon = str(self.__ui.slon.text())
        #保留str中的所有数字
        self.__ui.nlat.setText(hex(int(filter(str.isdigit, self.__str_slat)))[2:].zfill(8))
        self.__ui.nlon.setText(hex(int(filter(str.isdigit, self.__str_slon)))[2:].zfill(8))

    def __click_caculate_i2h(self):
        self.__str_int = str(self.__ui.intnum.text())
        self.__ui.hexnum.setText(hex(int(self.__str_int))[2:])