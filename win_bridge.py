# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'bridge.ui'
#
# Created: Tue Dec 26 23:07:20 2017
#      by: PyQt4 UI code generator 4.10.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(326, 294)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/img/image2.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet(_fromUtf8("selection-background-color: rgb(178, 214, 247);\n"
"background-image: url(:/img/image3.png);\n"
"color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0, stop:0 rgba(0, 0, 0, 255), stop:0.05 rgba(14, 8, 73, 255), stop:0.36 rgba(28, 17, 145, 255), stop:0.6 rgba(126, 14, 81, 255), stop:0.75 rgba(234, 11, 11, 255), stop:0.79 rgba(244, 70, 5, 255), stop:0.86 rgba(255, 136, 0, 255), stop:0.935 rgba(239, 236, 55, 255));"))
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(60, 10, 211, 31))
        self.label.setStyleSheet(_fromUtf8("font: 75 14pt \"华文新魏\";\n"
"color: rgb(135, 135, 203);"))
        self.label.setObjectName(_fromUtf8("label"))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 326, 23))
        self.menubar.setDefaultUp(False)
        self.menubar.setNativeMenuBar(True)
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.config = QtGui.QMenu(self.menubar)
        self.config.setObjectName(_fromUtf8("config"))
        self.other = QtGui.QMenu(self.menubar)
        self.other.setObjectName(_fromUtf8("other"))
        MainWindow.setMenuBar(self.menubar)
        self.action = QtGui.QAction(MainWindow)
        self.action.setObjectName(_fromUtf8("action"))
        self.About = QtGui.QAction(MainWindow)
        self.About.setObjectName(_fromUtf8("About"))
        self.cfg_ohtl = QtGui.QAction(MainWindow)
        self.cfg_ohtl.setCheckable(True)
        self.cfg_ohtl.setIcon(icon)
        self.cfg_ohtl.setObjectName(_fromUtf8("cfg_ohtl"))
        self.cfg_brtl = QtGui.QAction(MainWindow)
        self.cfg_brtl.setIcon(icon)
        self.cfg_brtl.setObjectName(_fromUtf8("cfg_brtl"))
        self.cfg_ohde = QtGui.QAction(MainWindow)
        self.cfg_ohde.setIcon(icon)
        self.cfg_ohde.setObjectName(_fromUtf8("cfg_ohde"))
        self.cfg_brde = QtGui.QAction(MainWindow)
        self.cfg_brde.setIcon(icon)
        self.cfg_brde.setObjectName(_fromUtf8("cfg_brde"))
        self.web = QtGui.QAction(MainWindow)
        self.web.setIcon(icon)
        self.web.setObjectName(_fromUtf8("web"))
        self.exit = QtGui.QAction(MainWindow)
        self.exit.setIcon(icon)
        self.exit.setObjectName(_fromUtf8("exit"))
        self.caculate = QtGui.QAction(MainWindow)
        self.caculate.setIcon(icon)
        self.caculate.setObjectName(_fromUtf8("caculate"))
        self.about = QtGui.QAction(MainWindow)
        self.about.setIcon(icon)
        self.about.setObjectName(_fromUtf8("about"))
        self.config.addAction(self.cfg_ohtl)
        self.config.addAction(self.cfg_brtl)
        self.config.addAction(self.cfg_brde)
        self.config.addAction(self.cfg_ohde)
        self.other.addAction(self.web)
        self.other.addAction(self.caculate)
        self.other.addSeparator()
        self.other.addAction(self.about)
        self.other.addAction(self.exit)
        self.menubar.addAction(self.other.menuAction())
        self.menubar.addAction(self.config.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "桥梁避碰终端配置工具包", None))
        self.label.setText(_translate("MainWindow", "桥梁避碰终端配置工具包", None))
        self.config.setTitle(_translate("MainWindow", "配置", None))
        self.other.setTitle(_translate("MainWindow", "菜单", None))
        self.action.setText(_translate("MainWindow", "配置", None))
        self.About.setText(_translate("MainWindow", "About", None))
        self.cfg_ohtl.setText(_translate("MainWindow", "超高主机配置", None))
        self.cfg_brtl.setText(_translate("MainWindow", "桥墩主机配置", None))
        self.cfg_ohde.setText(_translate("MainWindow", "超高节点配置", None))
        self.cfg_brde.setText(_translate("MainWindow", "桥墩节点配置", None))
        self.web.setText(_translate("MainWindow", "经纬度查询", None))
        self.exit.setText(_translate("MainWindow", "退出", None))
        self.caculate.setText(_translate("MainWindow", "经纬度进制转换", None))
        self.about.setText(_translate("MainWindow", "关于", None))

import winico_rc
