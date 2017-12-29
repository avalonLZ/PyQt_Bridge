# -*- coding: utf-8 -*-

import time
import serial
import serial.tools.list_ports
from dialog_ohde import *
from PyQt4 import QtCore, QtGui
import sys

# #设置当前系统的解码格式，即用若使用了unicode()则是用gb2312去进行解码
reload(sys)
sys.setdefaultencoding('gbk')


#串口扫描，返回存在的COM口
def serial_ports(open_com = None):
    ports = []
    port_list = list(serial.tools.list_ports.comports())
    for i in port_list:
        ports.append(str(i.device))
    return ports

old_port = []#保证不一致刷新com口数量

class Thread_ScanCom(QtCore.QThread):
    #信号初始化时可以带类型参数表示，使用信号并传递一个指定类型的参数
    sinOut = QtCore.pyqtSignal(list)

    def __init__(self, parent=None):
        super(Thread_ScanCom, self).__init__(parent)
        self.new_port = []

    def run(self):
        while 1:
             old_port = self.new_port
             self.new_port = serial_ports()

             if self.new_port != old_port:
                self.sinOut.emit(self.new_port)#发送信号到主线程

    #读写最好放不同线程，串口读线程
class Thread_SerialReadData(QtCore.QThread):
    sinOut = QtCore.pyqtSignal(str)

    def __init__(self, parent=None, obj = None):
        super(Thread_SerialReadData, self).__init__(parent)
        self.serial = obj
        self.nostop = 1

    def run(self):
        while self.nostop:#while结束线程也就退出了
            #Read:
            #print int(self.serial.in_waiting)#此处打印出0（被立马取出）
            self.data = self.serial.readline()#此处会阻塞
            #print int(self.serial.in_waiting)
            try:
                self.sinOut.emit(unicode(str(self.data)))#发送信号到主线程#self.display.append(str(self.data))
            except:
                self.sinOut.emit(str(self.data))#防止收到hex进制数据

    def readdata_stop(self):#被外信号绑定的函数不能写为私有函数
        self.nostop = 0


    #串口写线程
class Thread_SerialWriteData(QtCore.QThread):

    def __init__(self, parent=None, obj = None):
        super(Thread_SerialWriteData, self).__init__(parent)
        self.serial = obj
        self.nostop = 1

    def run(self):
        while self.nostop:
            pass

    # Write:
    def write_data(self, temcmd):
            self.serial.write(str(temcmd))
            time.sleep(0.1)#防止写入太快

    def writedata_stop(self):#被外信号绑定的函数不能写为私有函数
        self.nostop = 0

class Dialog_ohde(QtGui.QDialog):
    sin2readdatastop = QtCore.pyqtSignal()  # 创建一个信号,信号必须定义在类中，定义在方法中将无法正确链接到
    sin2writedatastop = QtCore.pyqtSignal()
    sin2writedata = QtCore.pyqtSignal(str)
    ser = serial.Serial()

    def __init__(self, parent = None):
        QtGui.QDialog.__init__(self, parent)
        self.__ui = Ui_Dialog()
        self.__ui.setupUi(self)

        self.__tool_init()
        self.__solt_init()

        # 创建线程扫描com变化
        self.thread_scancom = Thread_ScanCom()
        self.thread_scancom.sinOut.connect(self.__scancom)
        self.thread_scancom.start()

    def __ui_disable(self, obj = None):
        obj.setDisabled(True)

    def __ui_enable(self, obj = None):
        obj.setDisabled(False)

    def __tool_init(self):
        pass

    def __solt_init(self):
        self.connect(self.__ui.ohde_open, QtCore.SIGNAL("clicked()"), self.__click_open)
        self.connect(self.__ui.ohde_close, QtCore.SIGNAL("clicked()"), self.__click_close)
        self.connect(self.__ui.ohde_clean, QtCore.SIGNAL("clicked()"), self.__click_clean)
        self.connect(self.__ui.ohde_start, QtCore.SIGNAL("clicked()"), self.__click_start)
        self.connect(self.__ui.ohde_end, QtCore.SIGNAL("clicked()"), self.__click_end)

        self.connect(self.__ui.ohde_zbconfirm, QtCore.SIGNAL("clicked()"), self.__click_zbconfirm)
        self.connect(self.__ui.ohde_zbinfo, QtCore.SIGNAL("clicked()"), self.__click_zbinfo)

        ##############################################
        self.connect(self.__ui.ohde_confirm, QtCore.SIGNAL("clicked()"), self.__click_confirm)
        self.connect(self.__ui.ohde_info, QtCore.SIGNAL("clicked()"), self.__click_info)
        ##############################################

    def __scancom(self, com_list):
        self.__ui.ohde_serial.clear()
        self.__ui.ohde_serial.addItems(com_list)

    def __serial_config(self, serial = None, port = None, baudrate = None, bytesize = 8, stopbits = 1, parity = 'N'):
        serial.port = port
        serial.baudrate = baudrate
        serial.bytesize = bytesize
        serial.stopbits = stopbits
        serial.parity = parity

    def __click_open(self):

        if self.__ui.ohde_comboBox.currentText() == '' or str(self.__ui.ohde_serial.currentText()) == '':
            QtGui.QMessageBox.warning(self, u"错误" ,u"串口或波特率错误，请检查")
            return
        self.__serial_config(serial = self.ser, port = str(self.__ui.ohde_serial.currentText()),
                             baudrate=int(self.__ui.ohde_comboBox.currentText()))
        try:
            self.ser.open()

            #创建读线程
            self.__thread_serialreaddata = Thread_SerialReadData(obj=self.ser)
            self.sin2readdatastop.connect(self.__thread_serialreaddata.readdata_stop)#绑定停止信号
            self.__thread_serialreaddata.sinOut.connect(self.__diaplay)#绑定显示信号
            self.__thread_serialreaddata.start()

            #创建写线程
            self.__thread_serialwritedata = Thread_SerialWriteData(obj=self.ser)
            self.sin2writedatastop.connect(self.__thread_serialwritedata.writedata_stop)  # 绑定停止信号
            self.sin2writedata.connect(self.__thread_serialwritedata.write_data)  # 绑定写入数据信号
            self.__thread_serialwritedata.start()

            self.__ui_disable(self.__ui.ohde_open)

        except:
            QtGui.QMessageBox.warning(self, u"错误", u"串口被占用或异常，无法打开")

    def __click_clean(self):
        self.__ui.ohde_display.clear()

    def __click_close(self):
        self.__ui_enable(self.__ui.ohde_open)
        #结束全部线程
        self.sin2readdatastop.emit()
        self.sin2writedatastop.emit()
        self.ser.close()

    def __click_start(self):
        self.sin2writedata.emit("shell on\r\n")

    def __click_end(self):
        self.sin2writedata.emit("shell off\r\n")

    def __click_zbconfirm(self):
        self.__temzbparam = self.__ui.ohde_zbcmid.text()
        self.__temzbparam = "wltconfig cmid " + self.__temzbparam + "\r\n"
        self.sin2writedata.emit(self.__temzbparam)

        self.__temzbparam = self.__ui.ohde_zbctid.text()
        self.__temzbparam = "wltconfig ctid " + self.__temzbparam + "\r\n"
        self.sin2writedata.emit(self.__temzbparam)

        self.sin2writedata.emit("wltconfig reboot\r\n")

    def __click_zbinfo(self):
        self.sin2writedata.emit("wltconfig info\r\n")

        ##############################################
    def __click_confirm(self):
        self.__brname = self.__ui.ohde_brname.text()
        self.__brname = "terconfig bridge " + self.__brname + "\r\n"
        self.sin2writedata.emit(self.__brname)

    def __click_info(self):
        self.sin2writedata.emit("terconfig info\r\n")
        ##############################################

    def return_ui_display(self):
        return self.__ui.ohde_display

    def __diaplay(self, temstr):
        self.__ui.ohde_display.append(temstr)

    def closeEvent(self, QCloseEvent):#重写Dialog关闭方法

        if self.ser.isOpen():
            self.__click_close()
        QtGui.QDialog.closeEvent(self, QCloseEvent)
####################################################################################################



