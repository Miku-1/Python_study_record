# class People(object):
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
#
# class Relation(object):
#     def __init__(self,n1,n2):
#         print("in the relation")
#
#     def make_f(self,obj):
#         print("%s with %s" % (self.name,obj.name))
#
#
# class Man(Relation,People):
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
#
#     def sleep(self):
#         print("+++++++in the Man_S"
#               "leep %s" % self.name)
#
# class Wonman(Relation,People):
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
#
#     def sleep(self):
#         print("+++++++in the Man_S"
#               "leep %s" % self.name)
#
# m1=Man("M1",22)
# W1=Wonman("W1",21)
# m1.make_f(W1)

#
#
#
#
#





# class A:
#     def __init__(self):
#         print("A")
# class B(A):
#     pass
# class C(A):
#     pass
# class D(B,C):
#     pass
#
# obj=D()

# class School(object):
#     def __init__(self,name,addr):
#         self.name=name
#         self.addr=addr
#         self.students=[]
#         self.emps=[]
#     def student(self,stu_obj):
#         print("为学员%s办理注册手续" % stu_obj.name)
#         self.students.append(stu_obj)
#
#     def teach(self,tea_obj):
#         print("雇佣新员工：%s" % tea_obj.name)
#         self.emps.append(tea_obj)
#
# class Member(object):
#     def __init__(self,name,age,sex):
#         self.name=name
#         self.age=age
#         self.sex=sex
#
# class Teacher(Member):
#     def __init__(self,name,age,sex,salary,course):
#         super(Teacher, self).__init__(name,age,sex)
#         self.salary=salary
#         self.course=course
#
#     def tell(self):
#         print('''
#         ---info of Teacher:%s---
#         Name:%s
#         Age:%s
#         Sex:%s
#         Salary:%s
#         Course:%s
#         ''' % (self.name,self.name,self.age,self.sex,
#                self.salary,self.course))
#     def teach(self):
#         print("%s is teaching course [%s]" % (self.name,self.course))
#
# class Student(Member):
#     def __init__(self,name,age,sex,stu_id,grade):
#         super(Student, self).__init__(name,age,sex)
#         self.stu_id=stu_id
#         self.grade=grade
#
#     def tell(self):
#         print('''
#         ---info of Teacher:%s---
#         Name:%s
#         Age:%s
#         Sex:%s
#         Stu_id:%s
#         Grade:%s
#         ''' % (self.name,self.name,self.age,self.sex,
#                self.stu_id,self.grade))
#     def pay_money(self,money):
#         print("%s has paid money for $ %s" % (self.name,money))
#
# school=School("飞凡","陕理工校区")
#
# t1=Teacher("曹老师",29,"M",10000,"IOS")
#
# t2=Teacher("罗老师",28,"W",10000,".NET")
#
# s1=Student("米刚",19,"M",1000,"python")
#
# s2=Student("魏海丽",20,"W",1001,"python+java")
#
# t1.tell()
# t2.tell()
# school.teach(t1)
# school.student(s1)
# school.student(s2)
# print(school.students)
# print(school.emps)
#
# school.emps[0].teach()
#
# for stu in school.students:
#     stu.pay_money(5000)





