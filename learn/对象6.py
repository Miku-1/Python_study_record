#类方法

# class Dog(object):
#     name="hu"
#     def __init__(self,name):
#         self.name=name
#     @classmethod
#     #类方法，调用的是类变量。
#     def eat(cx):
#         print("%s is eating %s" % (cx.name,"DD"))
#
# d=Dog("D1")
# d.eat()

#属性方法

class Dog(object):
    def __init__(self,name):
        self.name=name
    @property
    #将一个方法变成一个属性
    def eat(self):
        print("%s is eating %s" % (self.name,self.__food))

    @eat.setter
    def eat(self,food):
        self.__food=food
        # print("set to food:",food)

    @eat.deleter
    def eat(self):
        del self.__food
        print("删除完了")

d=Dog("D1")
d.eat="baozi"
d.eat
# del d.eat
# d.eat

'''
静态方法：
只是名义上归类管理，实际上在静态方法内部，
不能访问类或者类的实例的属性

类方法：
只能访问类变量，不能访问实例变量

属性方法：
把一个方法变成静态属性，对外隐藏内部实现细节。
'''