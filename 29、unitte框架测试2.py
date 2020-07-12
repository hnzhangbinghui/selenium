#https://blog.csdn.net/xiaoquantouer/article/details/75089200
'''一、什么是单元测试
单元测试是用来对一个模块、一个函数或者一个类来进行正确性检验的测试工作。
比如对于函数abs()，我们可以编写的测试用例为：
（1）输入正数，比如1、1.2、0.99，期待返回值与输入相同
（2）输入复数，比如-1、-1.2、-0.99，期待返回值与输入相反
（3）输入0，期待返回0
（4）输入非数值类型，比如None、[]、{}、期待抛出TypeError'''
'''unittest工作原理
unittest中最核心的四部分是：TestCase，TestSuite，TestRunner，TestFixture
（1）一个TestCase的实例就是一个测试用例。测试用例就是指一个完整的测试流程，包括测试前准备环境的搭建（setUp），
执行测试代码（run），以及测试后环境的还原（tearDown）。元测试（unit test）的本质也就在这里，
一个测试用例是一个完整的测试单元，通过运行这个测试单元，可以对某一个问题进行验证。
（2）而多个测试用例集合在一起，就是TestSuite，而且TestSuite也可以嵌套TestSuite。
（3）TestLoader是用来加载TestCase到TestSuite中的。
（4）TextTestRunner是来执行测试用例的，其中的run(test)会执行TestSuite/TestCase中的run(result)方法
（5）测试的结果会保存到TextTestResult实例中，包括运行了多少测试用例，成功了多少，失败了多少等信息。
综上，整个流程就是首先要写好TestCase，然后由TestLoader加载TestCase到TestSuite，
然后由TextTestRunner来运行TestSuite，运行的结果保存在TextTestResult中，整个过程集成在unittest.main模块中。
'''

import unittest
from mydict import Dict

class TestDict(unittest.TestCase):

    def test_init(self):
        d=Dict(a=1,b='test')
        self.assertEqual(d.a,1) #判断d.a是否等于1
        self.assertEqual(d.b,'test') #判断d.b是否等于test
        self.assertTrue(isinstance(d,dict)) #判断d是否是dict类型

    def test_key(self):
        d=Dict()
        d['key']='value'
        self.assertEqual(d.key,'value')

    def test_attr(self):
        d=Dict()
        d.key='value'
        self.assertTrue('key' in d)
        self.assertEqual(d['key'],'value')

    def test_keyerror(self):
        d=Dict()
        with self.assertRaises(KeyError): #通过['empty']访问不存在的key时，断言会抛出keyerror
            value=d['empty']

    def test_attrerror(self):
        d=Dict()
        with self.assertRaises(AttributeError): #通过d.empty访问不存在的key时，我们期待抛出AttributeError（这个错误就是说python找不到对应的对象的属性）
            value=d.empty

if __name__=='__main__':
    unittest.main()

