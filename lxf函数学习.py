def my_abs(x):
    if x>0:
        return x
    else:
        return -x
print(my_abs(99))

#空函数，什么事情都不做，可以用pass语句
#实际上pass可以用作来占位符，以后想用的时候在用，不会报错；
def kong(x):
    if x>22:
        pass
    else:
        pass


#位置参数,power(x, n)函数有两个参数：x和n，这两个参数都是位置参数，调用函数时，传入的两个值按照位置顺序依次赋给参数x和n。
def power(x,n):
    s=1
    while n>0:
        n=n-1
        s=s*x
    return s
print(power(2,64))

#可变参数，要定义出这个函数，我们必须确定输入的参数。由于参数个数不确定，我们首先想到可以把a，b，c……作为一个list或tuple传进来
#还可以用*参数，来表示可变参数
def calc(numbers):
    sum=0
    for n in numbers:
        sum=sum+n*n
    return sum

print(calc([1,2,3,4,5]))
print(calc((1,2,3,4,5)))

def calc1(*numbers1):
    sum1=0
    for n in numbers1:
        sum1=sum1+n*n
    return sum1
print(calc1(1,2,3,4,5))

#关键字参数，可以上传0个或者任意个含参数名参数，这些关键字参数在函数内部自动组装为一个dict；

def person(name,age,**kw):
    print('name:',name,'age:',age,'other:',kw)

print(person('zhang',22,city='beijing'))
print(person('li',33,tizhong='56',job='test'))
#**extra表示把extra这个dict的所有key-value用关键字参数传入到函数的**kw参数，
#kw将获得一个dict，注意kw获得的dict是extra的一份拷贝，对kw的改动不会影响到函数外的extra。
extra = {'city': 'Beijing', 'job': 'Engineer'}
print(person('zhang',33,**extra))

#命名关键字参数
def people(name,age,*,city,job):
    print(name,age,city,job)
print(people('张冰辉-',22,city='-北京-',job='软件测试工程师'))

#如果函数定义中已经有了一个可变参数，后面跟着的命名关键字参数就不再需要一个特殊的分隔符*了；
#命名关键字参数必须传入参数名，这和位置参数不同，如果没有传入参数名，会报错；
#命名关键字参数可以传入默认值，调用时就不需要在传对应的值；
#使用命名关键字参数时，要特别注意，如果没有可变参数，就必须加一个*作为特殊分隔符。如果缺少*，Python解释器将无法识别位置参数和命名关键字参数



#参数组合，各种参数类型可以组合使用，必须注意顺序是：必选参数，默认参数，可变参数，命名关键字参数和关键字参数；

#递归函数(在函数内部调用自身本身)
def fact(n):
    if n==1:
        return 1
    else:
        return n*fact(n-1)
print(fact(5))
print(fact(10))
#递归函数优点，简单，逻辑清晰，理论上所有的递归函数都可以写成循环的方式，但是循环的逻辑不如递归清晰；

#尾递归,尾递归是指，在函数返回的时候，调用自身本身，并且，return语句不能包含表达式。
#这样，编译器或者解释器就可以把尾递归做优化，使递归本身无论调用多少次，都只占用一个栈帧，不会出现栈溢出的情况。
#尾递归调用时，如果做了优化，栈不会增长，因此，无论多少次调用也不会导致栈溢出。
def fact_iter(num,product):
    if num==1:
        return product
    else:
        return fact_iter(num-1,num*product)
print(fact_iter(5,1))





