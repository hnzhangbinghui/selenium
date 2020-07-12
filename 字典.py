#字典dictionary是一种映射结构的数据类型，由无序的键值对组成，字典的键必须是不可改变的类型，
#如字符串，数字，tuple；值可以是任何的python数据类型；具有极快的查询速度；

dict1={}
#增加字典的元素两种方法
#1
dict1['a']=1
print(dict1)
#2
dict1.setdefault('b',2)
print(dict1)
dict1.setdefault('c',3)
print(dict1)

print(dict1.get('d'))
#删除字典,也可以用pop方法
del dict1['b']
print(dict1)
aa=dict1.pop('a')
print(aa)
print(dict1)

#清空字典
dict1.clear()
print(dict1)

#字典的方法
#GET方法 get(key,default=None)
print(dict1.get('a'))

print(dict1.get('a','zhangbinghui'))

dict1.setdefault('a',123)
print(dict1)
print(dict1.get('a'))
#字典清空方法clear

#python3当中没有has_key()函数，被__contains__(key)替代
#有key则返回True，否则返回False

print(dict1.__contains__("a"))
print(dict1.__contains__('b'))

dict1.setdefault('b','33')
dict1.setdefault('c',445)
print(dict1)

#items方法返回键值对的一个列表
print(dict1.items())
#分别返回字段的键值列表
print(dict1.keys())
print(dict1.values())

#update(dict2)，把dict1的元素加入到dict2中，键字重复时会覆盖掉dict2中的键值；
dict2={}
print(dict2)
dict2.update(dict1)
print(dict2)

dict1.setdefault('d',11111)
print(dict1)
#修改字典的值
dict1['a']='beixiugai'
print(dict1)

dict2.update(dict1)
print(dict2)

#popitem方法，删除任意键值对，并返回该键值对，如果字典为空，则产生异常；
print("\n")
print(dict2)
jianzhi=dict2.popitem()
print(jianzhi)
print(dict2)
jianzhi=dict2.popitem()
print(jianzhi)
print(dict2)
jianzhi=dict2.popitem()
print(jianzhi)
print(dict2)

print('\n')
print(dict1)

#pop(key,[d]),删除指定键的键值对，并返回该键的值
print(dict1.pop('a'))

print(dict1.pop('aa',"没有此键的时候显示的值"))
print(dict1)
print(dict1.get('b'))
print(dict1['b'])


print('\n')
import time
now=time.strftime('%Y-%m-%d %H:%M:%S')
print(now)











