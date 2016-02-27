__author__ = 'jiajiewang'


# 很数书叠加
def sumLogic(*value):
    sumValue = 0
    for n in value:
        sumValue = sumValue + n
    return sumValue


print('很多输叠加的结果', sumLogic(1, 2, 3, 4, 5))


def sumLogic2(*args):
    def addAll():
        sumValue2 = 0
        for k in args:
            sumValue2 = sumValue2 + k
        return sumValue2

    return addAll


result = sumLogic2(1, 2, 3, 4, 5)
print(result())

result2 = sumLogic2(1, 2, 3, 4, 5)

print(result == result2)


def wjj(z, x, c):
    a = 20

    def wjj2():
        return a*(z * x * c)

    return wjj2


k = wjj(2, 3, 4)
print(k())

def line_conf(a, b):
    def line(x):
        return a*x + b
    return line

line1 = line_conf(1, 1)
line2 = line_conf(4, 5)
print(line1(5), line2(5))
