import unittest
import requests

class Test(unittest.TestCase):
    def setUp(self):
        print('Test start...')
        self.resp = requests.get('https://www.baidu.com/')

    def tearDown(self):
        print('Test over.')

    # 定义测试用例，以“test_”开头命名的方法
    def test_open_baidu(self):
        self.assertEqual(self.resp.status_code, 2090, msg='打开百度网页失败')
