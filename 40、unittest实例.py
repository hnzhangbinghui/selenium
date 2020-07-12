#coding=utf-8
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
import time
import unittest

class BlogHome(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver=webdriver.Firefox()
        cls.driver.get("https://www.cnblogs.com/laozhangceshi/")
        cls.driver.implicitly_wait(30)
        print(cls.driver.title)
    #可以把打开浏览器操作放到前置setUpClass(cls)里，这样就可以实现打开一次浏览器，执行多个case

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    def test_01(self):
        locator=('id',"Header1_HeaderTitle")
        #text=15239687008
        text=str(15239687008)
        result=EC.text_to_be_present_in_element(locator,text)(self.driver)
        self.assertEqual(result,True)

    def test_02(self):
        locator1=('xpath',"/html/body/div[2]/div[5]/div[1]/div/div/div[2]/input[2]")
        text1='谷歌搜索'
        result1=EC.text_to_be_present_in_element_value(locator1,text1)(self.driver)
        self.assertEqual(result1,True)

    def test_03(self):
        result3=EC.title_contains("15239687008")(self.driver)
        self.assertTrue(result3)

if __name__=='__main__':
    unittest.main(verbosity=1)