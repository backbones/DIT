# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Interface.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!
import self as self
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtCore import QThread, pyqtSignal
from PyQt5.QtWidgets import QFileDialog
import xml.dom.minidom
import sys ,os
from subprocess import Popen, PIPE
import urllib.parse

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(600, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.Select1 = QtWidgets.QPushButton(self.centralwidget)
        self.Select1.setObjectName("Select")
        self.verticalLayout.addWidget(self.Select1)
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setObjectName("lineEdit")

        self.verticalLayout.addWidget(self.lineEdit)
        self.verticalLayout_2.addLayout(self.verticalLayout)
        self.yes = QtWidgets.QPushButton(self.centralwidget)
        self.yes.setObjectName("yes")
        self.verticalLayout_2.addWidget(self.yes)
        self.horizontalLayout.addLayout(self.verticalLayout_2)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 209, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser.setObjectName("textBrowser")
        self.verticalLayout.addWidget(self.textBrowser)
        self.textBrowser.setLineWrapMode(0)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.Select1.clicked.connect(self.Select)
        self.yes.clicked.connect(self.run)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.Select1.setText(_translate("MainWindow", "选取xml文件"))
        self.yes.setText(_translate("MainWindow", "开始打点"))

    def Select(self):
        fname, _ = QFileDialog.getOpenFileName(self, "请选择xml文件路径", "/Users/apple/Desktop", '(*.xml)')
        if fname[0]:
            self.lineEdit.setText(fname)

    def run(self):
        Return = (self.lineEdit.text())
        self.xmlread(Return)
        self.yes.setText(QtCore.QCoreApplication.translate("MainWindow", "20200418"))
        self.yes.setEnabled(False)

    def display(self, str):
        self.textBrowser.append(str)

    def xmlread(self, xmlpath):
        self.xmlthread = MyThread(xmlpath)
        self.xmlthread.trigger.connect(self.display)
        self.xmlthread.start()

    def display(self, msm):
        self.textBrowser.append(msm)


class MyThread(QThread):
    trigger = pyqtSignal(str)

    def __init__(self, Return):
        super().__init__()
        self.Return = Return

    def run(self):
        Return = self.Return
        dom = xml.dom.minidom.parse(Return)
        root = dom.documentElement
        b = root.getElementsByTagName("pathurl")
        for x in b:
            argv = x.childNodes[0].data
            a = argv.replace('file://localhost', '')
            s = urllib.parse.unquote(a)
            echo = 'Cilp_Label:' + s
            p = os.path.dirname(sys.argv[0])+'/Label_script.scpt'
            (c, tError) = Popen(['osascript', p, s], stdout=PIPE).communicate()
            c = str(c).replace('\\n\'', '').replace('b\'', '')
            Output = echo
            self.trigger.emit(Output)
            Output = '状态' + c + '\n'
            self.trigger.emit(Output)
        self.trigger.emit('以上所有文件已经标记完毕')
        self.trigger.emit('trun的文件都是标记成功的，False都文件可能有特殊情况导致标记失败')