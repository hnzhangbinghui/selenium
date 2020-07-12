# coding=utf-8
'''
Created on 2020-03-15
@author:zhangbinghui
'''
import unittest
import HTMLTestRunner
import requests
import time
from BeautifulReport import BeautifulReport


class Test(unittest.TestCase):
    def setUp(self):
        print('Test start...')
        self.resp = requests.get('https://www.baidu.com/')

    def tearDown(self):
        print('Test over.')

    # 定义测试用例，以“test_”开头命名的方法
    def test_open_baidu(self):
        self.assertEqual(self.resp.status_code, 200, msg='打开百度网页失败')

    def test_open_time(self):
        self.assertTrue(self.resp.elapsed.total_seconds(), msg='打开网页的时间')

    @unittest.skip('暂时跳过这个测试用例')
    def test_other(self):
        self.assertEqual(1, 3)


# #1、执行测试用例的第一种方法，unittest会搜索该模块下的所有以test开发的测试用例方法，并自动执行他们
# if __name__ == '__main__':
#     unittest.main()

# #2、执行用例第二种方法，用测试套件TestSuite的addTest方法逐个添加到套件中
# if __name__=='__main__':
#     suite = unittest.TestSuite()
#     suite.addTest(Test('test_open_baidu'))
#     suite.addTest(Test('test_open_time'))
#     suite.addTest(Test('test_other'))
#     f = open('open_baidu.html', 'wb')
#     runner = HTMLTestRunner.HTMLTestRunner(f, title='打开百度', description='打开百度测试unittest', verbosity=2)
#     runner.run(suite)

# #3、执行用例第三种方法，构造测试集（简化了2中的先创建测试套件在依次加载的测试用例）
if __name__=='__main__':
    now = time.strftime("%Y-%m-%d %H-%M-%S")
    print(now)
    test_path='D:\PycharmProjects\My_Book'
    discover=unittest.defaultTestLoader.discover(test_path,pattern='test_*.py')
    f = open(now+'open_baidu_discover.html', 'wb')
    runner = HTMLTestRunner.HTMLTestRunner(f, title='打开百度', description='打开百度测试unittest', verbosity=2)
    runner.run(discover)

# 4、生成更美的html报告BeautifulReport,
# 关于截图问题，现在很多HTMLTestRunner报告都支持失败自动截图，可惜BeautifulReport还只支持人工智能截图
# if __name__ == '__main__':
#     now = time.strftime("%Y-%m-%d %H-%M-%S")
#     print(now)
#     fn =now+'beautiful.html'
#     test_path = 'D:\PycharmProjects\My_Book'
#     discover = unittest.defaultTestLoader.discover(test_path, pattern='test_*.py')
#     result = BeautifulReport(discover)
#     result.report(filename=fn, description="更美的报告", log_path=globals())
