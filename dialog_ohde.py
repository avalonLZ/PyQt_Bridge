# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ohde.ui'
#
# Created: Tue Dec 26 22:07:25 2017
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
        Dialog.resize(558, 356)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/img/image2.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Dialog.setWindowIcon(icon)
        self.label_4 = QtGui.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(10, 220, 54, 12))
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.line_4 = QtGui.QFrame(Dialog)
        self.line_4.setGeometry(QtCore.QRect(200, 190, 20, 271))
        self.line_4.setFrameShape(QtGui.QFrame.VLine)
        self.line_4.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_4.setObjectName(_fromUtf8("line_4"))
        self.ohde_comboBox = QtGui.QComboBox(Dialog)
        self.ohde_comboBox.setGeometry(QtCore.QRect(110, 240, 69, 22))
        self.ohde_comboBox.setObjectName(_fromUtf8("ohde_comboBox"))
        self.ohde_comboBox.addItem(_fromUtf8(""))
        self.ohde_comboBox.setItemText(0, _fromUtf8(""))
        self.ohde_comboBox.addItem(_fromUtf8(""))
        self.ohde_comboBox.addItem(_fromUtf8(""))
        self.ohde_comboBox.addItem(_fromUtf8(""))
        self.ohde_zbctid = QtGui.QLineEdit(Dialog)
        self.ohde_zbctid.setGeometry(QtCore.QRect(340, 270, 71, 20))
        self.ohde_zbctid.setObjectName(_fromUtf8("ohde_zbctid"))
        self.ohde_serial = QtGui.QComboBox(Dialog)
        self.ohde_serial.setGeometry(QtCore.QRect(10, 240, 69, 21))
        self.ohde_serial.setObjectName(_fromUtf8("ohde_serial"))
        self.label_5 = QtGui.QLabel(Dialog)
        self.label_5.setGeometry(QtCore.QRect(110, 220, 54, 12))
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.ohde_open = QtGui.QPushButton(Dialog)
        self.ohde_open.setGeometry(QtCore.QRect(10, 280, 71, 21))
        self.ohde_open.setObjectName(_fromUtf8("ohde_open"))
        self.ohde_zbconfirm = QtGui.QPushButton(Dialog)
        self.ohde_zbconfirm.setGeometry(QtCore.QRect(220, 320, 75, 21))
        self.ohde_zbconfirm.setObjectName(_fromUtf8("ohde_zbconfirm"))
        self.ohde_clean = QtGui.QPushButton(Dialog)
        self.ohde_clean.setGeometry(QtCore.QRect(10, 190, 75, 21))
        self.ohde_clean.setObjectName(_fromUtf8("ohde_clean"))
        self.label_15 = QtGui.QLabel(Dialog)
        self.label_15.setGeometry(QtCore.QRect(220, 230, 121, 20))
        self.label_15.setObjectName(_fromUtf8("label_15"))
        self.label_16 = QtGui.QLabel(Dialog)
        self.label_16.setGeometry(QtCore.QRect(340, 230, 91, 20))
        self.label_16.setObjectName(_fromUtf8("label_16"))
        self.ohde_start = QtGui.QPushButton(Dialog)
        self.ohde_start.setGeometry(QtCore.QRect(10, 320, 81, 21))
        self.ohde_start.setObjectName(_fromUtf8("ohde_start"))
        self.ohde_close = QtGui.QPushButton(Dialog)
        self.ohde_close.setGeometry(QtCore.QRect(110, 280, 71, 21))
        self.ohde_close.setObjectName(_fromUtf8("ohde_close"))
        self.label_14 = QtGui.QLabel(Dialog)
        self.label_14.setGeometry(QtCore.QRect(220, 190, 71, 20))
        self.label_14.setObjectName(_fromUtf8("label_14"))
        self.ohde_end = QtGui.QPushButton(Dialog)
        self.ohde_end.setGeometry(QtCore.QRect(110, 320, 81, 21))
        self.ohde_end.setObjectName(_fromUtf8("ohde_end"))
        self.ohde_zbinfo = QtGui.QPushButton(Dialog)
        self.ohde_zbinfo.setGeometry(QtCore.QRect(340, 320, 75, 21))
        self.ohde_zbinfo.setObjectName(_fromUtf8("ohde_zbinfo"))
        self.ohde_display = QtGui.QTextEdit(Dialog)
        self.ohde_display.setGeometry(QtCore.QRect(10, 0, 541, 181))
        self.ohde_display.setMouseTracking(False)
        self.ohde_display.setAcceptDrops(True)
        self.ohde_display.setReadOnly(True)
        self.ohde_display.setObjectName(_fromUtf8("ohde_display"))
        self.ohde_zbcmid = QtGui.QLineEdit(Dialog)
        self.ohde_zbcmid.setGeometry(QtCore.QRect(220, 270, 71, 20))
        self.ohde_zbcmid.setInputMask(_fromUtf8(""))
        self.ohde_zbcmid.setObjectName(_fromUtf8("ohde_zbcmid"))
        self.line_5 = QtGui.QFrame(Dialog)
        self.line_5.setGeometry(QtCore.QRect(420, 190, 20, 271))
        self.line_5.setFrameShape(QtGui.QFrame.VLine)
        self.line_5.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_5.setObjectName(_fromUtf8("line_5"))
        self.ohde_brname = QtGui.QLineEdit(Dialog)
        self.ohde_brname.setGeometry(QtCore.QRect(440, 250, 111, 20))
        self.ohde_brname.setInputMask(_fromUtf8(""))
        self.ohde_brname.setObjectName(_fromUtf8("ohde_brname"))
        self.label_17 = QtGui.QLabel(Dialog)
        self.label_17.setGeometry(QtCore.QRect(480, 230, 31, 20))
        self.label_17.setObjectName(_fromUtf8("label_17"))
        self.ohde_confirm = QtGui.QPushButton(Dialog)
        self.ohde_confirm.setGeometry(QtCore.QRect(460, 280, 75, 21))
        self.ohde_confirm.setObjectName(_fromUtf8("ohde_confirm"))
        self.label_18 = QtGui.QLabel(Dialog)
        self.label_18.setGeometry(QtCore.QRect(220, 250, 91, 20))
        self.label_18.setObjectName(_fromUtf8("label_18"))
        self.label_19 = QtGui.QLabel(Dialog)
        self.label_19.setGeometry(QtCore.QRect(340, 250, 91, 20))
        self.label_19.setObjectName(_fromUtf8("label_19"))
        self.ohde_info = QtGui.QPushButton(Dialog)
        self.ohde_info.setGeometry(QtCore.QRect(460, 320, 75, 21))
        self.ohde_info.setObjectName(_fromUtf8("ohde_info"))

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "超高节点配置", None))
        self.label_4.setText(_translate("Dialog", "串口", None))
        self.ohde_comboBox.setItemText(1, _translate("Dialog", "9600", None))
        self.ohde_comboBox.setItemText(2, _translate("Dialog", "38400", None))
        self.ohde_comboBox.setItemText(3, _translate("Dialog", "115200", None))
        self.ohde_zbctid.setText(_translate("Dialog", "8001", None))
        self.label_5.setText(_translate("Dialog", "波特率", None))
        self.ohde_open.setText(_translate("Dialog", "打开串口", None))
        self.ohde_zbconfirm.setText(_translate("Dialog", "确认配置", None))
        self.ohde_clean.setText(_translate("Dialog", "清屏", None))
        self.label_15.setText(_translate("Dialog", "ZigBee本机地址", None))
        self.label_16.setText(_translate("Dialog", "ZigBee对方地址", None))
        self.ohde_start.setText(_translate("Dialog", "开启配置模式", None))
        self.ohde_close.setText(_translate("Dialog", "关闭串口", None))
        self.label_14.setText(_translate("Dialog", "ZigBee配置:", None))
        self.ohde_end.setText(_translate("Dialog", "关闭配置模式", None))
        self.ohde_zbinfo.setText(_translate("Dialog", "ZigBee信息", None))
        self.ohde_zbcmid.setText(_translate("Dialog", "8002", None))
        self.ohde_brname.setText(_translate("Dialog", "三洪奇", None))
        self.label_17.setText(_translate("Dialog", "桥名", None))
        self.ohde_confirm.setText(_translate("Dialog", "确认配置", None))
        self.label_18.setText(_translate("Dialog", "Hex,max=ffff", None))
        self.label_19.setText(_translate("Dialog", "Hex,max=ffff", None))
        self.ohde_info.setText(_translate("Dialog", "节点配置", None))

import winico_rc
