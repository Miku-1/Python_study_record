#私有属性/方法
class Park:
    def __init__(self,name,age=20):
        self.name=name
        self.__age=age

    def __show(self):
        print("age 为 %s" % self.__age)

p=Park("feng",19)
print(p.name)
# print(p.age)
# p.show()
print(p._Park__age)
p._Park__age=30
p._Park__show()