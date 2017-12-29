# -*- coding: utf-8 -*-

import time
import serial
import serial.tools.list_ports
from dialog_ohtl import *
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

class Dialog_ohtl(QtGui.QDialog):
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
        self.connect(self.__ui.ohtl_open, QtCore.SIGNAL("clicked()"), self.__click_open)
        self.connect(self.__ui.ohtl_close, QtCore.SIGNAL("clicked()"), self.__click_close)
        self.connect(self.__ui.ohtl_clean, QtCore.SIGNAL("clicked()"), self.__click_clean)
        self.connect(self.__ui.ohtl_start, QtCore.SIGNAL("clicked()"), self.__click_start)
        self.connect(self.__ui.ohtl_end, QtCore.SIGNAL("clicked()"), self.__click_end)

        self.connect(self.__ui.ohtl_zbconfirm, QtCore.SIGNAL("clicked()"), self.__click_zbconfirm)
        self.connect(self.__ui.ohtl_zbinfo, QtCore.SIGNAL("clicked()"), self.__click_zbinfo)

        #################################################################################
        self.connect(self.__ui.ohtl_slinked, QtCore.SIGNAL("clicked()"), self.__click_slinked)
        self.connect(self.__ui.ohtl_unslinked, QtCore.SIGNAL("clicked()"), self.__click_unslinked)
        self.connect(self.__ui.ohtl_stime, QtCore.SIGNAL("clicked()"), self.__click_stime)
        self.connect(self.__ui.ohtl_unstime, QtCore.SIGNAL("clicked()"), self.__click_unstime)
        self.connect(self.__ui.ohtl_info, QtCore.SIGNAL("clicked()"), self.__click_info)
        self.connect(self.__ui.ohtl_schipdir, QtCore.SIGNAL("clicked()"), self.__click_schipdir)
        self.connect(self.__ui.ohtl_unschipdir, QtCore.SIGNAL("clicked()"), self.__click_unschipdir)
        self.connect(self.__ui.ohtl_checkvhf, QtCore.SIGNAL("clicked()"), self.__click_checkvhf)
        self.connect(self.__ui.ohtl_openvhf, QtCore.SIGNAL("clicked()"), self.__click_openvhf)
        self.connect(self.__ui.ohtl_closevhf, QtCore.SIGNAL("clicked()"), self.__click_closevhf)
        self.connect(self.__ui.ohtl_chechzb, QtCore.SIGNAL("clicked()"), self.__click_chechzb)
        self.connect(self.__ui.ohtl_openzb, QtCore.SIGNAL("clicked()"), self.__click_openzb)
        self.connect(self.__ui.ohtl_closezb, QtCore.SIGNAL("clicked()"), self.__click_closezb)
        self.connect(self.__ui.ohtl_confirm, QtCore.SIGNAL("clicked()"), self.__click_confirm)
        #################################################################################

    def __scancom(self, com_list):
        self.__ui.ohtl_serial.clear()
        self.__ui.ohtl_serial.addItems(com_list)

    def __serial_config(self, serial = None, port = None, baudrate = None, bytesize = 8, stopbits = 1, parity = 'N'):
        serial.port = port
        serial.baudrate = baudrate
        serial.bytesize = bytesize
        serial.stopbits = stopbits
        serial.parity = parity

    def __click_open(self):

        if self.__ui.ohtl_comboBox.currentText() == '' or str(self.__ui.ohtl_serial.currentText()) == '':
            QtGui.QMessageBox.warning(self, u"错误" ,u"串口或波特率错误，请检查")
            return
        self.__serial_config(serial = self.ser, port = str(self.__ui.ohtl_serial.currentText()),
                             baudrate=int(self.__ui.ohtl_comboBox.currentText()))
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

            self.__ui_disable(self.__ui.ohtl_open)

        except:
            QtGui.QMessageBox.warning(self, u"错误", u"串口被占用或异常，无法打开")

    def __click_clean(self):
        self.__ui.ohtl_display.clear()

    def __click_close(self):
        self.__ui_enable(self.__ui.ohtl_open)
        #结束全部线程
        self.sin2readdatastop.emit()
        self.sin2writedatastop.emit()
        self.ser.close()

    def __click_start(self):
        self.sin2writedata.emit("shell on\r\n")

    def __click_end(self):
        self.sin2writedata.emit("shell off\r\n")

    def __click_zbconfirm(self):
        self.__temzbparam = self.__ui.ohtl_zbcmid.text()
        self.__temzbparam = "wltconfig cmid " + self.__temzbparam + "\r\n"
        self.sin2writedata.emit(self.__temzbparam)

        self.__temzbparam = self.__ui.ohtl_zbctid.text()
        self.__temzbparam = "wltconfig ctid " + self.__temzbparam + "\r\n"
        self.sin2writedata.emit(self.__temzbparam)

        self.sin2writedata.emit("wltconfig reboot\r\n")

    def __click_zbinfo(self):
        self.sin2writedata.emit("wltconfig info\r\n")

        #################################################################################
    def __click_slinked(self):
        self.sin2writedata.emit("debug linked 1\r\n")

    def __click_unslinked(self):
        self.sin2writedata.emit("debug linked 0\r\n")

    def __click_stime(self):
        self.sin2writedata.emit("debug time 1\r\n")

    def __click_unstime(self):
        self.sin2writedata.emit("debug time 0\r\n")

    def __click_info(self):
        self.sin2writedata.emit("terconfig info\r\n")

    def __click_schipdir(self):
        self.sin2writedata.emit("debug ais 1\r\n")

    def __click_unschipdir(self):
        self.sin2writedata.emit("debug ais 0\r\n")

    def __click_checkvhf(self):
        self.sin2writedata.emit("vhfconfig info\r\n")

    def __click_openvhf(self):
        self.sin2writedata.emit("vhfconfig vhfsw 1\r\n")

    def __click_closevhf(self):
        self.sin2writedata.emit("vhfconfig vhfsw 0\r\n")

    def __click_chechzb(self):
        self.sin2writedata.emit("wltconfig swinfo\r\n")

    def __click_openzb(self):
        self.sin2writedata.emit("wltconfig sw 1\r\n")

    def __click_closezb(self):
        self.sin2writedata.emit("wltconfig sw 0\r\n")

    def __click_confirm(self):
        self.__temid = self.__ui.ohtl_id.text()
        self.__temid = "terconfig terid " + self.__temid + "\r\n"
        self.sin2writedata.emit(self.__temid)

        self.__temcdirmin = self.__ui.ohtl_dirmin.text()
        self.__temcdirmin = "terconfig dirmin " + self.__temcdirmin + "\r\n"
        self.sin2writedata.emit(self.__temcdirmin)

        self.__temcdirmax = self.__ui.ohtl_dirmax.text()
        self.__temcdirmax = "terconfig dirmax " + self.__temcdirmax + "\r\n"
        self.sin2writedata.emit(self.__temcdirmax)

        self.__temlat = self.__ui.ohtl_lat.text()
        self.__temlat = "terconfig loclat " + self.__temlat +"\r\n"
        self.sin2writedata.emit(self.__temlat)

        self.__temlon = self.__ui.ohtl_lon.text()
        self.__temlon = "terconfig loclon " + self.__temlon + "\r\n"
        self.sin2writedata.emit(self.__temlon)

        self.sin2writedata.emit("terconfig confirm\r\n")

        #################################################################################

    def return_ui_display(self):
        return self.__ui.ohtl_display

    def __diaplay(self, temstr):
        self.__ui.ohtl_display.append(temstr)

    def closeEvent(self, QCloseEvent):#重写Dialog关闭方法

        if self.ser.isOpen():
            self.__click_close()
        QtGui.QDialog.closeEvent(self, QCloseEvent)
####################################################################################################



