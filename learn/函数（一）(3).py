


'''
1、增强代码重用性
2、保持一致性
3、可拓展性增强

'''


def test(x):
    '''该函数是学到的第一个函数，执行参数加1的操作，
    最终得到的结果是参数执行加法运算的结果
    '''
    x+=1
    return x

# test(999)
print(test(2222))
# x=1
# def func1(x):
#     '''func1'''
#     x+=1
#     print("in the func1")
#     return x

# def func2(x):
#     '''jfdskl'''
#     print("in the func2")
#     x+=1

# func1(x)
# print(func1(x))
# print(func2(x))
import time
#
def logger():
    time_formt="%Y-%m-%d %x"
    time_current=time.strftime(time_formt)
    print(time_current)
#
def test1():
    print("in the test1")
    Start_time=time.time()
    logger()
    print(time.time()-Start_time)
    return "jfkds"
#
# def test2():
#     print("in the test2")
#     logger()
#
# def test3():
#     print("in the test3")
#     logger()
#
# print(test1())


def test(x,y):   #x,y:形式参数---形参（不占内存）
    print(x)
    print(y)
#
# test(1,2)        #1,2:实际参数---实参（占用实际内存）

#x,y这两个参数，又叫做位置参数  (个数，位置)


# test(y=9,x=8)
#位置参数调用：必须与形参一一对应
#关键字参数调用：与形参位置没有关系

#关键字参数不能写在位置参数之前
# test(x=2,6)    #错误
# test(3,y=9)
# test(9,x=5)    #错误

#默认参数：调用函数时，默认参数非必需传递
# def test(x,y=0):
#     print(x)
#     print(y)

# test(2,3)
# test(2)

# def Add(x,y):
#     return x+y
#
# def Sub(x,y):
#     return x-y
#
# def Mul(x,y):
#     return x*y
#
# def Dev(x,y):
#     return x/y

# Str=input("请输入计算公式：")
# if "+" in Str:
#     print(Add(int(Str.split("+")[0]),
#               int(Str.split("+")[1])))
# elif "-" in Str:
#     print(Sub(int(Str.split("-")[0]),
#               int(Str.split("-")[1])))
# elif "x" in Str:
#     print(Mul(int(Str.split("x")[0]),
#               int(Str.split("x")[1])))
# elif "/" in Str:
#     print(Dev(int(Str.split("/")[0]),
#               int(Str.split("/")[1])))



# s="7777832178392+96674399"
# N=int(s.split("+")[0])+int(s.split("+")[1])
# print(N)


# Str=input("请输入计算公式：")
# if "+" in Str:
#     print((int(Str.split("+")[0])+
#               int(Str.split("+")[1])))
# elif "-" in Str:
#     print((int(Str.split("-")[0])-
#               int(Str.split("-")[1])))
# elif "x" in Str:
#     print((int(Str.split("x")[0])*
#               int(Str.split("x")[1])))
# elif "/" in Str:
#     print((int(Str.split("/")[0])/
#               int(Str.split("/")[1])))

# M="7*2+1"    #[7*2,1]
# N="7-2*1"    #[7,2*1]
# N1=N.split("*")[1]   #2-1
# N2=N1.split("-")     #['2', '1']
# print(int(N.split("*")[0])*int(N2[0])
#       -int(N2[1]))
# if "-" in M:
#     L1=M.split("+")
#     if "*" in L1[0]:
#         pass
#     elif "/" in L1[0]:
#         pass
#     elif "+" in L1[0]:
#         pass
# elif "+" in M:
#     L2=M.split("+")
#     if "*" in L2[0]:
#         print(L2[0].split("*")[0])
#         print(L2[0].split("*")[1])
#         print(int(L2[0].split("*")[0])*
#               int(L2[0].split("*")[1]))
#     elif "/" in L2[0]:
#         print(int(L2[0].split("/")[0])/
#               int(L2[0].split("/")[1]))
#     elif "-" in L2[0]:
#         print(int(L2[0].split("-")[0])-
#               int(L2[0].split("-")[1]))


def Sstr(Str):
    if "+" in Str:
        return Str.split("+")[0],\
               Str.split("+")[1]
    elif "-" in Str:
        return Str.split("-")[0],\
               Str.split("-")[1]
    elif "x" in Str:
        return Str.split("x")[0],\
               Str.split("x")[1]
    elif "/" in Str:
        return Str.split("/")[0],\
               Str.split("/")[1]

M="7x2+1"    #[7*2,1]
N="7-2*1"
if "-" in M:
    L1=M.split("+")
    if "x" in L1[0]:
        pass
    elif "/" in L1[0]:
        pass
    elif "+" in L1[0]:
        pass
elif "+" in M:
    print(Sstr(M))
    print(Sstr(M)[0])
    if "x" in Sstr(M)[0]:
        print(int(Sstr(Sstr(M)[0])[0])*
              int(Sstr(Sstr(M)[0])[1]))
    elif "/" in Sstr(M)[0]:
        pass
    elif "-" in Sstr(M)[0]:
        pass



# M="7*2+1"    #[7*2,1]
# N="7-2*1"
# if "-" in M:
#     L1=M.split("+")
#     if "*" in L1[0]:
#         pass
#     elif "/" in L1[0]:
#         pass
#     elif "+" in L1[0]:
#         pass
# elif "+" in M:
#     L2=M.split("+")
#     if "*" in L2[0]:
#         print(L2[0].split("*")[0])
#         print(L2[0].split("*")[1])
#         print(int(L2[0].split("*")[0])*
#               int(L2[0].split("*")[1]))
#     elif "/" in L2[0]:
#         print(int(L2[0].split("/")[0])/
#               int(L2[0].split("/")[1]))
#     elif "-" in L2[0]:
#         print(int(L2[0].split("-")[0])-
#               int(L2[0].split("-")[1]))