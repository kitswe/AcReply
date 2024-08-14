# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'untitledlOWfuh.ui'
##
## Created by: Qt User Interface Compiler version 6.7.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################
import sys
import time
import Epate
import pywinstyles

import os
from PySide6 import QtGui
from PySide6.QtCore import (QCoreApplication, QMetaObject, Qt)
from PySide6.QtWidgets import (QApplication, QFormLayout, QSizePolicy,
                               QSplitter)

from qfluentwidgets import (BodyLabel, CheckBox, ComboBox, FluentIcon,
                            LineEdit, PrimaryPushButton, Slider,
                            StrongBodyLabel, SubtitleLabel, TextEdit, Theme,
                            setTheme, setThemeColor)
import requests


class Ui_Form(object):

    def setupUi(self, Form):

        def get_resource_path(relative_path):
            if hasattr(sys, '_MEIPASS'):
                return os.path.join(sys._MEIPASS, relative_path)
            return os.path.join(os.path.abspath("."), relative_path)

        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(400, 444)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding,
                                 QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Form.sizePolicy().hasHeightForWidth())
        Form.setSizePolicy(sizePolicy)
        ico_path = os.path.join(os.path.dirname(__file__),
                                get_resource_path('images/CatLiker.ico'))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(ico_path), QtGui.QIcon.Normal,
                       QtGui.QIcon.Off)
        Form.setWindowIcon(icon)

        pywinstyles.apply_style(Form, 'mica')
        setTheme(Theme.AUTO)
        setThemeColor(pywinstyles.get_accent_color())

        self.formLayout = QFormLayout(Form)
        self.formLayout.setObjectName(u"formLayout")

        self.splitter = QSplitter(Form)
        self.splitter.setObjectName(u"splitter")
        sizePolicy.setHeightForWidth(
            self.splitter.sizePolicy().hasHeightForWidth())
        self.splitter.setSizePolicy(sizePolicy)
        self.splitter.setOrientation(Qt.Orientation.Vertical)

        self.label_1 = SubtitleLabel('您的用户名')
        self.label_1.setObjectName(u"label_1")
        self.splitter.addWidget(self.label_1)

        self.lineEdit = LineEdit(self.splitter)
        self.lineEdit.setObjectName(u"lineEdit")
        self.splitter.addWidget(self.lineEdit)

        self.label_2 = SubtitleLabel('您的密码')
        self.label_2.setObjectName(u"label_2")
        self.splitter.addWidget(self.label_2)

        self.lineEdit2 = LineEdit(self.splitter)
        self.lineEdit2.setObjectName(u"lineEdit2")
        self.splitter.addWidget(self.lineEdit2)

        self.label_a = SubtitleLabel('评论内容')
        self.label_a.setObjectName(u"label_a")
        self.splitter.addWidget(self.label_a)

        self.lineEdita = LineEdit(self.splitter)
        self.lineEdita.setObjectName(u"lineEdita")
        self.splitter.addWidget(self.lineEdita)

        self.label_3 = SubtitleLabel('间隔时间')
        self.label_3.setObjectName(u"label_3")
        self.splitter.addWidget(self.label_3)

        self.horizontalSlider = Slider(self.splitter)
        self.horizontalSlider.setObjectName(u"horizontalSlider")
        self.horizontalSlider.setOrientation(Qt.Orientation.Horizontal)
        self.horizontalSlider.setRange(2, 600)
        self.horizontalSlider.setValue(5)
        self.horizontalSlider.valueChanged.connect(self.sliderValueChanged)
        self.splitter.addWidget(self.horizontalSlider)

        self.label_4 = StrongBodyLabel('当前值为 5 秒')
        self.label_4.setObjectName(u"label_4")
        self.splitter.addWidget(self.label_4)

        self.label_5 = SubtitleLabel('上限次数')
        self.label_5.setObjectName(u"label_5")
        self.splitter.addWidget(self.label_5)

        self.horizontalSlider2 = Slider(self.splitter)
        self.horizontalSlider2.setObjectName(u"horizontalSlider2")
        self.horizontalSlider2.setOrientation(Qt.Orientation.Horizontal)
        self.horizontalSlider2.setRange(1, 500)
        self.horizontalSlider2.setValue(10)
        self.horizontalSlider2.valueChanged.connect(self.sliderValueChanged)
        self.splitter.addWidget(self.horizontalSlider2)

        self.label_6 = StrongBodyLabel('当前值为 10 次')
        self.label_6.setObjectName(u"label_6")
        self.splitter.addWidget(self.label_6)

        self.pushButton = PrimaryPushButton(FluentIcon.PLAY_SOLID, '开始')
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.clicked.connect(self.check)
        self.splitter.addWidget(self.pushButton)

        self.label_7 = SubtitleLabel('日志')
        self.label_7.setObjectName(u"label_7")
        self.splitter.addWidget(self.label_7)

        self.log = TextEdit(self.splitter)
        self.log.setObjectName(u"log")
        self.splitter.addWidget(self.log)

        self.formLayout.setWidget(0, QFormLayout.SpanningRole, self.splitter)

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)

    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(
            QCoreApplication.translate("Form", u"AcReply", None))

    def sliderValueChanged(self):
        self.label_4.setText(
            QCoreApplication.translate(
                'Form', u"当前值为 " + str(self.horizontalSlider.value()) + ' 秒',
                None))
        self.label_6.setText(
            QCoreApplication.translate(
                'Form', u"当前值为 " + str(self.horizontalSlider2.value()) + ' 次',
                None))

    def addLog(self, text: str):
        self.log.append(f'{text}')

    def main(self):
        idfile = open(txt_path, "r")
        idlist = idfile.readlines()
        idfile.close()



        self.addLog('INFO 正在登录')
        try:
            login_info = Epate.login(self.lineEdit.text(), self.lineEdit2.text())
            self.addLog('INFO 登录成功 - http' + login_info)
        except Exception as errinfo:
            self.addLog('ERROR 登录失败 -' + str(errinfo))

        self.addLog('INFO 开始自动回复')

        for i in range(self.horizontalSlider2.value()):
            self.addLog('INFO 第' + str(i + 1) + '次' + ' - ' + str(self.horizontalSlider2.value()) + '次')
            new_work = requests.get('https://api.codemao.cn/creation-tools/v1/pc/discover/newest-work?offset=0&limit=5')
            new_work_json = new_work.json()
            the_work_s_id = str(new_work_json['items'][0]['work_id'])
            if the_work_s_id not in idlist:
                
                reply_info = Epate.comment.work(int(the_work_s_id),self.lineEdita.text())
                idlist.append(the_work_s_id)

                idfile = open(txt_path, "a")
                idfile.write(the_work_s_id + '\n')
                idfile.close()

                self.addLog(f'INFO 为{the_work_s_id}评论成功 - http' + reply_info)
            else:
                self.addLog(f'ERROR 为{the_work_s_id}评论失败-作品已被评论，将持续尝试')
                while the_work_s_id not in idlist:
                    new_work = requests.get('https://api.codemao.cn/creation-tools/v1/pc/discover/newest-work?offset=0&limit=5')
                    new_work_json = new_work.json()
                    the_work_s_id = new_work_json['items'][0]['work_id']
                    try:
                        Epate.comment.work(the_work_s_id,'您的作品真不错！')
                        idlist.append(the_work_s_id)
                        self.addLog(f'INFO 为{the_work_s_id}评论成功 - http' + reply_info)
                    except Exception as errinfo:
                        self.addLog(f'ERROR 为{the_work_s_id}评论失败 - '+ errinfo)
                    
            time.sleep(self.horizontalSlider.value())

    def check(self):
        if self.lineEdit.text() == '' or self.lineEdit2.text() == '' or self.lineEdita.text() == '':
            self.addLog('ERROR 请输入完整信息')
        else:
            def get_resource_path(relative_path):
                if hasattr(sys, '_MEIPASS'):
                    return os.path.join(sys._MEIPASS, relative_path)
                return os.path.join(os.path.abspath("."), relative_path)
            global txt_path
            txt_path = os.path.join(os.path.dirname(__file__),get_resource_path('info/id.txt'))
            self.main()