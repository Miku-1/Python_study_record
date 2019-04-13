# '''
# 一种接口，多种实现
# '''
#
# class Animal:
#     def __init__(self,name):
#         self.name=name
#
#     def talk(self):
#         pass
#
#     @staticmethod
#     def animal_talk(obj):
#         obj.talk()
#
# class Cat(Animal):
#     def talk(self):
#         print("in the Cat")
#
# class Dog(Animal):
#     def talk(self):
#         print("in the Dog")
#
# d=Dog("d1")
# c=Cat("c1")
# Animal.animal_talk(d)
# Animal.animal_talk(c)


'''
静态方法
'''

class Dog(object):
    def __init__(self,name):
        self.name=name

    @staticmethod
    def eat(self,food):
        print("%s is eating %s" % (self.name,food))

d=Dog("d1")
d.eat("包子")

'''
静态方法，只是名义上归类去管理，
但是实际上在静态方法里访问不了
类或者实例中的任何属性。
'''


