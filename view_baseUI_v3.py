# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'H:\soft\python_3.5.3\workspace\factory\transition\project\baseUI_v3.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QFileDialog
from PyQt5.QtWidgets import QMessageBox
import time

class Ui_Form(object):
    def setupUi(self, Form):
        self.setupData()
        Form.setObjectName("Spider")
        Form.resize(697, 623)
        self.buttonQuit = QtWidgets.QPushButton(Form)
        self.buttonQuit.setGeometry(QtCore.QRect(50, 580, 91, 31))
        self.buttonQuit.setStyleSheet("font: 10pt \"Andalus\";")
        self.buttonQuit.setObjectName("buttonQuit")
        self.buttonStart = QtWidgets.QPushButton(Form)
        self.buttonStart.setGeometry(QtCore.QRect(50, 520, 91, 31))
        self.buttonStart.setStyleSheet("font: 10pt \"Andalus\";")
        self.buttonStart.setObjectName("buttonStart")
        self.textEdit = QtWidgets.QTextEdit(Form)
        self.textEdit.setGeometry(QtCore.QRect(50, 40, 351, 291))
        self.textEdit.setStyleSheet("font: 10pt \"Andalus\";")
        self.textEdit.setObjectName("textEdit")
        self.label_print_title = QtWidgets.QLabel(Form)
        self.label_print_title.setGeometry(QtCore.QRect(50, 20, 54, 12))
        self.label_print_title.setObjectName("label_print_title")
        self.buttonImport = QtWidgets.QPushButton(Form)
        self.buttonImport.setGeometry(QtCore.QRect(50, 360, 91, 31))
        self.buttonImport.setStyleSheet("font: 10pt \"Andalus\";")
        self.buttonImport.setObjectName("buttonImport")
        self.buttonShow = QtWidgets.QPushButton(Form)
        self.buttonShow.setGeometry(QtCore.QRect(410, 40, 81, 31))
        self.buttonShow.setStyleSheet("font: 10pt \"Andalus\";")
        self.buttonShow.setObjectName("buttonShow")
        self.buttonClear = QtWidgets.QPushButton(Form)
        self.buttonClear.setGeometry(QtCore.QRect(410, 160, 81, 31))
        self.buttonClear.setStyleSheet("font: 10pt \"Andalus\";")
        self.buttonClear.setObjectName("buttonClear")
        self.buttonCowpy = QtWidgets.QPushButton(Form)
        self.buttonCowpy.setGeometry(QtCore.QRect(410, 200, 81, 31))
        self.buttonCowpy.setStyleSheet("font: 10pt \"Andalus\";")
        self.buttonCowpy.setObjectName("buttonCowpy")
        self.buttonHide = QtWidgets.QPushButton(Form)
        self.buttonHide.setGeometry(QtCore.QRect(410, 80, 81, 31))
        self.buttonHide.setStyleSheet("font: 10pt \"Andalus\";")
        self.buttonHide.setObjectName("buttonHide")
        self.buttonCopy = QtWidgets.QPushButton(Form)
        self.buttonCopy.setGeometry(QtCore.QRect(410, 120, 81, 31))
        self.buttonCopy.setStyleSheet("font: 10pt \"Andalus\";")
        self.buttonCopy.setObjectName("buttonCopy")
        self.progressBar_Stock = QtWidgets.QProgressBar(Form)
        self.progressBar_Stock.setGeometry(QtCore.QRect(50, 420, 381, 21))
        self.progressBar_Stock.setProperty("value", 0)
        self.progressBar_Stock.setObjectName("progressBar_Stock")
        self.label_progress_title = QtWidgets.QLabel(Form)
        self.label_progress_title.setGeometry(QtCore.QRect(50, 400, 81, 16))
        self.label_progress_title.setObjectName("label_progress_title")
        self.label_import_rawdata_title = QtWidgets.QLabel(Form)
        self.label_import_rawdata_title.setGeometry(QtCore.QRect(50, 340, 91, 16))
        self.label_import_rawdata_title.setObjectName("label_import_rawdata_title")
        self.label_status_rawdata_title = QtWidgets.QLabel(Form)
        self.label_status_rawdata_title.setGeometry(QtCore.QRect(170, 340, 51, 16))
        self.label_status_rawdata_title.setObjectName("label_status_rawdata_title")
        self.labelStatusRawdataValue = QtWidgets.QLabel(Form)
        self.labelStatusRawdataValue.setGeometry(QtCore.QRect(170, 360, 61, 31))
        self.labelStatusRawdataValue.setObjectName("labelStatusRawdataValue")
        self.label_file_rawdata_title = QtWidgets.QLabel(Form)
        self.label_file_rawdata_title.setGeometry(QtCore.QRect(260, 340, 51, 16))
        self.label_file_rawdata_title.setObjectName("label_file_rawdata_title")
        self.labelFileRawdataValue = QtWidgets.QLabel(Form)
        self.labelFileRawdataValue.setGeometry(QtCore.QRect(260, 360, 61, 31))
        self.labelFileRawdataValue.setObjectName("labelFileRawdataValue")
        self.label_quit_title = QtWidgets.QLabel(Form)
        self.label_quit_title.setGeometry(QtCore.QRect(50, 560, 61, 16))
        self.label_quit_title.setObjectName("label_quit_title")
        self.progressBar_Reviews = QtWidgets.QProgressBar(Form)
        self.progressBar_Reviews.setGeometry(QtCore.QRect(50, 470, 381, 21))
        self.progressBar_Reviews.setProperty("value", 0)
        self.progressBar_Reviews.setObjectName("progressBar_Reviews")
        self.label_remainingTime_stock = QtWidgets.QLabel(Form)
        self.label_remainingTime_stock.setGeometry(QtCore.QRect(50, 440, 141, 31))
        self.label_remainingTime_stock.setObjectName("label_remainingTime_stock")
        self.label_remainingTime_reviews = QtWidgets.QLabel(Form)
        self.label_remainingTime_reviews.setGeometry(QtCore.QRect(50, 490, 181, 31))
        self.label_remainingTime_reviews.setObjectName("label_remainingTime_reviews")

        self.retranslateUi(Form)
        self.buttonQuit.clicked.connect(Form.close)
        self.buttonShow.clicked.connect(self.textEdit.show)
        self.buttonClear.clicked.connect(self.textEdit.clear)
        #self.buttonCowpy.clicked.connect(self.msg_cowpy_print)
        self.buttonHide.clicked.connect(self.textEdit.hide)
        self.buttonCopy.clicked.connect(self.textEdit.copy)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Spider"))
        self.buttonQuit.setText(_translate("Form", "quit"))
        self.buttonStart.setText(_translate("Form", "start"))
        self.label_print_title.setText(_translate("Form", "打印区："))
        self.buttonImport.setText(_translate("Form", "import"))
        self.buttonShow.setText(_translate("Form", "show"))
        self.buttonClear.setText(_translate("Form", "clear"))
        self.buttonCowpy.setText(_translate("Form", "cowpy"))
        self.buttonHide.setText(_translate("Form", "hide"))
        self.buttonCopy.setText(_translate("Form", "copy"))
        self.label_progress_title.setText(_translate("Form", "<html><head/><body><p><span style=\" font-size:10pt;\">进度:</span></p></body></html>"))
        self.label_import_rawdata_title.setText(_translate("Form", "<html><head/><body><p><span style=\" font-size:10pt;\">导入原始数据</span></p></body></html>"))
        self.label_status_rawdata_title.setText(_translate("Form", "<html><head/><body><p><span style=\" font-size:10pt;\">状态</span></p></body></html>"))
        self.labelStatusRawdataValue.setText(_translate("Form", "<html><head/><body><p><span style=\" font-size:10pt;\">未导入</span></p></body></html>"))
        self.label_file_rawdata_title.setText(_translate("Form", "<html><head/><body><p><span style=\" font-size:10pt;\">文件</span></p></body></html>"))
        self.labelFileRawdataValue.setText(_translate("Form", "<html><head/><body><p><span style=\" font-size:10pt;\">空</span></p></body></html>"))
        self.label_quit_title.setText(_translate("Form", "<html><head/><body><p><span style=\" font-size:10pt;\">退出：</span></p></body></html>"))
        self.label_remainingTime_stock.setText(_translate("Form", "<html><head/><body><p><span style=\" font-size:10pt;\">Remaining Time:</span></p></body></html>"))
        self.label_remainingTime_reviews.setText(_translate("Form", "<html><head/><body><p><span style=\" font-size:10pt;\">Remaining Time:</span></p></body></html>"))


    def setupData(self):
        self.importData = ''

    def msg_import_xml(self):
        fileName, fileType = QFileDialog.getOpenFileName(self,
                                                         "选取要导入的亚马逊库存原始数据",
                                                         "/a/0ps/temp/11/python3/workspace/factory/transition/pyqt/amazon/amazon_stock",  # 起始路径
                                                         "Xlsx Files(*.xlsx);;All Files (*)"  # 设置文件扩展名过滤，注意用双分号间隔
                                                         )
        if fileName:
            self.importData = fileName
            self.msg_import_status(fileName)

    def msg_import_status(self,fileName):
        self.labelStatusRawdataValue.setText('已导入')
        self.labelFileRawdataValue.setText(fileName)
        self.labelFileRawdataValue.adjustSize()

    def msg_start(self):
        if not self.importData:
            reply = QMessageBox.warning(self,  # 使用warning信息框
                                        "错误",
                                        "请先import",
                                        QMessageBox.Yes | QMessageBox.No)
            if reply == QMessageBox.Yes:
                self.msg_import_xml()
            else:
                return

    def msg_cowpy_print(self,msg):
        self.textEdit.append(msg)

    def msg_print(self):
        msg = self.bufferPrint
        self.textEdit.append(msg)

    def msg_progress(self,length,num):
        self.progressBar_Stock.setMinimum(0)
        self.progressBar_Stock.setMaximum(length)
        self.progressBar_Stock.setValue(num)

    def msg_show_remainingTime(self,startTime,length,num):
        _translate = QtCore.QCoreApplication.translate
        localTime = time.time()
        remainTime = ( localTime - startTime ) / num * length
        remainTime = str(int(remainTime/60)) + 'm ' + str(int(remainTime%60)) + 's'
        #self.label_remainingTime_stock.setText('Remaining Time:' + remainTime )
        self.label_remainingTime_stock.setText(_translate("Form",
                                                          "<html><head/><body><p><span style=\" font-size:10pt;\">" + 'Remaining Time:' + " " + remainTime + "</span></p></body></html>"))
        self.label_remainingTime_stock.adjustSize()