# info={1:2,3:4,5:6}
# f=open("test","w")
# f.write(str(info))
# f.close()

# f=open("test","r")
# data=f.read()
# f.close()
# print(data[3])

#标准序列化
# import json
# info={"name":"slg","age":19}
# f=open("test","w")
# f.write(json.dumps(info))
# f.close()

#通用型序列化方式，用于不同语言间的数据交互

#标准反序列化
# import json
# f=open("test","r")
# data=json.loads(f.read())
# f.close()
# print(data["age"])

# import json
#
# def sayhi(name):
#     print("hello %s" % name)
#
# info={
#     "name":"slg",
#     "age":19,
#     "func":sayhi
# }
#
# f=open("test","w")
# f.write(json.dumps(info))
# f.close()
#


'''Python特有pickle方式序列化'''

import pickle

def sayhi(name):
    print("hello %s" % name)

info={
    "name":"slg",
    "age":19,
    "func":sayhi
}

f=open("test","wb")
# f.write(pickle.dumps(info))
pickle.dump(info,f)
f.close()

import pickle
def sayhi(name):
    print(name)

f=open("test","rb")
# data=pickle.loads(f.read())
data=pickle.load(f)
print(data["func"]("feng"))
#            sayhi("feng")