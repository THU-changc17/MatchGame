import sys
import os
if hasattr(sys, 'frozen'):
    os.environ['PATH'] = sys._MEIPASS + ";" + os.environ['PATH']
from PyQt5 import QtWidgets,QtGui,QtCore
from num_2 import Ui_Form
from data import  getdata,getdata_2,getdata_3
from search import Search,Search_2
from search_complex import Search_com,Searchcom_2
import math
import help
import complex
#字体图片
all_word={0:'word/0.png',
          1:'word/1.png',
          2:'word/2.png',
          3:'word/3.png',
          4:'word/4.png',
          5:'word/5.png',
          6:'word/6.png',
          7:'word/7.png',
          8:'word/8.png',
          9:'word/9.png',
          '+':'word/+.png',
          '-':'word/-.png',
          '×':'word/×.png',
          '=':'word/=.png'}

class MYForm(QtWidgets.QWidget,Ui_Form):
    #emit_list = QtCore.pyqtSignal(list)
    def __init__(self):
        super(MYForm,self).__init__()
        self.setupUi(self)
        self.setWindowTitle("火柴数字游戏")
        self.setWindowIcon(QtGui.QIcon('Icon.jpg'))
        self.Num_1.setPixmap(QtGui.QPixmap('word/0.png'))
        self.Num_2.setPixmap(QtGui.QPixmap('word/0.png'))
        self.Add_1.setPixmap(QtGui.QPixmap('word/0.png'))
        self.Add_2.setPixmap(QtGui.QPixmap('word/0.png'))
        self.Sym.setPixmap(QtGui.QPixmap('word/+.png'))
        self.Is.setPixmap(QtGui.QPixmap('word/=.png'))
        self.Result_1.setPixmap(QtGui.QPixmap('word/0.png'))
        self.Result_2.setPixmap(QtGui.QPixmap('word/0.png'))
        self.Num2_1.setPixmap(QtGui.QPixmap('word/0.png'))
        self.Num2_2.setPixmap(QtGui.QPixmap('word/0.png'))
        self.Add2_1.setPixmap(QtGui.QPixmap('word/0.png'))
        self.Add2_2.setPixmap(QtGui.QPixmap('word/0.png'))
        self.Sym_2.setPixmap(QtGui.QPixmap('word/+.png'))
        self.Is_2.setPixmap(QtGui.QPixmap('word/=.png'))
        self.Result2_1.setPixmap(QtGui.QPixmap('word/0.png'))
        self.Result2_2.setPixmap(QtGui.QPixmap('word/0.png'))

        self.NewGame.clicked.connect(self.update)     #建立信号槽
        self.Solve.clicked.connect(self.show_result)    #建立信号槽
        self.Judge.clicked.connect(self.judge_result)   #建立信号槽
        self.help_button.clicked.connect(self.help_display)
        #self.more.clicked.connect(self.more_display)
        #self.emit_list.connect(self.receive_list)
        self.i = 0
        self.ini_list=[]     #将获取的等式作为全局变量
        self.flag_1 = [1, 1, 1, 1, 1, 1, 1, 1]
        self.flag_2 = [1, 1, 1, 1, 1, 1, 1, 1]

    def use_palette(self):
        window_pale = QtGui.QPalette()
        #pix = QtGui.QPalette()
        #pix.setColor(self.backgroundRole(), QtGui.QColor(255, 255, 255))  # 设置背景颜色
        #self.setPalette(pix)
        pix = QtGui.QPixmap('tim.jpg')
        pix = pix.scaled(self.width(), self.height())
        window_pale.setBrush(self.backgroundRole(), QtGui.QBrush(pix))
        self.setPalette(window_pale)

    def update(self):
        self.i = 0    #结果显示计数变量
        list = []
        self.flag_1 = [1, 1, 1, 1, 1, 1, 1, 1]   #各位标志位，是否存在该位数字或符号，若存在记为1
        self.num_result.setText("")
        self.hard_result.setText("")
        self.resultline.setText("")
        if(self.comboBox.currentText()==""):
            QtWidgets.QMessageBox.about(self, "警告", "请选择游戏模式！")
        elif(self.questionbase.isChecked()and self.myquestion.isChecked()):
            QtWidgets.QMessageBox.about(self, "警告", "请选择唯一的游戏模式！")
        elif (not self.questionbase.isChecked() and  not self.myquestion.isChecked()):
            QtWidgets.QMessageBox.about(self, "警告", "请选择游戏模式！")
        elif(self.questionbase.isChecked() and self.comboBox.currentText()=="移动一根火柴"):
            self.questionline.setText("")
            list = getdata()
            if(list[0]>=10):
                self.Num_1.setPixmap(QtGui.QPixmap(all_word[int(list[0]/10)]))
                self.Num_2.setPixmap(QtGui.QPixmap(all_word[int(list[0]%10)]))
            else:
                self.Num_1.clear()
                self.flag_1[0]=0
                self.Num_2.setPixmap(QtGui.QPixmap(all_word[list[0]]))
            if (list[2]>=10):
                self.Add_1.setPixmap(QtGui.QPixmap(all_word[int(list[2]/10)]))
                self.Add_2.setPixmap(QtGui.QPixmap(all_word[int(list[2]%10)]))
            else:
                self.Add_1.clear()
                self.flag_1[3] = 0
                self.Add_2.setPixmap(QtGui.QPixmap(all_word[list[2]]))
            if (list[4]>=10):
                self.Result_1.setPixmap(QtGui.QPixmap(all_word[int(list[4]/10)]))
                self.Result_2.setPixmap(QtGui.QPixmap(all_word[int(list[4]%10)]))
            else:
                self.Result_1.clear()
                self.flag_1[6]=0
                self.Result_2.setPixmap(QtGui.QPixmap(all_word[list[4]]))
            self.Sym.setPixmap(QtGui.QPixmap(all_word[list[1]]))
            self.Is.setPixmap(QtGui.QPixmap(all_word[list[3]]))

        elif (self.questionbase.isChecked() and self.comboBox.currentText() == "移动两根火柴"):
            self.questionline.setText("")
            list = getdata_2()
            if (list[0] >= 10):
                self.Num_1.setPixmap(QtGui.QPixmap(all_word[int(list[0] / 10)]))
                self.Num_2.setPixmap(QtGui.QPixmap(all_word[int(list[0] % 10)]))
            else:
                self.Num_1.clear()
                self.flag_1[0] = 0
                self.Num_2.setPixmap(QtGui.QPixmap(all_word[list[0]]))
            if (list[2] >= 10):
                self.Add_1.setPixmap(QtGui.QPixmap(all_word[int(list[2] / 10)]))
                self.Add_2.setPixmap(QtGui.QPixmap(all_word[int(list[2] % 10)]))
            else:
                self.Add_1.clear()
                self.flag_1[3] = 0
                self.Add_2.setPixmap(QtGui.QPixmap(all_word[list[2]]))
            if (list[4] >= 10):
                self.Result_1.setPixmap(QtGui.QPixmap(all_word[int(list[4] / 10)]))
                self.Result_2.setPixmap(QtGui.QPixmap(all_word[int(list[4] % 10)]))
            else:
                self.Result_1.clear()
                self.flag_1[6] = 0
                self.Result_2.setPixmap(QtGui.QPixmap(all_word[list[4]]))
            self.Sym.setPixmap(QtGui.QPixmap(all_word[list[1]]))
            self.Is.setPixmap(QtGui.QPixmap(all_word[list[3]]))
        elif(self.questionbase.isChecked() and self.comboBox.currentText() == "等式变新等式"):
            self.questionline.setText("")
            list = getdata_3()
            if (list[0] >= 10):
                self.Num_1.setPixmap(QtGui.QPixmap(all_word[int(list[0] / 10)]))
                self.Num_2.setPixmap(QtGui.QPixmap(all_word[int(list[0] % 10)]))
            else:
                self.Num_1.clear()
                self.flag_1[0] = 0
                self.Num_2.setPixmap(QtGui.QPixmap(all_word[list[0]]))
            if (list[2] >= 10):
                self.Add_1.setPixmap(QtGui.QPixmap(all_word[int(list[2] / 10)]))
                self.Add_2.setPixmap(QtGui.QPixmap(all_word[int(list[2] % 10)]))
            else:
                self.Add_1.clear()
                self.flag_1[3] = 0
                self.Add_2.setPixmap(QtGui.QPixmap(all_word[list[2]]))
            if (list[4] >= 10):
                self.Result_1.setPixmap(QtGui.QPixmap(all_word[int(list[4] / 10)]))
                self.Result_2.setPixmap(QtGui.QPixmap(all_word[int(list[4] % 10)]))
            else:
                self.Result_1.clear()
                self.flag_1[6] = 0
                self.Result_2.setPixmap(QtGui.QPixmap(all_word[list[4]]))
            self.Sym.setPixmap(QtGui.QPixmap(all_word[list[1]]))
            self.Is.setPixmap(QtGui.QPixmap(all_word[list[3]]))
        elif(self.myquestion.isChecked()):
            word = self.questionline.text()
            temp = 0
            try:     #异常处理，若输入等式不符合要求，则还原初始化状态
                for i in word:
                    if (i != "=" and i != "+" and i != "-" and i != "×"):
                        temp = temp * 10 + int(i)
                    else:
                        list.append(temp)
                        list.append(i)
                        temp = 0
                list.append(temp)
                if(len(list)>5):
                    QtWidgets.QMessageBox.about(self, "警告", "请输入符合要求的算式！")
                    self.Num_1.setPixmap(QtGui.QPixmap('word/0.png'))
                    self.Num_2.setPixmap(QtGui.QPixmap('word/0.png'))
                    self.Add_1.setPixmap(QtGui.QPixmap('word/0.png'))
                    self.Add_2.setPixmap(QtGui.QPixmap('word/0.png'))
                    self.Sym.setPixmap(QtGui.QPixmap('word/+.png'))
                    self.Is.setPixmap(QtGui.QPixmap('word/=.png'))
                    self.Result_1.setPixmap(QtGui.QPixmap('word/0.png'))
                    self.Result_2.setPixmap(QtGui.QPixmap('word/0.png'))
                else:
                    if (list[0] >= 10):
                        self.Num_1.setPixmap(QtGui.QPixmap(all_word[int(list[0] / 10)]))
                        self.Num_2.setPixmap(QtGui.QPixmap(all_word[int(list[0] % 10)]))
                    else:
                        self.Num_1.clear()
                        self.flag_1[0] = 0
                        self.Num_2.setPixmap(QtGui.QPixmap(all_word[list[0]]))
                    if (list[2] >= 10):
                        self.Add_1.setPixmap(QtGui.QPixmap(all_word[int(list[2] / 10)]))
                        self.Add_2.setPixmap(QtGui.QPixmap(all_word[int(list[2] % 10)]))
                    else:
                        self.Add_1.clear()
                        self.flag_1[3] = 0
                        self.Add_2.setPixmap(QtGui.QPixmap(all_word[list[2]]))
                    if (list[4] >= 10):
                        self.Result_1.setPixmap(QtGui.QPixmap(all_word[int(list[4] / 10)]))
                        self.Result_2.setPixmap(QtGui.QPixmap(all_word[int(list[4] % 10)]))
                    else:
                        self.Result_1.clear()
                        self.flag_1[6] = 0
                        self.Result_2.setPixmap(QtGui.QPixmap(all_word[list[4]]))
                    self.Sym.setPixmap(QtGui.QPixmap(all_word[list[1]]))
                    self.Is.setPixmap(QtGui.QPixmap(all_word[list[3]]))
            except Exception as e:
                self.Num_1.setPixmap(QtGui.QPixmap('word/0.png'))
                self.Num_2.setPixmap(QtGui.QPixmap('word/0.png'))
                self.Add_1.setPixmap(QtGui.QPixmap('word/0.png'))
                self.Add_2.setPixmap(QtGui.QPixmap('word/0.png'))
                self.Sym.setPixmap(QtGui.QPixmap('word/+.png'))
                self.Is.setPixmap(QtGui.QPixmap('word/=.png'))
                self.Result_1.setPixmap(QtGui.QPixmap('word/0.png'))
                self.Result_2.setPixmap(QtGui.QPixmap('word/0.png'))
                QtWidgets.QMessageBox.about(self, "警告", "请输入符合要求的算式！")
        self.Num2_1.setPixmap(QtGui.QPixmap('word/0.png'))
        self.Num2_2.setPixmap(QtGui.QPixmap('word/0.png'))
        self.Add2_1.setPixmap(QtGui.QPixmap('word/0.png'))
        self.Add2_2.setPixmap(QtGui.QPixmap('word/0.png'))
        self.Sym_2.setPixmap(QtGui.QPixmap('word/+.png'))
        self.Is_2.setPixmap(QtGui.QPixmap('word/=.png'))
        self.Result2_1.setPixmap(QtGui.QPixmap('word/0.png'))
        self.Result2_2.setPixmap(QtGui.QPixmap('word/0.png'))
        self.ini_list=list

    def show_result(self):
        self.flag_2 = [1, 1, 1, 1, 1, 1, 1, 1]
        list_display = []
        all_list_judge = []
        list_display_1 = []
        list_display_2 = []
        try:   #异常处理，若属于无法操作的等式，抛出异常
            if(self.comboBox.currentText()=="移动一根火柴"):
                list_display,all_list_judge = Search(self.ini_list)
            elif(self.comboBox.currentText()=="移动两根火柴"):
                list_display,all_list_judge = Search_2(self.ini_list)
            elif(self.comboBox.currentText()=="等式变新等式"):
                list_display_1, all_list_judge_1 = Search(self.ini_list)
                list_display_2, all_list_judge_2 = Search_2(self.ini_list)
                for i in list_display_1:
                    if(i not in list_display):
                        list_display.append(i)
                for j in all_list_judge_1:
                    if(j not in all_list_judge):
                        all_list_judge.append(j)
                for i in list_display_2:
                    if(i not in list_display):
                        list_display.append(i)
                for j in all_list_judge_2:
                    if(j not in all_list_judge):
                        all_list_judge.append(j)
            if (list_display == []):
                QtWidgets.QMessageBox.about(self, "提示", "此式无解！")
            elif (self.i == len(list_display)):
                QtWidgets.QMessageBox.about(self, "提示", "没有更多的解！")
                self.i = 0
            else:
                new_list = list_display[self.i]
                self.num_result.setText(str(len(list_display)))      #显示结果数
                self.hard_result.setText(str(math.log(len(all_list_judge)/len(list_display))))  #难度定义为ln(总实验次数/结果数）
                self.i += 1
                if (new_list[0] >= 10):
                    self.Num2_1.setPixmap(QtGui.QPixmap(all_word[int(new_list[0] / 10)]))
                    self.Num2_2.setPixmap(QtGui.QPixmap(all_word[int(new_list[0] % 10)]))
                else:
                    self.Num2_1.clear()
                    self.flag_2[0] = 0
                    self.Num2_2.setPixmap(QtGui.QPixmap(all_word[new_list[0]]))
                if (new_list[2] >= 10):
                    self.Add2_1.setPixmap(QtGui.QPixmap(all_word[int(new_list[2] / 10)]))
                    self.Add2_2.setPixmap(QtGui.QPixmap(all_word[int(new_list[2] % 10)]))
                else:
                    self.Add2_1.clear()
                    self.flag_2[3] = 0
                    self.Add2_2.setPixmap(QtGui.QPixmap(all_word[new_list[2]]))
                if (new_list[4] >= 10):
                    self.Result2_1.setPixmap(QtGui.QPixmap(all_word[int(new_list[4] / 10)]))
                    self.Result2_2.setPixmap(QtGui.QPixmap(all_word[int(new_list[4] % 10)]))
                else:
                    self.Result2_1.clear()
                    self.flag_2[6] = 0
                    self.Result2_2.setPixmap(QtGui.QPixmap(all_word[new_list[4]]))
                self.Sym_2.setPixmap(QtGui.QPixmap(all_word[new_list[1]]))
                self.Is_2.setPixmap(QtGui.QPixmap(all_word[new_list[3]]))
                #若移动火柴过程中将十位数字变为0，将0显示出来，或者在增加数字1时出现显示0的问题，在这里解决
                if(self.flag_1[0]==1 and self.flag_2[0]==0):
                    self.Num2_1.setPixmap(QtGui.QPixmap('word/0.png'))
                if(self.flag_1[3]==1 and self.flag_2[3]==0):
                    self.Add2_1.setPixmap(QtGui.QPixmap('word/0.png'))
                if(self.flag_1[6]==1 and self.flag_2[6]==0):
                    self.Result2_1.setPixmap(QtGui.QPixmap('word/0.png'))
                if(self.ini_list[0]==8 and new_list[0]==1):
                    self.Num2_1.setPixmap(QtGui.QPixmap('word/0.png'))
                if (self.ini_list[2]==8 and new_list[2]==1):
                    self.Add2_1.setPixmap(QtGui.QPixmap('word/0.png'))
                if (self.ini_list[4]==8 and new_list[4]==1):
                    self.Result2_1.setPixmap(QtGui.QPixmap('word/0.png'))
                if (self.comboBox.currentText() == "等式变新等式" and new_list in list_display_1):
                    QtWidgets.QMessageBox.about(self, "提示", "得到此结果需要移动一根火柴")
                if (self.comboBox.currentText() == "等式变新等式" and new_list in list_display_2):
                    QtWidgets.QMessageBox.about(self, "提示", "得到此结果需要移动两根火柴")
                list_t = [str(i) for i in self.ini_list]
                word_add=''.join(list_t)
                if(self.comboBox.currentText()=="移动一根火柴" and self.myquestion.isChecked() and self.i==1):
                    with open('data_1.txt', 'a')as g:
                        g.writelines(word_add+"\n")
                        g.close()
                elif(self.comboBox.currentText()=="移动两根火柴" and self.myquestion.isChecked() and self.i==1):
                    with open('data_2.txt', 'a')as g:
                        g.writelines(word_add+"\n")
                        g.close()
                elif(self.comboBox.currentText()=="等式变新等式" and self.myquestion.isChecked()and self.i==1):
                    with open('data_3.txt', 'a')as g:
                        g.writelines(word_add+"\n")
                        g.close()
        except Exception as e:
            QtWidgets.QMessageBox.about(self, "警告", "请输入符合要求的算式！")

    def judge_result(self):
        list_display = []
        all_list_judge = []
        list_display_1 = []
        list_display_2 = []
        if (self.comboBox.currentText() == "移动一根火柴"):
            list_display, all_list_judge = Search(self.ini_list)
        elif (self.comboBox.currentText() == "移动两根火柴"):
            list_display, all_list_judge = Search_2(self.ini_list)
        elif (self.comboBox.currentText() == "等式变新等式"):
            list_display_1, all_list_judge_1 = Search(self.ini_list)
            list_display_2, all_list_judge_2 = Search_2(self.ini_list)
            for i in list_display_1:
                if (i not in list_display):
                    list_display.append(i)
            for j in all_list_judge_1:
                if (j not in all_list_judge):
                    all_list_judge.append(j)
            for i in list_display_2:
                if (i not in list_display):
                    list_display.append(i)
            for j in all_list_judge_2:
                if (j not in all_list_judge):
                    all_list_judge.append(j)
        if (list_display == []):
            QtWidgets.QMessageBox.about(self, "提示", "此式无解！")
        #将文本转化为列表形式
        answer_word=self.resultline.text()
        answer_list = []
        temp = 0
        for i in answer_word:
            if (i != "=" and i != "+" and i != "-" and i != "×"):
                temp = temp * 10 + int(i)
            else:
                answer_list.append(temp)
                answer_list.append(i)
                temp = 0
        answer_list.append(temp)
        if(answer_list in list_display):
            QtWidgets.QMessageBox.about(self, "提示", "您的答案是正确的！")
        else:
            QtWidgets.QMessageBox.about(self, "提示", "您的答案是错误的！")

    def help_display(self):
        form2 = QtWidgets.QDialog()
        ui = help.Ui_Form()
        ui.setupUi(form2)
        form2.setFixedSize(760,600)
        form2.setWindowTitle("火柴数字游戏")
        form2.setWindowIcon(QtGui.QIcon('Icon.jpg'))
        window_pale = QtGui.QPalette()
        pix = QtGui.QPixmap('tim.jpg')
        pix = pix.scaled(form2.width(), form2.height())
        window_pale.setBrush(form2.backgroundRole(), QtGui.QBrush(pix))
        form2.setPalette(window_pale)
        ui.label_2.setPixmap(QtGui.QPixmap('math.png'))
        form2.show()
        form2.exec_()

class CForm(QtWidgets.QWidget,complex.Ui_Dialog):
    #emit_list = QtCore.pyqtSignal(list)
    def __init__(self):
        super(CForm,self).__init__()
        self.setupUi(self)
        self.setFixedSize(700, 500)
        self.setWindowTitle("火柴数字游戏")
        self.setWindowIcon(QtGui.QIcon('Icon.jpg'))
        window_pale = QtGui.QPalette()
        pix = QtGui.QPixmap('tim.jpg')
        pix = pix.scaled(self.width(), self.height())
        window_pale.setBrush(self.backgroundRole(), QtGui.QBrush(pix))
        self.setPalette(window_pale)
        self.label.setPixmap(QtGui.QPixmap('math.png'))
        self.pushButton.clicked.connect(self.more_solve)
        self.label_2.setText("")
        self.label_2.setFont(QtGui.QFont("Roman times",15))

    def more_solve(self):
        try:
            word = self.lineEdit.text()
            temp = 0
            list = []
            for i in word:
                if (i != "=" and i != "+" and i != "-" and i != "×"):
                    temp = temp * 10 + int(i)
                else:
                    list.append(temp)
                    list.append(i)
                    temp = 0
            list.append(temp)
            list_display = []
            list_display_1 = []
            list_display_2 = []
            all_list_judge = []
            all_list_judge_1 = []
            all_list_judge_2 = []
            all_re = ""
            if (self.comboBox.currentText() == "移动一根火柴"):
                list_display, all_list_judge = Search_com(list)
            elif (self.comboBox.currentText() == "移动两根火柴"):
                list_display, all_list_judge = Searchcom_2(list)
            elif (self.comboBox.currentText() == "等式变新等式"):
                list_display_1, all_list_judge_1 = Search_com(list)
                list_display_2, all_list_judge_2 = Searchcom_2(list)
                for i in list_display_1:
                    if (i not in list_display):
                        list_display.append(i)
                for j in all_list_judge_1:
                    if (j not in all_list_judge):
                        all_list_judge.append(j)
                for i in list_display_2:
                    if (i not in list_display):
                        list_display.append(i)
                for j in all_list_judge_2:
                    if (j not in all_list_judge):
                        all_list_judge.append(j)
            if (list_display == []):
                QtWidgets.QMessageBox.about(self, "提示", "此式无解！")
            else:
                u = 0
                for i in list_display:
                    for j in i:
                        all_re = all_re + str(j)
                    u = u + 1
                    all_re = all_re + "     "
                    if (u % 2 == 0):
                        all_re = all_re + '\n'

                self.label_2.setText(all_re)
        except Exception as e:
            QtWidgets.QMessageBox.about(self, "警告", "请输入符合要求的算式！")

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    my_form = MYForm()
    my_form.show()
    C=CForm()
    my_form.setFixedSize(980,600)
    my_form.use_palette()
    my_form.more.clicked.connect(C.show)
    sys.exit(app.exec_())