'''
    冒泡排序
    1,对相邻的两个数字比较。如果第一个比第二个大，就交换他们两个。
    2,从头开始对每一对相邻元素做同样的工作，最后的元素就是最大的数
    3,针对所有的元素重复以上的步骤，除了最后一个。
    4,持续每次对越来越少的元素重复上面的步骤，直到没有任何一对数字需要比较。
'''

def bubble(arr):
    # i控制循环次数
    for i in range(len(arr) - 1):
        # j控制每次循环中的比较次数
        for j in range(len(arr) - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr
# if __name__ == '__main__':
#     arr = [1, 3, 4, 7, 8, 11, 9, 2]
#     print(bubble(arr))


'''
    归并排序    
'''
# 合并序列
def merge(left, right):
    a = 0
    b = 0
    c = []
    while a < len(left) and b < len(right):
        if left[a] < right[b]:
            c.append(left[a])
            a += 1
        else:
            c.append(right[b])
            b += 1
    if a == len(left):
        for i in right[b:]:
            c.append(i)
    else:
        for i in left[a:]:
            c.append(i)
    return c

# 划分序列
def merge_sort(arr):
    if len(arr) == 1:
        return arr
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    return merge(left, right)

# if __name__ == '__main__':
#     arr = [1, 3, 4, 7, 8, 11, 9, 2]
#     print(merge_sort(arr))
list1 = [1,2,3]
list2 = [3,4,5]
set1 = set(list1)
set2 = set(list2)
print(set1 & set2)
print(set1 ^ set2)
print(set1 | set2)
print(set1 and set2)
print(set1 or set2)

Str = 'ahdiu'
