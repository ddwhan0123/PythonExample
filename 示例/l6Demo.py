__author__ = 'jiajiewang'
# coding: utf-8
import os
from functools import reduce


# 把对象指向函数
print('最大值函数 :', max([1, 2, 3, 100, 20]));
maxValue = max;
print('对象指向函数 最大值为:', maxValue(10, 20))


# 把函数当做参数传入
c = abs


def testABS(a, b, c):
    return c(a) + b


print('测试函数结果:', testABS(-1, -9, c))


# map函数 把运算规则抽象
def testMAP(a):
    return a + a


print('返回的结果为:', list(map(testMAP, (1, 2, 3, 4, 5))))

listValue = []
for x in [1, 2, 3, 4, 5, ]:
    listValue.append(testMAP(x))
print('返回的结果为:', listValue)


def toString(a):
    return str(a)


print('转换为字符串:', list(map(toString, [1, 2, 3, 4])))


# 上一次计算结果为这一次参数的reduce方法
def absAll(a, b):
    return abs(a) + abs(b)


print('返回所有值的绝对值的和', reduce(absAll, (-1, 2, -3, -10, 1)))


# map reduce组合使用
def toInt(a):
    return int(a)


print('字符串转数字:', toInt("12"))
print('组合拳结果为:', reduce(absAll, list(map(toInt, ["1", "2", "3"]))))


def checkValue(a):
    return a - 5 > 0


print('判断是否>5', list(filter(checkValue, [1, 6, 9, 3])))
