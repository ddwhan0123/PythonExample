__author__ = 'jiajiewang'


def add(x):
    return x + x


print(add(2))

v = lambda x: x + x
print(v(2))

list = lambda x=3: x + 3

print('3为默认值', list(), list(5))
list1 = lambda x: x + 3
print('无默认值', list1(1))

# 像变量一样的匿名函数

v1 = lambda: 123
print('无参数匿名函数', v1())

# 传入多个参数的匿名函数,但是这种模式不支持多个参数有默认值

list2 = lambda z, x, c=3: z + x + c
print('传入多个参数的匿名函数', list2(1, 2, 5))
