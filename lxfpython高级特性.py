#一、切片
list1=['Michael', 'Sarah', 'Tracy', 'Bob', 'Jack']
print(list1)
print(list1[:])  #[:]可以看做是原样列表的复制
print(list1[:3])
print(list1[2:])
l=list(range(11))
print(l)

#每5个取一个数
print(l[::5])

#元祖切片
yuanzu=(1,2,3,4,5)
print(yuanzu[:])
print(yuanzu[:2])
print(yuanzu[::2])

#字符串切片
zfc='zhangbinghui'
print(zfc[:])
print(zfc[:5])
print(zfc[::3])

zz='  zhangbing  '
print(zz.strip())

#二、迭代
#字典迭代key，或者value，因为dict的存储不是按照list的方式顺序排列，所以，迭代出的结果顺序很可能不一样。
d={'a':1,'b':'zhagnbingh','c':'hello'}
print(d)
for key in d.keys():
    print(key)
#迭代value
for value in d.values():
    print(value)

#迭代key，value
for x,y in d.items():
    print(x,y)

#迭代字符串
aaa='zhangbinghui'
for a in aaa:
    print(a)

#判断一个对象是否是可迭代对象，方法是通过collections模块的iterable类型判断
#还可以被next()函数不断调用并返回下一个值，直到最后抛出StopIteration错误表示无法继续返回下一个值了。
#可以被next()函数调用并不断返回下一个值的对象称为迭代器：Iterator。
from collections import Iterable
#判断一个对象是否是iterator,可迭代的
print(isinstance([1,2,3],Iterable))
print(isinstance(123,Iterable))

#判断一个对象是否是迭代生成器
print(isinstance([],Iterable))



#三，列表生成式
l=list(range(1,11))
print(l)

#但如果要生成[1x1, 2x2, 3x3, ..., 10x10]
ll=[]
for x in range(1,11):
    ll.append(x*x)

print(ll)
#列表生成式可以用一条语句代替循环生产
print([y*y for y in range(1,11)])

print([y*y for y in range(1,11) if y%2==0])
#双层循环
print([x+y for x in 'ABC' for y in 'abc'])

#for循环可以同时使用两个甚至多个变量
d={'x': 'A', 'y': 'B', 'z': 'C' }
for k,v in d.items():
    print(k,'=',v)

#生成器，只要把一个列表生成式的[]改成()，就创建了一个generator：
#通过next（）函数获得genetator的下一个值；

ll=[x*x for x in range(10)]
print(ll)
gg=(x*x for x in range(10))
print(gg)
print(next(gg))
print(next(gg))
for n in gg:
    print(n)
#这就是定义generator的另一种方法。如果一个函数定义中包含yield关键字，那么这个函数就不再是一个普通函数，而是一个generator：


ls=[1,2,3,4]
#把一个列表转化为迭代生成器
lss=iter(ls)
print(lss)
print(next(lss))
















