# S="fdsfdsjkds.com"
# S1="HHHJJKGGYVCJ"
#1、首字母大写
# print(S.capitalize())

#2、计数
# print(S.count("f"))

#3、整个字符串大写变小写
# print(S1.casefold())

#4、居中操作
# print(S.center(50,"+"))

#5、格式转换
# S.encode(encoding="utf-8")
# S.encode(encoding="GBK")
# print(S.encode(encoding="utf-8"))

#6、判断结尾
# print(S.endswith(".jpg"))

#7、查找
# print(S.find("f" ))

#8.1格式化操作
# name="{name} is {age}"
# print(name)
# print(name.format(name="feng",age=19))
#8.2
# print(name.format_map({"name":"feng","age":"19"}))
#8.3
#该字符串操作，填入的参数是元组
# print("%s is " % "feng")
# print("%s is " % ("feng"))
# print("%s is %s" % ("feng",73821))
# print("%s is %d" % ("feng",73821))
# print("%s is %d" % "feng",73821)     #默认追加一个参数
# print("%s is %d" % ("feng","jfdks"))   #错误

#9、判断是否由数字组成
# S="342nuds"
# print(S.isalnum())
#10、判断是否由字母组成(包含大小写)
# S="fdsfdsjkdscomDDDD"
# print(S.isalpha())
#11、判断是否是十进制数
# S="73281"
# S="1A"
# print(S.isdecimal())
#12、判断是不是整数
# S="8493.2"
# print(S.isdigit())
#13、判断是不是一个合法的标识符
# S="00__fjdsk"
# print(S.isidentifier())
#14、判断是不是小写
# S="jfdksSSS"
# print(S.islower())
#15、判断是不是数字
# S="8989--"
# print(S.isnumeric())
#16、判断是不是空格
# S="  "
# print(S.isspace())
#17、判断字符串中每一个单词是不是大写开头
# S="Gfs djfkds"
# print(S.istitle())
#18、判断字符串能不能打印（用途较少）
# S="fjkds"
# print(S.isprintable())
#19、判断是不是大写
# S="IIOJfdsfdsH"
# print(S.isupper())
#20、join格式化
# print("+".join(["1","2","3"]))
#21.1、向左格式化打印
# S="jfkdlsjfkds"
# print(S.ljust(30,"+"))
#21.2、向右格式化打印
# print(S.rjust(30,"+"))
#22、大写变小写
# S="JKHJKHJK"
# print(S.lower())
#23、小写变大写
# S="jfkds"
# print(S.upper())
#24.1、去掉左边空格和回车
# S="\njfkdsj"
# print(S)
# print(S.lstrip())
#24.2、去掉右边空格和回车
# S="fdks\n"
# print(S+"jfkdsl")
# print(S.rstrip()+"jfkdls")
#24.3、去掉两端全部空格和回车
# S="\nfhdsj\t"
# print(S.strip()+"jfdksncue")

#25、自定义格式化(形成对照表),,,两字符串长度必须一致
# p=str.maketrans("1234267","abcdefg")
# print("5372".translate(p))

#26、字符串替换
# s="bubunimovyisa"
# print(s.replace("b","B",3))

#27、从右向左查找
# s="jfkdlssfds"
# print(s.rfind("s"))

#28、字符串分割
s="bcudsncusiabjdf"
l=s.split("s")
# l.append("feng")
print(l)
# print(" ".join(l))
s=s.replace("s"," ")+" feng" #查找和替换
print(s)

#29、识别换行(主要针对于全部系统)
# s="1\n+2\n"
# print(s)
# print(s.split("\n"))
# print(s.splitlines())

#30、将字符串中的大小写互换
# s="HUbfjds"
# print(s.swapcase())

#31、将字符串中的每一个单词首字母变大写
# s="feng oo pbce"
# print(s.title())

#32、格式化操作
# s="10"
# print(s.zfill(8))

'''字符串不允许修改'''
# s="fengnaifds"
# l=[1,2,3,4]
# print("列表修改前：",id(l))
# l.append("fiwe")
# print("列表修改后：",id(l))
# print("字符串修改前：",id(s))
# s=s+"jfi"
# print("字符串修改后：",id(s))