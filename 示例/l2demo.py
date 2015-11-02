__author__ = 'Ezreal'
# coding: utf-8

#列表长度
list=['a',123,'ssa:s']
print('第6行',len(list))
#可以顺序添加
list.append(1)
print('第9行',list)
#可以从中插入
list.insert(0,'sqca')
print('第12行',list)
#删除最后一个元素
list.pop()
print("第15行删除最后一个元素",list)
#删除指定元素
list.pop(0)
print('第18行 删除制定元素',list)
#元素置换
list[1]="王亟亟"
print("第21行元素置换",list)

#利用元组的好处，安全
#如何定义只有一个元素的元祖
myTuple=('aa',)
print('第26行打印只有一个元素的元组',myTuple)
#如何让元组可变？
a=[33,44]
pp="你好"
changeTuple=(a,2,3,pp)
print(changeTuple)
pp="你好啊"
print(changeTuple)
changeTuple[0][0]=55
changeTuple[0][1]=66
#变了是因为元素中列表的指针发生了变化，元组只是指向了那个元素的地址
print(changeTuple)
#普通的逻辑判断
flag=True
if flag==True:
    print('第41行if判断',flag)
else:
    print('第43行 if判断',flag)

age=10
if age<10:
    print(age,"<10  第47行if判断")
elif age<20:
    print(age,"<20  第49行elif判断")
else:
    print("年纪奇怪 第51行 else判断")

#根据输入判断
s=input("请输入内容")
if int(s)>10:
    print("输入内容大于10")
else:
    print("输入内容不对")

#循环
#遍历列表
names = ['aa', 'bb', 'cc',11]
for name in names:
    print(name)

sum = 0
for x in range(101):
    sum = sum + x
print(sum)

sum = 0
n = 100
while n > 0:
    sum = sum + n
    n = n - 1
print(sum)

#跳出循环体
edibles = ["ham", "spam","eggs","nuts"]
for food in edibles:
    if food == "spam":
        print("No more spam please!")
        break
    print("Great, delicious " + food)
else:
    print("I am so glad: No spam!")
print("Finally, I finished stuffing myself")
#生成整数序列
for i in range(5):
     print(i,end=' ')
print()
#按照指定范围以及大小值进行生成
for i in range(0, 13, 2) :
    print(i,end=' ')
print()

for k in range(1,10):
    for j in range (1,1+k):
        print(j,"*",k,"=",j*k,end="  ")
    print(end="\n")