import unittest
import requests

class Test(unittest.TestCase):
    def setUp(self):
        print('Test start...')
        self.resp = requests.get('https://www.baidu.com/')

    def tearDown(self):
        print('Test over.')
    @unittest.skip('暂时跳过这个测试用例')
    def test_other(self):
        self.assertEqual(1,3,msg='比对结果失败')