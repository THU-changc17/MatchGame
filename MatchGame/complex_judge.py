import re
#正则表达式处理部分参考https://www.cnblogs.com/Faker006/articles/7211577.html
brac    = re.compile(r"\([^()]+\)")
mul     = re.compile(r"(\d+\.?\d*\×-\d+\.?\d*)|(\d+\.?\d*\×\d+\.?\d*)")
add     = re.compile(r"(-?\d+\.?\d*\+-\d+\.?\d*)|(-?\d+\.?\d*\+\d+\.?\d*)")
sub     = re.compile(r"(-?\d+\.?\d*--\d+\.?\d*)|(-?\d+\.?\d*-\d+\.?\d*)")
flag    = re.compile(r"\(?\+?-?\d+\.?\d*\)?")

def Mul(s):
    exp = re.split(r'\×',mul.search(s).group())
    return s.replace(mul.search(s).group(),str(int(exp[0])*int(exp[1])))
def Add(s):
    exp = re.split(r'\+',add.search(s).group())
    return s.replace(add.search(s).group(),str(int(exp[0])+int(exp[1])))
def Sub(s):
    exp = sub.search(s).group()
    if exp.startswith('-'):
        exp = exp.replace('-', '+')
        res = Add(exp).replace('+', '-')
    else:
        exp = re.split(r'-',exp)
        res = str(int(exp[0]) - int(exp[1]))
    return s.replace(sub.search(s).group(),res)

def solve(s):
        s = s.strip()
        s = ''.join([x for x in re.split('\s+', s)])
        if not s.startswith('('):
            s = str('(%s)' % s)
        while brac.search(s):
            s = s.replace('--', '+')
            s_search = brac.search(s).group()
            if mul.search(s_search):  # 判断是否包含乘法运算
                s = s.replace(s_search, Mul(s_search))
            elif sub.search(s_search):  # 判断是否包含减法运算
                s = s.replace(s_search, Sub(s_search))
            elif add.search(s_search):  # 判断是否加法运算
                s = s.replace(s_search, Add(s_search))
            elif flag.search(s_search):  # 加减乘除都不含，判断是否有括号
                s=s.replace('(','').replace(')','')

        return s

def judge(list):
    list_copy=list.copy()
    all_s=[]
    s=""
    if('=' not in list_copy):
        return False
    for i in list_copy:
        if(i!="="):
            s=s+str(i)
        elif(s!=""):
            all_s.append(s)
            s=""
    all_s.append(s)
    result=[]
    for j in all_s:
        solve(j)
        result.append(solve(j))
    length=len(set(result))
    if(length>1):
        return False
    else:
        return True


if __name__ == "__main__":
   s=[3,'×',6,'-',5,'+',9,'=',22,'=',11,'+',11]
   print(judge(s))
   print(solve("0+4-9×5"))