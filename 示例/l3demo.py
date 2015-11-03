__author__ = 'Ezreal'
# coding: utf-8

#dictionary索引
dic={'wjj':185,'wmm':175}
print('第6行检索dictionary',dic['wjj'])
#判断某个key是否存在
print('第8行，判断某个key是否在字典里','wdd' in dic)
#也可以使用get的方法，并且可以指定返回值
print('第10行，如果没get到就返回自己赋予的值',dic.get('wj1j',3))
print('第11行，如果没get到就返回None',dic.get('wj1j'))
#添加某个键值对
dic.setdefault('wgg',102)
#移除某个键值对
dic.pop('wmm')
print('第16行移除wmm后的效果',dic)

#创建set
sets=set([1,1,1,3,6,3])
print('第20行 创建set,重复部分会被去除',sets)
#添加元素,无序的
sets.add('12')
print('第23行',sets)
#删除某个元素,不是下标而是它本身的key
sets.remove(1)
print('第26行',sets)

#函数
print('第29行 打印最大值',max(1,21,2,3))
print('第30行 绝对值',abs(-10),abs(100))
print('第31行 遍历是否都为真',all([True,True,True]),all([True,False,True]),all([3>2,True,True]))
print('第31行 遍历部分是否为真',any([True,True,True]),any([True,False,True]),any([3>2,True,True]))

#类型转换,bool 除了0 别的都是 True
print('第35 打印字符串转数字',int('123'))
print('第36 各种类型转换',str(100)+'你好',float('10.34'),int(17.3124), bool(-100))

#函数的概念
a = max # 变量a指向abs函数
# 所以也可以通过a调用abs函数
print('第41行 函数赋值',a(-1,2,3))

#自定义函数
def strToInt(str):
    intValue=int(str)
    return intValue
print('第47行 打印有返回值的自定义函数',strToInt('10086'))

#没有返回值的函数
intVBal=1
def intToBool(intVBal):
    print('第52行转数据类型',bool(intVBal))

intToBool(intVBal)
print('第55行 显示返回值',intToBool(intVBal))

def my_abs(x):
    if not isinstance(x, (int, float)):
        raise TypeError('bad operand type')
    if x >= 0:
        return x
    else:
        return -x
print(my_abs(123))

#返回多个值
def reMoreVal(x,y):
    return x,y

print('第70行 返回多个值',reMoreVal(1,'a'))

#有默认值的函数
def printInfo( name, age = 35 ):
    print("Name: ", name)
    print("Age ", age)
    return

#调用printinfo函数
printInfo( age=50, name="miki" )
printInfo( name="miki" )

#不定长参数
def printMore(value,*more):
    print(value)
    for val in more:
        print(val,end=' ')
    print()
    return
printMore('aaa',1,2,3)

#匿名函数
addAll=lambda arg1,arg2,arg3:arg1+arg2+arg3
print('第93行打印他们的合',addAll(2,3,4))

