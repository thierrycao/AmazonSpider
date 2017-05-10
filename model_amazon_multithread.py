from PyQt5 import QtWidgets

from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5 import QtWidgets, QtCore


import time

class myThread(QThread):
    _trigger = pyqtSignal()


    def __init__(self):
        super(myThread,self).__init__()

    def run(self):     
        print("myThread is run!")
        self._trigger.emit()
        print("myThread is end!")

class deamonThread(QThread):
    _trigger = pyqtSignal(str)
    _trigger_progress = pyqtSignal(dict)


    def __init__(self,mQueue):
        super(deamonThread,self).__init__()
        self.mQueue = mQueue

    def run(self):     
        print("deamonThread is run!")
        while True:
            try:
                msg = self.mQueue.get(False)
                msg_str = str(msg)
                if isinstance(msg,dict):
                    self._trigger_progress.emit(msg)
                else:
                    self._trigger.emit(msg_str)
            except:
                time.sleep(1)
                print("No data")
                pass
            """
        	try:
        		msg = self.mQueue.get(False)
                msg_str = str(msg)



                self._trigger.emit(msg_str)
                #self._trigger.emit(msg)
                #if isinstance(msg, dict):
                #    self._trigger_progress.emit(msg)
                #else:
                #self._trigger.emit(str(msg))
            except:
                time.sleep(1)
                print('No data')
                pass
            """
        print("deamonThread is end!")
    	

class spiderThread(QThread):
    _trigger = pyqtSignal()
    

    def __init__(self, key_class):
        super(spiderThread,self).__init__()
        self.key_class = key_class
    def run(self):     
        print("spiderThread is run!")
        #self._trigger.emit()
        self.key_class.start()
        print("spiderThread is end!")


