# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'help.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


import sys
import os
if hasattr(sys, 'frozen'):
    os.environ['PATH'] = sys._MEIPASS + ";" + os.environ['PATH']
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(760, 600)
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(40, 140, 671, 441))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(220, -30, 300, 150))
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "<html><head/><body><p><span style=\" font-size:10pt;\">游戏简介及说明：</span></p><p><span style=\" font-size:10pt;\">火柴数字游戏是一种益智类游戏，可有效锻炼人们的脑力，趣味无穷。</span></p><p><span style=\" font-size:10pt;\">玩家进入游戏后，请先选择模式呦！</span></p><p><span style=\" font-size:10pt;\">本游戏既可以采用题库模式，也可以采用自定义模式，提供三种游戏方案：移动一根火柴，</span></p><p><span style=\" font-size:10pt;\">移动两根火柴，等式变新等式。</span></p><p><span style=\" font-size:10pt;\">若采用题库模式，点击下一题即可得到待求等式（若题目不变请再刷新），玩家可输入自</span></p><p><span style=\" font-size:10pt;\">己的求解并查看正误，也可查看标准答案，若题目存在多解，只需重复点击查看答案即可</span></p><p><span style=\" font-size:10pt;\">获得全部解。</span></p><p><span style=\" font-size:10pt;\">若采用自定义模式，请在输入栏键入符合要求的等式(A±B=C或A×B=C或A=B±C或A=B×C）</span></p><p><span style=\" font-size:10pt;\">的形式，其中A，B，C均为个位数或两位数，×请用叉号代替，点击下一题即可开始自定义</span></p><p><span style=\" font-size:10pt;\">游戏，同样地，玩家可以自己求解查看正误，亦可查看答案。</span></p><p><span style=\" font-size:10pt;\">游戏还给出难度的评测，并显示全部结果的数量，在等式变新等式环节，答案中每个新等</span></p><p><span style=\" font-size:10pt;\">式给出的同时，系统还会显示变成这个等式需要移动的火柴根数</span></p><p><span style=\" font-size:10pt;\">开始您的火柴游戏之旅吧！</span><br/></p></body></html>"))
