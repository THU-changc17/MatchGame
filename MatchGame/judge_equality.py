#将list转化为single格式
def trans_list_single(list):
    single=[]
    temp1 = 0
    temp2 = 0
    for i in list:
        if (i != "=" and i != "+" and i != "-" and i != "×" and i>=10):
                temp1 = int(i/10)
                temp2 = int(i%10)
                single.append(temp1)
                single.append(temp2)
        else:
                single.append(i)
    return single
#将single转化为list格式
def trans_single_list(single):
    temp = 0
    list = []
    for i in single:
        if (i != "=" and i != "+" and i != "-" and i != "×"):
            temp = temp * 10 + i
        else:
            list.append(temp)
            list.append(i)
            temp = 0
    list.append(temp)
    return list
#判断等式是否成立
def judge(list):
    if(list[1]=='+' and list[3]=='='):
        if(list[0]+list[2]==list[4]):
            return True
    elif(list[1]=='-' and list[3]=='='):
        if (list[0] - list[2] == list[4]):
            return True
    elif (list[1] == '×' and list[3] == '='):
        if (list[0] * list[2] == list[4]):
            return True
    elif (list[1] == '=' and list[3] == '+'):
        if (list[2] + list[4]==list[0]):
            return True
    elif (list[1] == '=' and list[3] == '-'):
        if (list[2] - list[4] == list[0]):
            return True
    elif (list[1] == '=' and list[3] == '='):
        if (list[2] == list[4] and list[4] == list[0]):
            return True
    else:
        return False



