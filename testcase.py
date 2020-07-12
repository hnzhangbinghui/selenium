import unittest,os,time
from mathfunc import *
import HtmlTestRunner

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

    def test_divide1(self):
        try:
            divide(6,0)
            if b==0:
                return False
        except:
            return True

if __name__=='__main__':
    print('__name__')
    unittest.main(verbosity=2)
    print("unittest自动化测试")


