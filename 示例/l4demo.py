__author__ = 'Ezreal'
import os
# coding: utf-8

#递归章程
def Recursive(n):
    if n==1:
        return 1
    return n*Recursive(n-1)

print('第10行递归的结果等于',Recursive(5));


#尾递归方式
def fact_iter(num, product):
    if num == 1:
        return product
    return fact_iter(num - 1, num * product)

def fact(n):
    return fact_iter(n, 1)

print('第22行尾递归的结果等于',fact(5))

#打印出1,3,5,7...99
xInt=1
listA=[]
while xInt<=99:
    listA.append(xInt)
    xInt=xInt+2
print("第31行 list的len等于",len(listA),'list等于',listA)

#取出list中前X个项

nList=[]
flagK=4
for i in range(flagK):
    nList.append(listA[i])
print("第38行打印",nList)
#切片操作
print("第41行切片操作",listA[0:3])
print("第42行切片操作，取最后一个",listA[-1])
print("第43行切片操作，取倒数三个,左边元素不包括自己",listA[-4:-1])
print("第44行，用切片创建10位的list",list(range(10)))
print("第45行,前10个数，每两个取一个",listA[:10:2])
print("第46行每两个取一个",listA[::2])
print("第47行复制原来的集合",listA[::])

#使用在元组上
mTuple=(1,2,3,4,5,6,7,8,9,10)
print('第51行，元组切片',mTuple[2:10])
print("第52行，元组复制",mTuple[::])

##字符串的切片
print('第55行，切片HelloWorld，返回的也是字符串','helloworld'[2:6])

#迭代
#python中众多数据类型都可以迭代遍历，甚至是字符串
for value in "abcdefghi":
    print(value,end= " ")
print("第59行迭代了一个字符串")

#迭代一个dic
d={"a":1,"b":2,"1b":3}

for value1 in d:
    print(value1,end=" ")
print("第66行，迭代一个字典的key,但是是无序的哦")

for value2 in d.items():
    print(value2,end=" ")
print("第70行，迭代一个字典,但是是无序的哦")

from collections import Iterable
print("第74行判断对象是否能被迭代",isinstance('abc', Iterable))
print("第75行判断对象是否能被迭代",isinstance(False, Iterable))

for i, value in enumerate(['A', 'B', 'C']):
     print(i, value,end="   ")
print("第78行，显示下标需要调用enumerate函数")
#多项迭代
for x, y,z in [(1, 1, 3), (3,2, 4), (4,3, 9)]:
    print(x, y,z,end="     ")
print()
#列表生成表达式
print("第86行列表生成表达式",[x for x in range(20) if x%3==0])
print("第87行，多层循环",[m + n for m in 'ABCD' for n in 'XYZ'])
print("第89行循环读出同级目录内容",[d for d in os.listdir('.')])

for k1,k2 in d.items():
    print(k1,"   ",k2)
print("第91行 一个循环读2样东西")

d = {'x': 'A', 'y': 'B', 'z': 'C' }
print("第95行两个变量生成list",[k + '=' + v for k, v in d.items()])

mlist = ['Android', 'NIHAO', 'HAha', 'Apple']
print("所有元素变成小写",[s.lower() for s in mlist])

L = ['NIHAO', 'HAha', 118, 'Android', None]
print("第102行去数字去大写",[sa.lower() for sa in L if isinstance(sa, str)==True])

#打印金字塔
def printPyramid(level):
    for i in range(level):
        print( ' ' * (level-i-1) + '*' * (2*i+1))

printPyramid(4)


#斐波那契数列前n项和（sn = a1 + a2+...+ an) 递归
def aa(f):
    if f==0:
        return f
    elif f==1:
        return f
    else:
        return aa(f-1)+aa(f-2)

print(aa(11))


