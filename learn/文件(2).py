# data=open("file.txt",encoding="utf-8").read()
# file=open("file.txt","w",encoding="gbk")
# data=file.read()
# data1=file.read()
# print(data)
# print("fjdksl",data1)
# file.write("00000000000000")
# data=file.read()
# print(data)


# file=open("file","w",encoding="utf-8")
# file.write("hfkdshfjdkshfjkds")

# file=open("file","a",encoding="utf-8")
# file.write("++++++++++++")

# file=open("file","r",encoding="utf-8")
# data=file.readlines()    #读取全部内容，以列表方式
# print(data)




# for index,line in enumerate(file.readlines()):
#     if index == 4:
#         continue
#     print(line.strip())

# for i in enumerate(file.readlines()):
#     print(i)


# file_list=file.readlines()
# Num_file=len(file_list)
#
# for i in range(Num_file):
#     if i == 4:
#         continue
#     print(file_list[i].strip())


# count=0
# for line in 冒泡排序:
#     if count==4:
#         count+=1
#         continue
#     print(line.strip())
#     count+=1
#
# file=open("file.txt","r",encoding="utf-8")
# file.readline()
# print(file.read(5))
#读取光标位置
# print(file.tell())
#
# file.read(10)
# print(file.tell())

#移动光标位置
# file.seek(0)
# print(file.tell())
# print(file.read())

#打印文件编码方式
# print(file.encoding)

#打印文件调用接口
# print(file.fileno())

#查看文件名
# print(file.name)

#判断文件光标是否可移动
# print(file.seekable())

#判断文件是否可读
# print(file.readable())

# import time,sys
#
# for i in range(20):
#     sys.stdout.write("#")
#     sys.stdout.flush()
#     time.sleep(0.3)



# data=file.read()
# print(data)
#
# file.close()

#文件截取
# f=file.truncate(10)
# file.write("++++++")

#读和追加的方式打开文件
# file=open("file.txt","r+",encoding="utf-8")
# print(file.read())
# file.write("-------")
# print(file.readline())

#写和读的方式打开文件(基本不用)
# file=open("file.txt","w+",encoding="utf-8")
# # file.write("999999")
# print(file.tell())
# print(file.read(3))

#以二进制方式读取
# file=open("file.txt","rb")
# print(file.readline())

#以二进制写入
# f=open("文件","wb")
# f.write("hello\nworld".encode())
# f.close()

#Python中建议一行最多不要超过80个字符
# with open("file.txt","r",encoding="utf-8") as f,\
#     open("file","r",encoding="utf-8") as f2:
#     print(f.readline())
#     print(f2.readline())