#
# class People(object):
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
#
#     def eat(self):
#         print("%s is eating" % self.name)
#
#     def talk(self):
#         print("%s is talking" % self.name)
#
#     def sleep(self):
#         print("in the People_Sleep %s" % self.name)
#
# class Man(People):
#     def __init__(self,name,age,money):
#         People.__init__(self,name,age)    #深度优先
#         # super(Man,self).__init__(name,age) #广度优先
#         self.money=money
#
#     def sleep(self):
#         People.sleep(m1)
#         print("+++++++in the Man_S"
#               "leep %s" % self.name)
#
# class Women(People):
#     pass
#
# m1=Man("feng",19,3000)
# m1.sleep()

# l=[1,2,3,4]
# l.reverse()
# print(l)