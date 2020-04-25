# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Widows.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!
import urllib.parse
from turtle import color

from PyQt5 import QtCore, QtWidgets
from PyQt5.QtCore import QThread, pyqtSignal, QBasicTimer
from PyQt5.QtGui import QCursor
from PyQt5.QtWidgets import QFileDialog, QAction, QMenu
import xml.dom.minidom
import shutil,os

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(960, 540)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout.addWidget(self.pushButton)
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setObjectName("lineEdit")
        #开启拖拽
        self.setAcceptDrops(True)
        self.horizontalLayout.addWidget(self.lineEdit)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.radioButton = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton.setObjectName("radioButton")
        self.horizontalLayout_3.addWidget(self.radioButton)
        self.radioButton_2 = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton_2.setChecked(True)
        self.radioButton_2.setAutoRepeat(False)
        self.radioButton_2.setObjectName("radioButton_2")
        self.horizontalLayout_3.addWidget(self.radioButton_2)
        self.radioButton_3 = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton_3.setEnabled(True)
        self.radioButton_3.setTabletTracking(False)
        self.radioButton_3.setAcceptDrops(False)
        self.radioButton_3.setAutoFillBackground(False)
        self.radioButton_3.setChecked(False)
        self.radioButton_3.setObjectName("radioButton_3")
        self.horizontalLayout_3.addWidget(self.radioButton_3)
        self.radioButton_4 = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton_4.setObjectName("radioButton_4")
        self.horizontalLayout_3.addWidget(self.radioButton_4)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem)
        self.radioButton_5 = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton_5.setObjectName("radioButton_5")
        self.horizontalLayout_3.addWidget(self.radioButton_5)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setObjectName("label")
        self.horizontalLayout_3.addWidget(self.label)
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.horizontalLayout_3.addWidget(self.lineEdit_2)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser.setObjectName("textBrowser")
        self.verticalLayout.addWidget(self.textBrowser)
        #进度条
        self.progressBar = QtWidgets.QProgressBar(self.centralwidget)
        self.progressBar.setProperty("value", 0)
        self.progressBar.setObjectName("progressBar")
        self.verticalLayout.addWidget(self.progressBar)
        #样式
        style = """
                        QProgressBar {
                            border-radius: 5px;
                            text-align: center;
                        }"""
        self.progressBar.setStyleSheet(style)
        self.textBrowser.append('注意事项：不要在爬取过程中关闭程序，会造成最终拷贝文件的不完整。需要手动删除。')

        #创建计时器
        self.timer = QBasicTimer()
        #初始时间
        self.timer.start(100, self)

        #右键清除
        self.textBrowser.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.textBrowser.customContextMenuRequested[QtCore.QPoint].connect(self.right)




        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_2.addWidget(self.label_2)
        spacerItem1 = QtWidgets.QSpacerItem(128, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem1)


        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalLayout_2.addWidget(self.pushButton_2)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.verticalLayout_2.addLayout(self.verticalLayout)
        MainWindow.setCentralWidget(self.centralwidget)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.label2 = QtWidgets.QLabel(self.centralwidget)
        self.label2.setObjectName("label")
        self.horizontalLayout_3.addWidget(self.label2)
        #pushButton = 选择xml
        #lineEdit = 显示路径地址
        #radioButton = 视频选项
        #radioButton_2 = 音频选项
        #radioButton_3 = 图片选项
        #radioButton_4 = 全部
        #radioButton_5= 增加扩展
        #lineEdit_2 = 自定义内容
        #textBrowser = 打印平台
        #progressBar = 进度监看
        #pushButton_2 = 输出确认
        self.pushButton.clicked.connect(self.PushButton)
        self.radioButton.clicked.connect(self.RadioButton)
        self.radioButton_2.clicked.connect(self.RadioButton_2)
        self.radioButton_3.clicked.connect(self.RadioButton_3)
        self.radioButton_4.clicked.connect(self.RadioButton_4)
        self.radioButton_5.clicked.connect(self.RadioButton_5)
        self.pushButton_2.clicked.connect(self.PushButton_2)
        #状态
        self.lineEdit_2.setEnabled(False)
    #右键按钮
    def right(self):
        popMenu = QMenu()
        popMenu.addAction(QAction(u'clear', self))
        popMenu.triggered[QAction].connect(self.processtrigger)
        popMenu.exec_(QCursor.pos())
    #右键事件
    def processtrigger(self, q):
        self.textBrowser.clear()
    #拖拽执行
    def dragEnterEvent(self, evn):
        #拖入执行
        evn.accept()
    def dropEvent(self, evn):
        #松开鼠标
        a = evn.mimeData().text().replace('file://','')
        if a.endswith('.xml'):
            self.lineEdit.setText(a)



    def PushButton(self):
        fname, _ = QFileDialog.getOpenFileName(self, "请选择xml文件路径", "/Users/apple/Desktop", '(*.xml)')
        if fname:
            self.pushButton_2.setEnabled(True)
            self.lineEdit.setText(fname)
        else:
            self.textBrowser.append('')
    def RadioButton(self):
        self.radioButton.setEnabled(True)
    def RadioButton_2(self):
        self.lineEdit_2.setEnabled(False)
    def RadioButton_3(self):
        self.lineEdit_2.setEnabled(False)
    def RadioButton_4(self):
        self.lineEdit_2.setEnabled(False)
    def RadioButton_5(self):
        self.lineEdit_2.setEnabled(True)
    def PushButton_2(self):
        fname2 = QFileDialog.getExistingDirectory(self, "请选择输出文件路径", "/Users/apple/Desktop")
        self.progressBar.setProperty("value", 0)
        if fname2:
            self.pushButton_2.setText(QtCore.QCoreApplication.translate("MainWindow", "生成中"))
            self.pushButton_2.setEnabled(False)
            self.range = ''
            if self.radioButton.isChecked() == True:
                self.range = '.mp4', '.mov'
            if self.radioButton_2.isChecked() == True:
                self.range = '.wav', '.mp3'
            if self.radioButton_3.isChecked() == True:
                self.range = '.jpg', '.png'
            if self.radioButton_4.isChecked() == True:
                self.range = ['all']
            if self.radioButton_5.isChecked() == True:
                a = self.lineEdit_2.text()
                self.range = a
            # 多线程实例
            self.Thread = MyThread(self.lineEdit.text(), fname2, self.range)
            # 链接信号，发送信号
            self.Thread.trigger.connect(self.display)
            # 链接进度条信号
            self.Thread.proess.connect(self.pro)
            #返回值
            self.Thread.Run.connect(self.Run)
            # 开启多线程
            self.Thread.start()
        else:
            self.textBrowser.append('')
    #平台信号
    def display(self, msm):
        self.textBrowser.append(msm)
    #进度条信号
    def pro(self,n):
        self.progressBar.setValue(n)
    #返回值
    def Run(self,n):
        if n == 1:
            self.pushButton_2.setText(QtCore.QCoreApplication.translate("MainWindow", "输出文件"))
            self.pushButton_2.setEnabled(True)

    def retranslateUi(self, MainWindow):
        v=str(0)
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "XML文件爬虫软件"))
        self.pushButton.setText(_translate("MainWindow", "选择xml"))
        self.radioButton.setText(_translate("MainWindow", "视频媒体(mp4,mov)"))
        self.radioButton_2.setText(_translate("MainWindow", "音频媒体(wav,mp3)"))
        self.radioButton_3.setText(_translate("MainWindow", "图片(jpg,png)"))
        self.radioButton_4.setText(_translate("MainWindow", "全部"))
        self.radioButton_5.setText(_translate("MainWindow", "额外"))
        self.label.setText(_translate("MainWindow", "自定义过滤(例: .MOV)："))
        self.label_2.setText(_translate("MainWindow", "作者：金健  WeChat：jinmuzaiyan"))
        self.pushButton_2.setText(_translate("MainWindow", "输出文件"))




class MyThread(QThread):
    trigger = pyqtSignal(str)
    proess = pyqtSignal(int)
    Run = pyqtSignal(int)
    def __init__(self, xmlpath, out, expan):
        super().__init__()
        self.xmlpath = xmlpath
        self.out = out
        self.expan = expan
    def run(self):
        xmlpath = self.xmlpath
        out = self.out
        expan = self.expan
        dom = xml.dom.minidom.parse(xmlpath)
        root = dom.documentElement
        b = root.getElementsByTagName("pathurl")

        #设置进度条计时器变量
        offset = 0
        #自定义
        Len = 0
        l =set()
        #开始循环增加计时器并计算
        for x in b:
            argv = x.childNodes[0].data
            a = argv.replace('file://localhost', '')
            s = urllib.parse.unquote(a)
            if 'all' in expan:
                offset = int(offset) + 1
                proess = int(offset) / len(b) * 100
                self.trigger.emit('正在拷贝' + os.path.basename(s))
                shutil.copyfile(s, out + '/' + os.path.basename(s))
                #进度条发送信号
                self.proess.emit(int(proess))
            else:
                if s.endswith(expan):
                    Len = int(Len) + 1
                    l.add(s)
                else:
                    continue
        if Len>0:
            offset = 0
            for i in l:
                offset = int(offset) + 1
                proess = int(offset) / Len * 100
                self.trigger.emit('正在拷贝' + os.path.basename(i))
                shutil.copyfile(i, out + '/' + os.path.basename(i))
                # 进度条发送信号
                self.proess.emit(int(proess))
        self.Run.emit(1)



