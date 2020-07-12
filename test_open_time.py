import unittest
import requests

class Test(unittest.TestCase):
    def setUp(self):
        print('Test start...')
        self.resp = requests.get('https://www.baidu.com/')

    def tearDown(self):
        print('Test over.')
    def test_open_time(self):
        self.assertTrue(self.resp.elapsed.total_seconds(), msg='打开网页的时间')

