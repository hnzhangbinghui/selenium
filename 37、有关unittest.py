'''熟悉java的应该都清楚常见的单元测试框架Junit和TestNG，这个招聘的需求上也是经常见到的。python里面也有单元测试框架-unittest,
相当于是一个python版的junit。
python里面的单元测试框架除了unittest,还有一个pytest框架'''

import unittest
class IntegerArithmeticTestCase(unittest.TestCase):
    '''def setUp(self):
        print("测试前的准备工作")
    def tearDown(self):
        print("测试后的收尾工作")
        这样写每次运行一个case都为启动一次前置和后置；
        '''
    @classmethod
    def setUpClass(cls):
        print("所有的case都启动一次前置工作\n")
    @classmethod
    def tearDownClass(cls):
        print("所有的cese都启动一次后置工作")

    def test1Add(self):  ## test method names begin 'test*' 测试用例的名称要以test开头
        self.assertEqual((1 + 2), 3)
        self.assertEqual(0 + 1, 1)
        print("第一个")

    def test2Multiply(self):
        self.assertEqual((0 * 10), 0)  #断言其实就是拿实际结果和期望结果去对比
        self.assertEqual((5 * 8), 40)
        print("第二个")

    def test3Minus(self):
        result=6-5
        hope=1
        self.assertEqual(result,hope)
        print("第三个")

    def test4Divide(self):
        result=7/2
        hope=3
        self.assertNotEqual(result,hope)
        print("第四个")

if __name__ == '__main__':
    unittest.main()












