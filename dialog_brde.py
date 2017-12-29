# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'brde.ui'
#
# Created: Tue Dec 26 21:58:11 2017
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

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName(_fromUtf8("Dialog"))
        Dialog.resize(559, 355)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/img/image2.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Dialog.setWindowIcon(icon)
        self.brde_display = QtGui.QTextEdit(Dialog)
        self.brde_display.setGeometry(QtCore.QRect(10, 10, 541, 181))
        self.brde_display.setMouseTracking(False)
        self.brde_display.setAcceptDrops(True)
        self.brde_display.setReadOnly(True)
        self.brde_display.setObjectName(_fromUtf8("brde_display"))
        self.brde_serial = QtGui.QComboBox(Dialog)
        self.brde_serial.setGeometry(QtCore.QRect(10, 250, 69, 21))
        self.brde_serial.setObjectName(_fromUtf8("brde_serial"))
        self.brde_open = QtGui.QPushButton(Dialog)
        self.brde_open.setGeometry(QtCore.QRect(10, 290, 71, 21))
        self.brde_open.setObjectName(_fromUtf8("brde_open"))
        self.brde_end = QtGui.QPushButton(Dialog)
        self.brde_end.setGeometry(QtCore.QRect(110, 330, 81, 21))
        self.brde_end.setObjectName(_fromUtf8("brde_end"))
        self.brde_close = QtGui.QPushButton(Dialog)
        self.brde_close.setGeometry(QtCore.QRect(110, 290, 71, 21))
        self.brde_close.setObjectName(_fromUtf8("brde_close"))
        self.brde_clean = QtGui.QPushButton(Dialog)
        self.brde_clean.setGeometry(QtCore.QRect(10, 200, 75, 21))
        self.brde_clean.setObjectName(_fromUtf8("brde_clean"))
        self.label_5 = QtGui.QLabel(Dialog)
        self.label_5.setGeometry(QtCore.QRect(110, 230, 54, 12))
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.label_4 = QtGui.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(10, 230, 54, 12))
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.brde_start = QtGui.QPushButton(Dialog)
        self.brde_start.setGeometry(QtCore.QRect(10, 330, 81, 21))
        self.brde_start.setObjectName(_fromUtf8("brde_start"))
        self.brde_comboBox = QtGui.QComboBox(Dialog)
        self.brde_comboBox.setGeometry(QtCore.QRect(110, 250, 69, 22))
        self.brde_comboBox.setObjectName(_fromUtf8("brde_comboBox"))
        self.brde_comboBox.addItem(_fromUtf8(""))
        self.brde_comboBox.setItemText(0, _fromUtf8(""))
        self.brde_comboBox.addItem(_fromUtf8(""))
        self.brde_comboBox.addItem(_fromUtf8(""))
        self.brde_comboBox.addItem(_fromUtf8(""))
        self.brde_zbconfirm = QtGui.QPushButton(Dialog)
        self.brde_zbconfirm.setGeometry(QtCore.QRect(280, 300, 75, 21))
        self.brde_zbconfirm.setObjectName(_fromUtf8("brde_zbconfirm"))
        self.brde_zbinfo = QtGui.QPushButton(Dialog)
        self.brde_zbinfo.setGeometry(QtCore.QRect(410, 300, 75, 21))
        self.brde_zbinfo.setObjectName(_fromUtf8("brde_zbinfo"))
        self.label_15 = QtGui.QLabel(Dialog)
        self.label_15.setGeometry(QtCore.QRect(280, 220, 121, 20))
        self.label_15.setObjectName(_fromUtf8("label_15"))
        self.brde_zbcmid = QtGui.QLineEdit(Dialog)
        self.brde_zbcmid.setGeometry(QtCore.QRect(280, 260, 71, 20))
        self.brde_zbcmid.setInputMask(_fromUtf8(""))
        self.brde_zbcmid.setObjectName(_fromUtf8("brde_zbcmid"))
        self.brde_zbctid = QtGui.QLineEdit(Dialog)
        self.brde_zbctid.setGeometry(QtCore.QRect(410, 260, 71, 20))
        self.brde_zbctid.setObjectName(_fromUtf8("brde_zbctid"))
        self.label_14 = QtGui.QLabel(Dialog)
        self.label_14.setGeometry(QtCore.QRect(220, 200, 71, 20))
        self.label_14.setObjectName(_fromUtf8("label_14"))
        self.label_16 = QtGui.QLabel(Dialog)
        self.label_16.setGeometry(QtCore.QRect(410, 220, 91, 20))
        self.label_16.setObjectName(_fromUtf8("label_16"))
        self.line_4 = QtGui.QFrame(Dialog)
        self.line_4.setGeometry(QtCore.QRect(200, 200, 20, 271))
        self.line_4.setFrameShape(QtGui.QFrame.VLine)
        self.line_4.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_4.setObjectName(_fromUtf8("line_4"))
        self.label_17 = QtGui.QLabel(Dialog)
        self.label_17.setGeometry(QtCore.QRect(280, 240, 91, 20))
        self.label_17.setObjectName(_fromUtf8("label_17"))
        self.label_18 = QtGui.QLabel(Dialog)
        self.label_18.setGeometry(QtCore.QRect(410, 240, 91, 20))
        self.label_18.setObjectName(_fromUtf8("label_18"))

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "桥墩节点配置", None))
        self.brde_open.setText(_translate("Dialog", "打开串口", None))
        self.brde_end.setText(_translate("Dialog", "关闭配置模式", None))
        self.brde_close.setText(_translate("Dialog", "关闭串口", None))
        self.brde_clean.setText(_translate("Dialog", "清屏", None))
        self.label_5.setText(_translate("Dialog", "波特率", None))
        self.label_4.setText(_translate("Dialog", "串口", None))
        self.brde_start.setText(_translate("Dialog", "开启配置模式", None))
        self.brde_comboBox.setItemText(1, _translate("Dialog", "9600", None))
        self.brde_comboBox.setItemText(2, _translate("Dialog", "38400", None))
        self.brde_comboBox.setItemText(3, _translate("Dialog", "115200", None))
        self.brde_zbconfirm.setText(_translate("Dialog", "确认配置", None))
        self.brde_zbinfo.setText(_translate("Dialog", "ZigBee信息", None))
        self.label_15.setText(_translate("Dialog", "ZigBee本机地址", None))
        self.brde_zbcmid.setText(_translate("Dialog", "8004", None))
        self.brde_zbctid.setText(_translate("Dialog", "8003", None))
        self.label_14.setText(_translate("Dialog", "ZigBee配置:", None))
        self.label_16.setText(_translate("Dialog", "ZigBee对方地址", None))
        self.label_17.setText(_translate("Dialog", "Hex,max=ffff", None))
        self.label_18.setText(_translate("Dialog", "Hex,max=ffff", None))

import winico_rc
