###字典
dict1 = {}
dict2 = {'name':'guoguo','age':4,'sex':'girl'}
##无序， 哈希算法， 键值对存储数据，python 中唯一的映射类型


###一切皆对象

# a = 10
# print(id(a))


###不可变类型： 整型，字典，元祖
###可变类型：
##字典创建，1,用工厂函数创建;2,
#工厂函数
#a = [1,2,3]
a= list((1,))
b = list([4])
print(a)
print(b)
##字典的操作：
dict4 = dict((('name','guoguo'),))
print(dict4)
dict4['hobby']='boy'
dict4.setdefault('age',12)

print(dict4)

##查找
print(dict4['name'])
print(dict4.keys())
print(list(dict4.keys()))
print(list(dict4.items()))
print(list(dict4.values()))
