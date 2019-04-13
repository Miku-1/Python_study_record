# name=["魏海丽","米刚","邵世超","赵莹","惠鑫婧",
#       "米刚","赵莹","惠鑫婧","邵世超"]
'''1、切片'''
# print(name[1],name[2])
# print(name[1:3])

# print(name[-1])
# print(name[4])
# print(name[-4:-1])

# print(name[0:])
# print(name[0::2])

'''2、列表插入'''
# name.append("郭倩")
# print(name)

# name1=["郭倩"]
# name=name+name1
# print(name)

# name.insert(2,"郭倩")
# print(name)

'''3、修改'''
# name[1]="郭倩"
# print(name)

'''4、删除'''
# name.remove("邵世超")
# print(name)
# name.remove(4)
# print(name)
#
# del name[2]
# print(name)
#
# s="fjdksl"
# s1=s
# del s
# print(s1)
# print(s)

#抛出
# a=name.pop(3)
# print(name)
# print(a)

'''5、查找元素'''
# '''n=[1,2,3,4,5,2,3,4,5]'''
# print(name.index("米刚"))
# print(name.index("米刚",2,-1))

'''6、输出元素个数'''
# print(name.count("赵莹"))

'''7、清除（清空）'''
# name.clear()
# print(name)

'''8、反转顺序'''
# name.reverse()
# print(name)


'''9、合并(添加)'''
# n=[5,6,7,8,9]
# name.extend(n)
# print(name)

# n=[["主菜单",[]],["设置",],["添加",],[]]
# n=["a","b","c","d","a","c","u","o","b","p","b"]
# n=["a","b","c","d","b"]
# n1=[]
# for i in n:
#     if i not in n1:
#         n1.append(i)
#         # print(n1)
#     else:
#         continue
# print(n1)

# n=[["主菜单",[4,3,2,1]],["退出",[]]]
# for i in range(1):
#     print("1、",n[0][0])
#     print("2、",n[1][0])
# print(n[0][1][0],n[0][1][1])

'''复制（浅拷贝）'''

# name1=["魏海丽","米刚","邵世超",["a","b"]]
# name2=name1.copy()
# # name2=name1
# print(name1)
# print(name2)
# name1[1]="++++++"
# print(name1)
# print(name2)
# print(id(name1))
# print(id(name2))
# n=[9999]
# name1=["魏海丽","米刚","邵世超",n]
# name2=name1.copy()
# name3=name1.copy()
# print(name1)
# print(name2)
# name1[-1][0]="000000"
# name1[0]="+++++"
# print(name1)
# print(name2)
# name1[-1][0]=name1[-1][0]-100
# print(name1[-1][0])
# print(name2[-1][0])

'''
	深拷贝
	递归复制
'''
import copy
name1=["魏海丽","米刚","邵世超",["a","b"]]
name2=copy.deepcopy(name1)
# name2=name1
# print(name2)



print(id(name1[-1]))
print(id(name2[-1]))
name1[-1][0]="))))"
# print(name1,'\n',name2)

