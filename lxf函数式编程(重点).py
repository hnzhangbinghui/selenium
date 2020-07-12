#高阶函数,map和reduce函数
#map()函数，两个参数，一个函数，一个iterable，map讲interable的值传入函数，并把结果作为新的iterable返回
#Iterator是惰性序列，因此通过list()函数让它把整个序列都计算出来并返回一个list。
def f(x):
    return x*x
r=map(f,[1,2,3,4,5,6,7,8])
print(list(r))

a=[]
for n in [1,2,3,4,5,6,7,8]:
    a.append(f(n))
print(a)
#把list的所有数字转化为字符串
print(list(map(str,[1,2,3,4,5])))

#reduce把一个函数作用在一个序列[x1, x2, x3, ...]上，这个函数必须接收两个参数，reduce把结果继续和序列的下一个元素做累积计算，
from functools import reduce
def add(x,y):
    return x+y
print(reduce(add,range(100)))
#但是如果要把序列[1, 3, 5, 7, 9]变换成整数13579，reduce就可以派上用场：
from  functools import reduce
def fn(x,y):
    return x*10+y
print(reduce(fn,[1,3,5,7,9]))

#map和reduce的结合使用；
def char2num(s):
    digits = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}
    return digits[s]
print(reduce(fn,map(char2num,'13579')))

def normalize(name):
    return name.title()
L1 = ['adam', 'LISA', 'barT']
L2 = list(map(normalize, L1))
print(L2)

from functools import reduce


from functools import reduce
def prod(x,y):
    return x*y
a=reduce(prod,[3,5,7,9])
print(a)


#filter函数
#和map()类似，filter()也接收一个函数和一个序列。和map()不同的是，
#filter()把传入的函数依次作用于每个元素，然后根据返回值是True还是False决定保留还是丢弃该元素。
def is_odd(n):
    return n%2==0  #判断奇数偶数
print(list(filter(is_odd,[1,2,3,4,5,6,7,8,9])))

l=['zhang00','','bing','hui',None,'     ']
def not_empty(s):
    return s and s.strip()
print(list(filter(not_empty,l)))
#注意到filter()函数返回的是一个Iterator，也就是一个惰性序列，
# 所以要强迫filter()完成计算结果，需要用list()函数获得所有结果并返回list。

ss='zhangbinghui00000'
print(ss.strip('0'))


#利用filter求素数
def odd_iter():
    n=1
    while True:
        n=n+2    #从三开始的奇数列表
        yield n #是一个生成器，且是无线序列
def not_divisible(n):
    return lambda x:x%n>0
def primes():
    print(2)
    it=odd_iter() #初始序列
    while True:
        n=next(it)
        #返回序列第一个数
        yield n
        yield next(it)#打印n
        it=filter(not_divisible(n),it)  #构造新序列

for n in primes():
    if n<10:
        print(n)
    break



import math
def is_sqr(x):
    return  math.sqrt(x)%1==0
newlist=filter(is_sqr,range(1,101))
print(list(newlist))


#排序算法sorted
#排序也是在程序中经常用到的算法。无论使用冒泡排序还是快速排序，排序的核心是比较两个元素的大小。
# 如果是数字，我们可以直接比较，但如果是字符串或者两个dict呢？直接比较数学上的大小是没有意义的，
# 因此，比较的过程必须通过函数抽象出来。排序也是在程序中经常用到的算法。无论使用冒泡排序还是快速排序，
# 排序的核心是比较两个元素的大小。如果是数字，我们可以直接比较，但如果是字符串或者两个dict呢？
# 直接比较数学上的大小是没有意义的，因此，比较的过程必须通过函数抽象出来。

lb=[23,45,7,-23,-89,0]
print(sorted(lb))
print(sorted([23,45,7,-23,-89,0],key=abs))
lb.sort()
print(lb)

print(sorted(lb,key=lambda x:x*x))  #根据匿名函数排列

print(sorted(lb,reverse=True))  #降序排列
#字符串排序是大写A到Z,小写a到z的顺序进行排序；
print(sorted(['bob', 'about', 'Zoo', 'Credit']))
print(sorted(['Z','H','A','z','h','a']))

print(sorted(['Z','H','A','z','h','a'],key=str.lower,reverse=True))  #组合进行排序


#重点
L=[('Bob',75),('Adam',92),('Bart',66),('Lisa',88)]
def by_name(t):
    return t[1]
L2=sorted(L,key=by_name,reverse=True)
print(L2)



dic={'chen':24,'alex':34,'egon':37,'evaJ':18}
print(sorted(dic.keys()))  #根据键排序
print(sorted(dic.values())) #根据值排序
print(sorted(dic.items(),key=lambda x:x[1])) #根据键值排序整个字典


test_dict={'a':[1,'n'],'b':[7,'k','b'],
           'c':[5,'h1','h2','h3','h4','h5'],
           'd':[3,'dfg1','dfg2','df3'],
           'e':[4,'dfg1','dfg2','dfg3','dfg4'],
           'f':[2,'dfgl','dfg2'],
           'g':[6,'f1','f2'],
           }

print(sorted(test_dict.items(),reverse=False,key=lambda x:x[1][0]))


#返回函数，高阶函数除了可以接受函数作为参数外，还可以把函数作为结果值返回。
def calc_sum(*args): #可变参数,个数不固定
    ax=0
    for n in args:
        ax=ax+n
    return ax
print(calc_sum(10,33,44,5,6,7,7))



#如果不需要立刻求和，而是在后面的代码中，根据需要再计算怎么办？可以不返回求和的结果，而是返回求和的函数：
def lazy_sum(*args):
    def sum():
        ax=0
        for n in args:
            ax=ax+n
        return ax
    return sum

f=lazy_sum(1,3,5,7,9)
print(f())


def count():
    fs=[]
    for i in range(1,4):
        def f():
            return i*i
        fs.append(f)
    return fs
ff=count()


#匿名函数
print(list(map(lambda x:x*x,[1,2,3,4,5,6,7,8,9])))
#两者可以划等号
def f(x):
    return x*x
print(list(map(f,[1,2,3,4,5,6,7,8,9])))

#装饰器
#由于函数也是一个对象，而且函数对象可以被赋值给变量，所以，通过变量也能调用该函数
print('\n')
def now(x):
    return x+x
f=now
print(f(5))
print(f.__name__)  #得到函数的名字
print(now.__name__)

#能打印日志的decorator函数
def log(now):
    def wrapper(*args,**kw):
        print('call %s():'%now.__name__)
        return now(*args,**kw)
    return wrapper

print('\n')
@log
def now():
    print('jiayou ,qin')

print(now())

#偏函数
print(int('12345'))
print(int('12345',8))
#转化为二进制
def int2(x,base=2):
    return int(x,base)

print(int2('1000000'))
#functools.partial就是帮助我们创建一个偏函数的，不需要我们自己定义int2()，可以直接使用下面的代码创建一个新的函数int2：
#简单总结functools.partial的作用就是，把一个函数的某些参数给固定住（也就是设置默认值），返回一个新的函数，调用这个新函数会更简单。
import functools
int10=functools.partial(int,base=10)
print(int10('12345'))























