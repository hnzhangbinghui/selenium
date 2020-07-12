"""
map() 会根据提供的函数对指定序列做映射。
第一个参数 function 以参数序列中的每一个元素调用 function 函数，
返回包含每次 function 函数返回值的新列表。
"""
#map(function, iterable, ...)
"""
function -- 函数
iterable -- 一个或多个序列
这种情况是因为在python3里面，map()的返回值已经不再是list,
而是iterators, 所以想要使用，只用将iterator 转换成list 即可，
比如 list(map()) 。
"""
def f(x):
    return x**2
list1=list(map(f,[1,2,3,4]))
print(list1)
#lambda是匿名函数
list2=list(map(lambda x:x**2 ,[1,2,3,4]))
print(list2)
"""reduce() 函数会对参数序列中元素进行累积。

函数将一个数据集合（链表，元组等）中的所有数据进行下列操作：
用传给 reduce 中的函数 function（有两个参数）先对集合中的第
 1、2 个元素进行操作，得到的结果再与第三个数据用 function 函数运算
 ，最后得到一个结果。"""
from functools import reduce
def add(x,y):
    return x+y
print(reduce(add,[1,2,3,4,5]))
print(reduce(lambda x,y:x+y,[1,2,3,4,5]))

"""filter() 函数用于过滤序列，过滤掉不符合条件的元素，
返回一个迭代器对象，如果要转换为列表，可以使用 list() 来转换。
该接收两个参数，第一个为函数，第二个为序列，
序列的每个元素作为参数传递给函数进行判，然后返回 True 或 False，
最后将返回 True 的元素放到新列表中。"""

def is_odd(n):
    return n%2==1
tmplist=filter(is_odd,[1,2,3,4,5,6,7,8,9])
newlist=list(tmplist)
print(newlist)

#过滤1-100平方根是整数的数
import math
def is_sqr(x):
    return math.sqrt(x)%1==0
tmplist=filter(is_sqr,range(1,101,3))
newlist=list(tmplist)
print(newlist)


"""python range() 函数可创建一个整数列表，一般用在 for 循环中。
range(start, stop[, step])
start: 计数从 start 开始。默认是从 0 开始。例如range（5）等价于range（0， 5）;
stop: 计数到 stop 结束，但不包括 stop。例如：range（0， 5） 是[0, 1, 2, 3, 4]没有5
step：步长，默认为1。例如：range（0， 5） 等价于 range(0, 5, 1)
"""
"""zip() 函数用于将可迭代的对象作为参数，将对象中对应的元素打包成一个个元组，
然后返回由这些元组组成的列表。
如果各个迭代器的元素个数不一致，
则返回列表长度与最短的对象相同，利用 * 号操作符，
可以将元组解压为列表。"""

a=[1,2,3]
b=[4,5,6]
c=[4,5,6,7,8,9]
aa=[]
for each in zip(a,b):
    print(each)
    aa.append(each)
print(aa)
bb=[]
for each in zip(a,c):
    print(each)
    bb.append(each)
print(bb)

"""round()函数返回浮点型参数x四舍五入后小数位保留n位的值。"""
print(round(3.12345,4))
print(round(3.15745,2))


#给一个值的赋值比较长时，用小括号来显示；
s=("fdajlfjdsalfds"
   "fdsafdsafdsafdsafdsafd")
print(s)





















