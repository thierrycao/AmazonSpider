# -*- coding:utf-8 -*-

import time
import os
from PyQt5 import QtWidgets, QtCore
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPalette
from PyQt5.QtWidgets import QMessageBox, QInputDialog, QLineEdit, QFileDialog, QColorDialog, QFontDialog

from view_baseUI_v3 import Ui_Form
from model_amazon_stock import amazon_stock
#from amazon_multiprocessing import spiderProcess

from model_amazon_multithread import spiderThread,myThread,deamonThread


import multiprocessing
from multiprocessing import Process


from amazon_egg import myCowpy

class mywindow(QtWidgets.QWidget, Ui_Form):
    _signal = QtCore.pyqtSignal(str)
    def __init__(self):
        super(mywindow,self).__init__()
        self.setupUi(self)
        self.setupSpider()
        self.setupLocalUi()
        self.setupPrint()

    def setupLocalUi(self):


        self.buttonImport.clicked.connect(self.slot_import_xml)
        self.buttonStart.clicked.connect(self.slot_startThread)
        self.buttonCowpy.clicked.connect(self.slot_crowpy_print)

    def slot_import_xml(self):
        self.msg_import_xml()
        self.setupSpider()

    def slot_crowpy_print(self):
        msg = myCowpy().cowpyFactory

        self.msg_cowpy_print(msg)
    	

    def setupSpider(self):
    
        #new Queue to share the source between main process and child process
        self.mQueue = multiprocessing.Queue()

        self.mQueueDeamonThread = deamonThread(self.mQueue)
        self.mQueueDeamonThread._trigger.connect(self.slotPrint)
        self.mQueueDeamonThread._trigger_progress.connect(self.slotFlushProgress)


    def setupPrint(self):
        self.bufferPrint = ''

    def slot_startThread(self):
        self.startTime = time.time()
        self.msg_start()

        #new spider process
        self.mSpiderProcess = Process(target=self.childProcess_startSpider, args=(self.importData, self.mQueue))

        #start spider child process
        print("Main process pid:")
        self.mSpiderProcess.start()
        print("child process is alive?", self.mSpiderProcess.is_alive())

        #main process stat textLine
        self.mQueueDeamonThread.start()



    def childProcess_startSpider(self,data,mQueue):
    	#print("spider start....")

        #child process spider
        spider = amazon_stock()
        spider.waitingReadUserChoose = data
        spider.mQueue = mQueue

        spider._trigger_int.connect(lambda x:print(x))
        spider._trigger_str.connect(lambda x:print(x))
        spider._trigger_list.connect(lambda x:print(x))
        spider._trigger_dict.connect(lambda x:print(x))
        #spider._trigger_progress.connect(self.slotFlushProgress)

        spider.start()


    def slotPrint(self,msg):
    	self.bufferPrint = msg
    	self.msg_print()

    def slotFlushProgress(self,msg):
        index = msg['index']
        length = msg['length']
        num = msg['num']

        self.msg_progress(length,num)
        self.msg_show_remainingTime(self.startTime,length,num)



if __name__ == "__main__":
    import sys


    app = QtWidgets.QApplication(sys.argv)
    myshow = mywindow()
    myshow.show()
    sys.exit(app.exec_())
