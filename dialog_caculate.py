# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'caculate.ui'
#
# Created: Wed Dec 27 16:04:13 2017
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
        Dialog.resize(280, 135)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/img/image2.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Dialog.setWindowIcon(icon)
        Dialog.setStyleSheet(_fromUtf8(""))
        self.slat = QtGui.QLineEdit(Dialog)
        self.slat.setGeometry(QtCore.QRect(10, 30, 71, 20))
        self.slat.setObjectName(_fromUtf8("slat"))
        self.label_12 = QtGui.QLabel(Dialog)
        self.label_12.setGeometry(QtCore.QRect(10, 10, 101, 16))
        self.label_12.setObjectName(_fromUtf8("label_12"))
        self.label_13 = QtGui.QLabel(Dialog)
        self.label_13.setGeometry(QtCore.QRect(100, 10, 101, 16))
        self.label_13.setObjectName(_fromUtf8("label_13"))
        self.slon = QtGui.QLineEdit(Dialog)
        self.slon.setGeometry(QtCore.QRect(100, 30, 81, 20))
        self.slon.setObjectName(_fromUtf8("slon"))
        self.label_14 = QtGui.QLabel(Dialog)
        self.label_14.setGeometry(QtCore.QRect(10, 60, 61, 16))
        self.label_14.setObjectName(_fromUtf8("label_14"))
        self.label_15 = QtGui.QLabel(Dialog)
        self.label_15.setGeometry(QtCore.QRect(100, 60, 61, 16))
        self.label_15.setObjectName(_fromUtf8("label_15"))
        self.nlat = QtGui.QLineEdit(Dialog)
        self.nlat.setGeometry(QtCore.QRect(10, 80, 71, 20))
        self.nlat.setObjectName(_fromUtf8("nlat"))
        self.nlon = QtGui.QLineEdit(Dialog)
        self.nlon.setGeometry(QtCore.QRect(100, 80, 81, 20))
        self.nlon.setObjectName(_fromUtf8("nlon"))
        self.caculate = QtGui.QPushButton(Dialog)
        self.caculate.setGeometry(QtCore.QRect(60, 110, 61, 23))
        self.caculate.setObjectName(_fromUtf8("caculate"))
        self.label_16 = QtGui.QLabel(Dialog)
        self.label_16.setGeometry(QtCore.QRect(210, 10, 51, 20))
        self.label_16.setObjectName(_fromUtf8("label_16"))
        self.intnum = QtGui.QLineEdit(Dialog)
        self.intnum.setGeometry(QtCore.QRect(200, 30, 71, 20))
        self.intnum.setObjectName(_fromUtf8("intnum"))
        self.label_17 = QtGui.QLabel(Dialog)
        self.label_17.setGeometry(QtCore.QRect(220, 60, 21, 16))
        self.label_17.setObjectName(_fromUtf8("label_17"))
        self.hexnum = QtGui.QLineEdit(Dialog)
        self.hexnum.setGeometry(QtCore.QRect(200, 80, 71, 20))
        self.hexnum.setObjectName(_fromUtf8("hexnum"))
        self.caculate_i2h = QtGui.QPushButton(Dialog)
        self.caculate_i2h.setGeometry(QtCore.QRect(200, 110, 61, 23))
        self.caculate_i2h.setObjectName(_fromUtf8("caculate_i2h"))
        self.line = QtGui.QFrame(Dialog)
        self.line.setGeometry(QtCore.QRect(180, 10, 20, 121))
        self.line.setFrameShape(QtGui.QFrame.VLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName(_fromUtf8("line"))

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "经纬度进制转换", None))
        self.slat.setText(_translate("Dialog", "00.0000", None))
        self.label_12.setText(_translate("Dialog", "纬度（.mmmm）", None))
        self.label_13.setText(_translate("Dialog", "经度（.mmmm）", None))
        self.slon.setText(_translate("Dialog", "000.0000", None))
        self.label_14.setText(_translate("Dialog", "纬度（Hex）", None))
        self.label_15.setText(_translate("Dialog", "经度（Hex）", None))
        self.nlat.setText(_translate("Dialog", "00000000", None))
        self.nlon.setText(_translate("Dialog", "00000000", None))
        self.caculate.setText(_translate("Dialog", "转换", None))
        self.label_16.setText(_translate("Dialog", "任意Int", None))
        self.intnum.setText(_translate("Dialog", "0", None))
        self.label_17.setText(_translate("Dialog", "Hex", None))
        self.hexnum.setText(_translate("Dialog", "0", None))
        self.caculate_i2h.setText(_translate("Dialog", "转换", None))

import winico_rc
