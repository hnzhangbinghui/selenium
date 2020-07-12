#!/usr/bin/env python3
#-*-coding:utf-8-*—
'模块文档注释'
_author_='zhang'  #引入作者
#导入sys模块后，我们就有了变量sys指向该模块，利用sys这个变量，就可以访问sys模块的所有功能。
import sys
def test():
    args=sys.argv
    if len(args)==1:
        print('hello,world!!')
    elif len(args)==2:
        print('hello,%s' %args[1])
    else:
        print('too many arguments')
if __name__=='_main__':   #Python解释器把一个特殊变量__name__置为__main__
    test()
































#作用域
'''正常的函数和变量名是公开的（public），可以被直接引用，比如：abc，x123，PI等；
类似__xxx__这样的变量是特殊变量，可以被直接引用，但是有特殊用途，比如上面的__author__，__name__就是特殊变量，
hello模块定义的文档注释也可以用特殊变量__doc__访问，我们自己的变量一般不要用这种变量名；
类似_xxx和__xxx这样的函数或变量就是非公开的（private），不应该被直接引用，比如_abc，__abc等；'''
def _private1(name):
    return 'hello,%s' %name
def __private2(name):
    return 'hello,%s' %name
def greeting(name):
    if len(name)>3:
        return _private1(name)
    else:
        return __private2(name)

print(greeting('zhangbinghui'))

'''我们在模块里公开greeting()函数，而把内部逻辑用private函数隐藏起来了，
这样，调用greeting()函数不用关心内部的private函数细节，这也是一种非常有用的代码封装和抽象的方法，即：
外部不需要引用的函数全部定义成private，只有外部需要引用的函数才定义为public。'''











