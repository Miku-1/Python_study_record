#参数组

#参数数目不固定
# def test(*args):
#     print(args)
#
# test(1,2,3)

# def test(x,*args):
#     print(x)
#     print(args)
#
# test(1,2)
# test(1,[1,2,3,4])


# def test(**kwargs):
#     print(kwargs["name"])
#     print(kwargs["age"])

# test({1:"1",2:"2"})
# test(name="feng",age=19)


# def test(x,age=19,**kwargs):
#     print(x)
#     print(age)
#     print(kwargs)
#
# test("feng",30,sex="Man")

def test(name,age=18,*args,**kwargs):
    print(name)
    print(age)
    print(args)
    print(kwargs)

test("feng",20,sex="Man",Last_name="ZZZ")

#参数组传入参数，以位置方式
#字典传入参数，以关键字方式

#参数为参数组，字典参数时，该参数必须放在函数后面。