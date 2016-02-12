__author__ = 'jiajiewang'

# 排序
list = [1, 3, -1, 8, 9]
print('排序前', list, '基础排序后', sorted(list))

print('按照绝对值排序', sorted(list, key=abs))

people = [('Wjj1', 'A', 99), ('Wjj2', 'B', 100), ('Wjj3', 'C', 45), ('Wjj4', 'D', 75), ]

print('符合对象排序  成绩 : ',sorted(people,key=lambda person:person[2]))
print('符合对象排序 等级 : ',sorted(people,key=lambda person:person[1]))

daXie = "Wo de ming Zi Jiao Wjj"
print('拆分字符串', sorted(daXie.split(), key=str.lower))

daXie = "WO SHI Wjj"
print('大写字变小写 : ', daXie.lower())

xiaoXie = 'wo shi Wjj'
print('小写变大写 : ', xiaoXie.upper())

print('大小写互换 : ', xiaoXie.swapcase(), '    ', daXie.swapcase())

print('首字母大写', xiaoXie.title())

print('左对齐 : ', daXie.ljust(15, "a"))

print('右缩进 : ', daXie.rjust(15, 'b'))

print('居中处理 : ', xiaoXie.center(15, 'c'))

print('填充处理 : ', daXie.zfill(15))

print('去掉两边的空格 : ', '           abc  cc  dd        '.strip())

print('去掉左边空格 : ', '           abc  cc  dd        '.lstrip())

print('去掉右边的空格 : ', '           abc  cc  dd        '.rstrip())
