from data import getdata
from judge_equality import judge,trans_single_list,trans_list_single


def Search(list):
    #将数字对应的变化情况存储为字典形式，（初始数字/符号，添加火柴根数，结果数字/符号）
    all_possibility = {0: [(0, 0, 6), (0, 0, 9), (0, 1, 8)],
                       1: [(1, 1, 7)],
                       2: [(2, 0, 3)],
                       3: [(3, 0 ,2), (3, 0, 5),(3, 1, 9)],
                       4: [],
                       5: [(5, 0, 3), (5, 1, 6), (5, 1, 9)],
                       6: [(6, 0, 0), (6, 0, 9), (6, 1, 8), (6, -1, 5)],
                       7: [(7, -1, 1)],
                       8: [(8, -1, 0),(8, -1, 6), (8, -1, 9)],
                       9: [(9, 0, 0), (9, 0, 6), (9, 1, 8), (9, -1, 5), (9, -1, 3)],
                       '+': [('+', 0, '='), ('+', -1, '-')],
                       '-': [('-', 1, '+'), ('-', 1, '=')],
                       '=': [('=', 0, '+'), ('=', -1, '-')],
                       '×': []}
    hard_par = 0
    all_list_judge=[]
    single=trans_list_single(list)
    list_display = []
    choice_1=[]
    choice_2=[]
    single_copy = single.copy()
    #自身移动一根使等式成立
    for i in single:
        for j in all_possibility[i]:
            if(j!=[] and j[1]==0):
                pos = get_pos(single,j[0])
                for k in pos:
                    single_copy[k]=j[2]
                    list_judge = trans_single_list(single_copy)
                    if(list_judge not in all_list_judge):
                        all_list_judge.append(list_judge)
                    if(judge(list_judge) and list_judge not in list_display):
                        list_display.append(list_judge)
                    single_copy = single.copy()
            elif(j!=[] and j[1]==1 and j not in choice_1):
                choice_1.append(j)
            elif(j!=[] and j[1]==-1 and j not in choice_2):
                choice_2.append(j)
    #某个数字加一根火柴，另一个数字减一根火柴
    list_display,all_list_judge = operate(single,choice_1,choice_2,list_display,all_list_judge)
    #print(all_list_judge)
    #print(len(all_list_judge))
    return list_display,all_list_judge

def Search_2(list):
    #将数字对应变化写成字典形式，（初始数字/符号，移动次数，添加火柴根数，结果数字）
    all_possibility = {0:[(0,1,0,6),(0,1,0,9),(0,0,1,8),(0,1,-1,2),(0,1,-1,5),(0,1,-1,3)],
                       1:[(1,0,1,7),(1,0,2,4)],
                       2:[(2,1,0,3),(2,2,0,5),(2,1,1,0),(2,1,1,9),(2,1,1,6),(2,0,2,8)],
                       3:[(3,1,0,2),(3,1,0,5),(3,0,1,9),(3,1,1,0),(3,1,1,6),(3,0,2,8),(3,1,-1,4),(3,0,-2,7)],
                       4:[(4,1,1,3),(4,1,1,5),(4,0,2,9),(4,0,-2,1),(4,1,-1,7)],
                       5:[(5,1,0,3),(5,2,0,2),(5,0,1,9),(5,0,1,6),(5,1,1,0),(5,0,2,8),(5,1,-1,4)],
                       6:[(6,1,0,0),(6,1,0,9),(6,0,1,8),(6,0,-1,5),(6,1,-1,2),(6,1,-1,3)],
                       7:[(7,0,-1,1),(7,1,1,4),(7,0,2,3)],
                       8:[(8,0,-1,0),(8,0,-2,2),(8,0,-2,3),(8,0,-2,5),(8,0,-1,6),(8,0,-1,9)],
                       9:[(9,1,0,0),(9,1,0,6),(9,0,1,8),(9,0,-1,3),(9,0,-2,4),(9,0,-1,5),(9,1,-1,2)],
                       '+':[('+',1,0,'='),('+',2,0,'×'),('+',0,-1,'-')],
                       '-':[('-',0,1,'+'),('-',0,1,'='),('-',1,1,'×')],
                       '=':[('=',1,0,'+'),('=',2,0,'×'),('=',0,-1,'-')],
                       '×':[('×',2,0,'='),('×',2,0,'+'),('×',1,-1,'-')]
                       }
    single = trans_list_single(list)
    single_copy = single.copy()
    list_display = []
    all_list_judge = []
    choice_1=[]
    choice_2=[]
    choice_3=[]
    choice_4=[]
    choice_5=[]
    choice_6=[]
    choice_7=[]

    list_search_1,list_search_1_judge_list = Search(list)
    #print("-----------------------------------------------------------------------------------------------------------")
    #自身移动两次火柴
    for i in single:
        for j in all_possibility[i]:
            if (j[1] == 2):
                pos = get_pos(single,j[0])
                for k in pos:
                    single_copy[k] = j[3]
                    list_judge = trans_single_list(single_copy)
                    if (list_judge not in all_list_judge):
                        all_list_judge.append(list_judge)
                    if (judge(list_judge) and list_judge not in list_display):
                        list_display.append(list_judge)
                    single_copy = single.copy()
            elif(j[2]==2 and j not in choice_1):
                choice_1.append(j)
            elif(j[2]==-2 and j not in choice_2):
                choice_2.append(j)
            elif(j[1]==0 and j[2]== 1 and j not in choice_3):
                choice_3.append(j)
            elif(j[1]==0 and j[2]==-1 and j not in choice_4):
                choice_4.append(j)
            elif(j[1]==1 and j[2]== 1 and j not in choice_5):
                choice_5.append(j)
            elif(j[1]==1 and j[2]==-1 and j not in choice_6):
                choice_6.append(j)
            elif(j[1]==1 and j[2]== 0 and j not in choice_7):
                choice_7.append(j)
    #建立得到七种情况的列表
    #某一个数字加两根，另一个数字减两根
    if (choice_1 != [] and choice_2 != []):
        list_display,all_list_judge = operate(single,choice_1,choice_2,list_display,all_list_judge)
    #print("----------------------------------------------------------------------------------------------------------------")
    #某一个数字加一根，另一个数字减一根再自身移动一次
    if (choice_3 != [] and choice_6 != []):
        list_display,all_list_judge = operate(single,choice_3,choice_6,list_display,all_list_judge)
    #print("----------------------------------------------------------------------------------------------------------------")
    #某一个数字减一根，另一个数字加一根再自身移动一次
    if (choice_4 != [] and choice_5 != []):
        list_display,all_list_judge = operate(single,choice_4,choice_5,list_display,all_list_judge)
    #print("--------------------------------------------------------------------------------------------------------------")
    #两个数字分别自身移动一根火柴
    if (choice_7 != []):
        for i in choice_7:
            pos_1 = get_pos(single,i[0])
            for j in choice_7:
                if (choice_7.index(i) <= choice_7.index(j)):    #index小于等于，即可得到所有的搭配方式，避免无谓的重复
                    pos_2 = get_pos(single, j[0])
                    for k in pos_1:
                        for t in pos_2:
                            if (k != t):
                                single_copy[k] = i[3]
                                single_copy[t] = j[3]
                                list_judge = trans_single_list(single_copy)
                                if (list_judge not in all_list_judge):
                                    all_list_judge.append(list_judge)
                                if (judge(list_judge) and list_judge not in list_display):
                                    list_display.append(list_judge)
                                single_copy = single.copy()
    #print("*******************************************************************************************************************")
    #两个数字分别减少一根火柴，第三个数字增加两根火柴
    if(choice_1!=[] and choice_4!=[]):
        for i in choice_1:
            pos_1 = get_pos(single,i[0])
            for j in choice_4:
                pos_2 = get_pos(single,j[0])
                for k in choice_4:
                    if (choice_4.index(j) <= choice_4.index(k)):
                        pos_3 = get_pos(single, k[0])
                        for w in pos_1:
                            for u in pos_2:
                                for v in pos_3:
                                    if (u != v and u != w and v != w):
                                        single_copy[w] = i[3]
                                        single_copy[u] = j[3]
                                        single_copy[v] = k[3]
                                        list_judge = trans_single_list(single_copy)
                                        if (list_judge not in all_list_judge):
                                            all_list_judge.append(list_judge)
                                        if (judge(list_judge) and list_judge not in list_display):
                                            list_display.append(list_judge)
                                        single_copy = single.copy()
    #两个数字分别增加一根火柴，第三个数字减少两根火柴
    if (choice_2 != [] and choice_3 != []):
        for i in choice_2:
            pos_1 = get_pos(single, i[0])
            for j in choice_3:
                pos_2 = get_pos(single, j[0])
                for k in choice_3:
                    if (choice_3.index(j) <= choice_3.index(k)):
                        pos_3 = get_pos(single, k[0])
                        for w in pos_1:
                            for u in pos_2:
                                for v in pos_3:
                                    if (u != v and u != w and v != w):
                                        single_copy[w] = i[3]
                                        single_copy[u] = j[3]
                                        single_copy[v] = k[3]
                                        list_judge = trans_single_list(single_copy)
                                        if (list_judge not in all_list_judge):
                                            all_list_judge.append(list_judge)
                                        if (judge(list_judge) and list_judge not in list_display):
                                            list_display.append(list_judge)
                                        single_copy = single.copy()
    #某个数字减少两根火柴，用以增加一位数字 1
    if(choice_2!=[] and len(single)!=8):
        flag = [0,0,0]
        if(list[0]>=10):
            flag[0] = 1
        if(list[2]>=10):
            flag[1] = 1
        if(list[4]>=10):
            flag[2] = 1
        for i in choice_2:
            pos = get_pos(single,i[0])
            for j in range(3):
                if(flag[j]==0):
                    for k in pos:
                        single_copy[k] = i[3]
                        list_judge = trans_single_list(single_copy)
                        list_judge[2 * j] = list_judge[2 * j] + 10   #在十位增加数字1
                        if (list_judge not in all_list_judge):
                            all_list_judge.append(list_judge)
                        if (judge(list_judge) and list_judge not in list_display):
                            list_display.append(list_judge)
                        list_judge = trans_single_list(single_copy)
                        list_judge[2 * j] = list_judge[2 * j] * 10 + 1   #在个位增加数字1
                        if (list_judge not in all_list_judge):
                            all_list_judge.append(list_judge)
                        if (judge(list_judge) and list_judge not in list_display):
                            list_display.append(list_judge)
                        single_copy = single.copy()
    #两个数字分别减少一根火柴，用以增加一位数字 1
    if(choice_4!=[] and len(single)!=8):
        flag = [0, 0, 0]
        if (list[0] >= 10):
            flag[0] = 1
        if (list[2] >= 10):
            flag[1] = 1
        if (list[4] >= 10):
            flag[2] = 1
        for i in choice_4:
            pos_1 = get_pos(single, i[0])
            for j in choice_4:
                if(choice_4.index(i)<=choice_4.index(j)):
                    pos_2 = get_pos(single, j[0])
                    for k in pos_1:
                        for u in pos_2:
                            if (k != u):
                                for t in range(3):
                                    if (flag[t] == 0):
                                        single_copy[k] = i[3]
                                        single_copy[u] = j[3]
                                        list_judge = trans_single_list(single_copy)
                                        list_judge[2 * t] = list_judge[2 * t] + 10    #在十位增加 1
                                        if (list_judge not in all_list_judge):
                                            all_list_judge.append(list_judge)
                                        if (judge(list_judge) and (list_judge not in list_display)):
                                            list_display.append(list_judge)
                                        list_judge = trans_single_list(single_copy)
                                        list_judge[2 * t] = list_judge[2 * t] * 10 + 1   #在个位增加 1
                                        if (list_judge not in all_list_judge):
                                            all_list_judge.append(list_judge)
                                        if (judge(list_judge) and list_judge not in list_display):
                                            list_display.append(list_judge)
                                        single_copy = single.copy()
    #某一个数字增加一根火柴，另一个数字减少一根火柴，对新的待处理等式进行Search操作，即再移动一根火柴，使得等式成立，并进行去重
    if (choice_3 != [] and choice_4 != []):
        for i in choice_3:
            pos_1 = get_pos(single, i[0])
            for j in choice_4:
                pos_2 = get_pos(single, j[0])
                for k in pos_1:
                    for t in pos_2:
                        if (k != t):
                            single_copy[k] = i[3]
                            single_copy[t] = j[3]
                            list_judge = trans_single_list(single_copy)
                            list_add,list_search_1_judge = Search(list_judge)
                            for u in list_search_1_judge:
                                if(u not in all_list_judge):
                                    all_list_judge.append(u)
                            for n in list_add:
                                if (n not in list_display and n not in list_search_1 and n!=list):
                                    list_display.append(n)
                            single_copy = single.copy()
    #print(all_list_judge)
    #print(len(all_list_judge))
    return list_display,all_list_judge

#操作函数，仅两个数字同时改变时调用
def operate(single,choice_first,choice_second,list_display,all_list_judge):
    single_copy = single.copy()
    for i in choice_first:
        pos_1=get_pos(single,i[0])
        #print(pos_1)
        for j in choice_second:
            pos_2 = get_pos(single, j[0])
            #print(pos_2)
            for k in pos_1:
                for t in pos_2:
                    if (k != t):
                        single_copy[k] = i[len(i) - 1]
                        single_copy[t] = j[len(j) - 1]
                        list_judge = trans_single_list(single_copy)
                        #print(list_judge)
                        if (list_judge not in all_list_judge):
                            all_list_judge.append(list_judge)
                        if (judge(list_judge) and list_judge not in list_display):
                            list_display.append(list_judge)
                        single_copy = single.copy()
    return list_display,all_list_judge

#定位函数，返回某数字在single列表中的全部位置
def get_pos(single,element):
    count = single.count(element)
    pos = []
    y = 0
    for p in range(count):
        list_tmp_1 = single[y:]
        y += list_tmp_1.index(element) + 1
        pos.append(y - 1)
    return pos

if __name__ == '__main__':
    list = [9,'-',5,'=',8]
    list_dis,list_jud=Search(list)
    print(list_dis)
    print(len(list_jud))
