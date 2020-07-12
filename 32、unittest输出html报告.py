import unittest,os,time,requests
from mathfunc import *
from  HtmlTestRunner import HTMLTestRunner
class TestMathFunc(unittest.TestCase):
    def test_add(self):
        self.assertEqual(3,add(1,2))
        self.assertNotEqual(3,add(3,2))

    def test_minus(self):
        self.assertEqual(3,minus(6,3))
        self.assertEqual(-2,minus(3,5))

    def test_multi(self):
        self.assertEqual(6,multi(3,2))
        self.assertEqual(0,multi(0,33))

    def test_divide(self):
        self.assertEqual(2,divide(6,3))
        self.assertEqual(2.5,divide(5,2))
'''
if __name__=='__main__':
    #filepath='C:/Users/zhangbinghui_v/PycharmProjects/zbh_python/python+selenium/unittestResultHTML.html'
    #dakai=open(filepath,'wb',encoding='utf-8')
    suite=unittest.TestSuite()   #实例化
    #加载用例
    
    suite.addTest(TestMathFunc('test_add'))
    suite.addTest(TestMathFunc('test_minus'))
    suite.addTest(TestMathFunc('test_multi'))
    suite.addTest(TestMathFunc('test_divide'))
    suite.addTest(TestMathFunc('test_dividel'))
    #2加载用例
    suite.addTests(unittest.TestLoader().loadTestsFromTestCase(TestMathFunc))
    #配置自动生产html测试报告
    now=time.strftime('%Y-%m-%d %H:%M:%S')
    print(now)
    #定义报告存放路径
    filename='D:/'+now+'relult.html'
    fp=open(filename,'wb')
    runner=HtmlTestRunner.HTMLTestRunner(stream=fp,
                                         report_title='welcome to this web!!')
    runner.run(suite)
    unittest.main()'''
#第二种方法
if __name__=='__main__':
    report_path="E:/zbh_python/python+selenium/0816test.html"
    fp=open(report_path,"wb")
    suite=unittest.TestSuite()
    suite.addTests(unittest.TestLoader().loadTestsFromTestCase(TestMathFunc))
    runner=HTMLTestRunner.HTMLTestRunner(stream=fp,title="0816 auto test html;")
    runner.run(suite)
    unittest.main()