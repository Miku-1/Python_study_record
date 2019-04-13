'''
列表：[]
元组：()
字典：{}
集合：{}
集合是无序的

集合中的元素是唯一的
集合可用来做关系测试
'''

#1、唯一性测试
# List=[1,2,3,4,3,2,1,5,6,7,8]
# List1=set(List)
# print(List1)

#2、关系测试(取交集)
# List2={7,6,5,4}
# List2=[7,6,5,4]
# print(List1.intersection(List2))

#3、取并集
# print(List1.union(List2))

#4、取差集(去掉1中存在，而2中不存在的元素)
# print(List1.difference(List2))

#5、判断子集
# print(List2.issubset(List1))

#6、判断父集
# print(List1.issuperset(List2))

#7、取对称差集(会去掉1和2中都存在的元素)
# print(List1.symmetric_difference(List2))

#8、判断是否没有共同元素
# print(List2.isdisjoint({0,10}))

#9、交集
# print(List1 & List2)

#10、并集
# print(List1 | List2)

#11、差集
# print(List1 - List2)

#12、对称差集
# print(List1 ^ List2)

#13、添加元素
# List=[1,2,3,4,3,2,1,5,6,7,8]
# List1=set(List)

# List1.add(99999)
# print(List1)

# List1.update([99,999])
# print(List1)

#14、删除数据
# Set={1,2,3,4,5}
# Set.remove(5)
# print(Set)

# print(Set.pop())

# Set.discard(4)
# print(Set)



