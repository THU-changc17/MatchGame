# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'num_2.ui'
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
        Form.resize(1000, 700)
        self.NewGame = QtWidgets.QPushButton(Form)
        self.NewGame.setGeometry(QtCore.QRect(350, 70, 120, 30))
        self.NewGame.setStyleSheet("")
        self.NewGame.setIconSize(QtCore.QSize(30, 30))
        self.NewGame.setAutoDefault(False)
        self.NewGame.setObjectName("NewGame")
        self.Solve = QtWidgets.QPushButton(Form)
        self.Solve.setGeometry(QtCore.QRect(690, 70, 120, 30))
        self.Solve.setObjectName("Solve")
        self.questionline = QtWidgets.QLineEdit(Form)
        self.questionline.setGeometry(QtCore.QRect(410, 10, 160, 20))
        self.questionline.setText("")
        self.questionline.setObjectName("questionline")
        self.comboBox = QtWidgets.QComboBox(Form)
        self.comboBox.setGeometry(QtCore.QRect(150, 70, 120, 30))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.model = QtWidgets.QLabel(Form)
        self.model.setGeometry(QtCore.QRect(160, 10, 120, 20))
        self.model.setObjectName("model")
        self.questionbase = QtWidgets.QCheckBox(Form)
        self.questionbase.setGeometry(QtCore.QRect(110, 40, 100, 20))
        self.questionbase.setObjectName("questionbase")
        self.myquestion = QtWidgets.QCheckBox(Form)
        self.myquestion.setGeometry(QtCore.QRect(230, 40, 100, 20))
        self.myquestion.setObjectName("myquestion")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(690, 40, 72, 20))
        self.label.setObjectName("label")
        self.num_result = QtWidgets.QLabel(Form)
        self.num_result.setGeometry(QtCore.QRect(750, 39, 40, 21))
        self.num_result.setText("")
        self.num_result.setObjectName("num_result")
        self.Num_1 = QtWidgets.QLabel(Form)
        self.Num_1.setGeometry(QtCore.QRect(80, 120, 100, 180))
        self.Num_1.setText("")
        self.Num_1.setObjectName("Num_1")
        self.Num_2 = QtWidgets.QLabel(Form)
        self.Num_2.setGeometry(QtCore.QRect(180, 120, 100, 180))
        self.Num_2.setText("")
        self.Num_2.setObjectName("Num_2")
        self.Add_1 = QtWidgets.QLabel(Form)
        self.Add_1.setGeometry(QtCore.QRect(380, 120, 100, 180))
        self.Add_1.setText("")
        self.Add_1.setObjectName("Add_1")
        self.Add_2 = QtWidgets.QLabel(Form)
        self.Add_2.setGeometry(QtCore.QRect(480, 120, 100, 180))
        self.Add_2.setText("")
        self.Add_2.setObjectName("Add_2")
        self.Sym = QtWidgets.QLabel(Form)
        self.Sym.setGeometry(QtCore.QRect(280, 120, 100, 180))
        self.Sym.setText("")
        self.Sym.setObjectName("Sym")
        self.Is = QtWidgets.QLabel(Form)
        self.Is.setGeometry(QtCore.QRect(580, 120, 100, 180))
        self.Is.setText("")
        self.Is.setObjectName("Is")
        self.Result_1 = QtWidgets.QLabel(Form)
        self.Result_1.setGeometry(QtCore.QRect(680, 120, 100, 180))
        self.Result_1.setText("")
        self.Result_1.setObjectName("Result_1")
        self.Result_2 = QtWidgets.QLabel(Form)
        self.Result_2.setGeometry(QtCore.QRect(780, 120, 100, 180))
        self.Result_2.setText("")
        self.Result_2.setObjectName("Result_2")
        self.Result2_2 = QtWidgets.QLabel(Form)
        self.Result2_2.setGeometry(QtCore.QRect(780, 370, 100, 180))
        self.Result2_2.setText("")
        self.Result2_2.setObjectName("Result2_2")
        self.Num2_1 = QtWidgets.QLabel(Form)
        self.Num2_1.setGeometry(QtCore.QRect(80, 370, 100, 180))
        self.Num2_1.setText("")
        self.Num2_1.setObjectName("Num2_1")
        self.Add2_1 = QtWidgets.QLabel(Form)
        self.Add2_1.setGeometry(QtCore.QRect(380, 370, 100, 180))
        self.Add2_1.setText("")
        self.Add2_1.setObjectName("Add2_1")
        self.Add2_2 = QtWidgets.QLabel(Form)
        self.Add2_2.setGeometry(QtCore.QRect(480, 370, 100, 180))
        self.Add2_2.setText("")
        self.Add2_2.setObjectName("Add2_2")
        self.Num2_2 = QtWidgets.QLabel(Form)
        self.Num2_2.setGeometry(QtCore.QRect(180, 370, 100, 180))
        self.Num2_2.setText("")
        self.Num2_2.setObjectName("Num2_2")
        self.Is_2 = QtWidgets.QLabel(Form)
        self.Is_2.setGeometry(QtCore.QRect(580, 370, 100, 180))
        self.Is_2.setText("")
        self.Is_2.setObjectName("Is_2")
        self.Result2_1 = QtWidgets.QLabel(Form)
        self.Result2_1.setGeometry(QtCore.QRect(680, 370, 100, 180))
        self.Result2_1.setText("")
        self.Result2_1.setObjectName("Result2_1")
        self.Sym_2 = QtWidgets.QLabel(Form)
        self.Sym_2.setGeometry(QtCore.QRect(280, 370, 100, 180))
        self.Sym_2.setText("")
        self.Sym_2.setObjectName("Sym_2")
        self.resultline = QtWidgets.QLineEdit(Form)
        self.resultline.setGeometry(QtCore.QRect(410, 40, 160, 20))
        self.resultline.setText("")
        self.resultline.setObjectName("resultline")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(690, 10, 51, 20))
        self.label_2.setObjectName("label_2")
        self.hard_result = QtWidgets.QLabel(Form)
        self.hard_result.setGeometry(QtCore.QRect(750, 9, 41, 20))
        self.hard_result.setText("")
        self.hard_result.setObjectName("hard_result")
        self.Judge = QtWidgets.QPushButton(Form)
        self.Judge.setGeometry(QtCore.QRect(520, 70, 120, 30))
        self.Judge.setStyleSheet("")
        self.Judge.setIconSize(QtCore.QSize(30, 30))
        self.Judge.setAutoDefault(False)
        self.Judge.setObjectName("Judge")
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(830, 70, 111, 30))
        self.label_3.setObjectName("label_3")
        self.help_button = QtWidgets.QPushButton(Form)
        self.help_button.setGeometry(QtCore.QRect(835, 10, 95, 30))
        self.help_button.setObjectName("help_button")
        self.more = QtWidgets.QPushButton(Form)
        self.more.setGeometry(QtCore.QRect(20, 10, 90, 30))
        self.more.setObjectName("more")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.NewGame.setText(_translate("Form", "下一题"))
        self.Solve.setToolTip(_translate("Form", "<html><head/><body><p><span style=\" font-size:11pt;\">重复点击可获得算式其他解！</span></p></body></html>"))
        self.Solve.setWhatsThis(_translate("Form", "<html><head/><body><p><br/></p></body></html>"))
        self.Solve.setText(_translate("Form", "查看答案"))
        self.questionline.setPlaceholderText(_translate("Form", "请在此输入自定义算式"))
        self.comboBox.setItemText(0, _translate("Form", "移动一根火柴"))
        self.comboBox.setItemText(1, _translate("Form", "移动两根火柴"))
        self.comboBox.setItemText(2, _translate("Form", "等式变新等式"))
        self.model.setText(_translate("Form", "请选择游戏模式"))
        self.questionbase.setText(_translate("Form", "题库模式"))
        self.myquestion.setText(_translate("Form", "自定义模式"))
        self.label.setText(_translate("Form", "结果数："))
        self.resultline.setPlaceholderText(_translate("Form", "请在此输入你的答案"))
        self.label_2.setText(_translate("Form", "难度："))
        self.Judge.setText(_translate("Form", "查看正误"))
        self.label_3.setText(_translate("Form", "多解可重复点击"))
        self.help_button.setText(_translate("Form", "帮助"))
        self.more.setText(_translate("Form", "扩展模式"))