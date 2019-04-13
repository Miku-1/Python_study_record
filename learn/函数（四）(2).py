# Sum=0
# for i in range(10):
#     Sum+=i
#
# print(Sum)

def HH(n):    #10,5,2,1
    print(n)
    if int(n/2)>0:
        return HH(int(n/2))

HH(10)

# Sum=0
# def ADD(n):
#     global Sum
#     if n>0:
#         Sum+=n
#         return ADD(n-1)
#     print(Sum)
#
# ADD(10)