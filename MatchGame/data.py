import random
import os
def getdata():
    #移动一根火柴的等式库
    all_equality = ["3+5=74", "8-7=7", "33-76=11", "1+8=1", "19-10=6","7×5=83","4+6=4","18-6=9","61-53=38","9-5=8","6-8=5",
                    "1+5=2","19-3=6","5-8=7","6+6=6","7+6=1","2-3=1","9+5=0","9-4=7","2+66=8"]
    if(os.path.isfile("data_1.txt")):
        with open("data_1.txt", "r") as fr:
            for line in fr:
                if (line.rstrip('\n') not in all_equality):
                    all_equality.append(line.rstrip('\n'))
    i = random.randint(0, len(all_equality) - 1)
    equality = all_equality[i]
    temp = 0
    list =[] #list是五个元素  [数字，符号，数字，符号，数字]
    #single = [] #single是将每一部分的数字拆开的列表
    for i in equality:
        if (i != "=" and i != "+" and i != "-" and i!="×"):
            temp = temp * 10 + int(i)
        else:
            list.append(temp)
            list.append(i)
            temp = 0

    list.append(temp)
    return list

def getdata_2():
    #移动两根火柴的等式库
    all_equality = ["8+8=15","9-5=0","4×9=46","3×8=73","6+1=18","27-33=24","6-6=8","9=2-17","16-12=98","2+9=4",
                    "30+19=39","91-15=79","9+5=8","4+2=28","8+8=1"]
    if (os.path.isfile("data_2.txt")):
        with open("data_2.txt", "r") as fr:
            for line in fr:
                if (line.rstrip('\n') not in all_equality):
                    all_equality.append(line.rstrip('\n'))
    i = random.randint(0, len(all_equality) - 1)
    equality = all_equality[i]
    temp = 0
    list = []  # list是五个元素
    # single = [] #single是将每一部分的数字拆开的列表
    for i in equality:
        if (i != "=" and i != "+" and i != "-" and i != "×"):
            temp = temp * 10 + int(i)
        else:
            list.append(temp)
            list.append(i)
            temp = 0
    list.append(temp)
    return list

def getdata_3():
    #移动一根火柴的等式库
    all_equality = ["6+9=15","7+3=10","17+15=32","4×18=72","5=2+3","19=13+6","6+0=6","41+5=46","15+6=21","21+4=25"]
    if (os.path.isfile("data_3.txt")):
        with open("data_3.txt", "r") as fr:
            for line in fr:
                if (line.rstrip('\n') not in all_equality):
                    all_equality.append(line.rstrip('\n'))
    i = random.randint(0, len(all_equality) - 1)
    equality = all_equality[i]
    temp = 0
    list =[] #list是五个元素  [数字，符号，数字，符号，数字]
    #single = [] #single是将每一部分的数字拆开的列表
    for i in equality:
        if (i != "=" and i != "+" and i != "-" and i!="×"):
            temp = temp * 10 + int(i)
        else:
            list.append(temp)
            list.append(i)
            temp = 0

    list.append(temp)
    return list

if __name__ == '__main__':
   getdata_2()
