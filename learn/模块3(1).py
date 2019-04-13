# import random

# print(int(random.random()*100))

# print(random.randint(1,2))

# print(random.randrange(1,5))

# print(random.choice(["a","b","c","d"]))

# print(random.sample("jfkdsjf",2))

# print(random.uniform(1,4))

# l=[3,4,2,8,9]
# random.shuffle(l)
# print(l)


import os
#获取本程序操作目录 E:\飞凡\PythonTest\陕理工
# print(os.getcwd())

#切换当前目录
# os.chdir(r"c:")
# os.chdir(r"E:/飞凡/PythonTest/陕理工")
# print(os.getcwd())

#返回当前目录
# print(os.curdir)
# print(os.pardir)

# os.makedirs(r'c:\a/b/c')

# os.removedirs(r"c:/a/b/c")

# os.mkdir(r"c:\a\c")

# os.rmdir()

# print(os.listdir(".."))

# os.remove("file.txt")

# os.rename(r"c:\a\a.txt",r"c:\a\adsadsa.txt")

# print(os.stat(r"test2.py"))

# print(os.sep)   #win--\,\\   Linux--/

# print(os.linesep)

# print(os.pathsep)

# print(os.environ)

# print(os.name)    #posix

# os.system("dir")

# print(os.path.dirname(__file__))

# print(os.path.isfile())

# os.path.isdir()

# os.path.isabs()

# print(os.path.join(r"c:",r"\a.txt"))


print(os.path.getatime("test2.py"))