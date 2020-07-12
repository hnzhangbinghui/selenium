# coding=utf-8
import HTMLTestRunner
import os
import time
import unittest
import io

iost = io.StringIO


class MyTest(unittest.TestCase):  # 继承unittest.TestCase
    def tearDown(self):
        # 每个测试用例执行之后做操作
        print('teardown用例结束')

    def setUp(self):
        # 每个测试用例执行之前做操作
        print("setup用例开始执行")

    def test_run(self):
        # self.assertEqual(1,1)
        self.assertIs(1, 1, 't')
        # 测试用例

    def test_run2(self):
        # self.assertEqual(1,1)
        self.assertIs(1, 1, 't')  # 测试用例

    def test_run3(self):
        # self.assertEqual(1,1)
        self.assertIs(1, 1, 't')
        # 测试用例

    def test_run1(self):
        # self.assertEqual(1,1)
        self.assertIs(1, 1, 't')
        # 测试用例


if __name__ == '__main__':
    # 构建测试集
    suite = unittest.TestSuite()  # 实例化测试套件
    suite.addTest(MyTest("test_run"))
    suite.addTest(MyTest("test_run2"))
    now = time.strftime("%Y-%m-%d_%H:%:M:%S", time.localtime())
    print(now)
    filename='test_unittest.html'
    filepath=os.path.join(os.getcwd(),filename)
    print(filepath)
    with open(filepath, 'wb') as fp:
        runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title="测试结果", description="报告描述")
        runner.run(suite)
        fp.close()
