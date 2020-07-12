'''登录这个场景在写用例的时候经常会有，我们可以把登录封装成一个方法，
然后把账号和密码参数化，这样以后用的登录的时候，只需调用这个方法就行了
'''

#coding=utf-8
from selenium import webdriver
import time
import unittest

class Blog(unittest.TestCase):
    def setUp(self):
        self.driver=webdriver.Firefox()
        url="https://passport.cnblogs.com/user/signin?ReturnUrl=https%3A%2F%2Fwww.cnblogs.com%2F"
        self.driver.get(url)
        self.driver.implicitly_wait(30)

    def login(self,username,pwd):
        self.driver.find_element_by_id('input1').send_keys(username)
        self.driver.find_element_by_id('input2').send_keys(pwd)
        self.driver.find_element_by_id('signin').click()
        time.sleep(3)
        self.driver.find_element_by_xpath('/html/body/div[1]/div/div/form/div[4]/div/div/div[2]/div[2]/div/div[2]/div[1]/div[3]/span[1]').click()

    def test_01(self):
        self.login('15239687008','zbh@911915')
        #调用is_login_success方法判断是否登录成功
        result=self.is_login_success()
        #设置断言，判断结果是否和预期一样
        self.assertTrue(result)

    def test_02(self):
        self.login('15239687008','zbh@911915')
        #调用is_login_success方法判断是否登录成功
        result=self.is_login_success()
        #设置断言，判断结果是否和预期一样
        self.assertTrue(result)

    def is_login_success(self):
        try:
            text=self.driver.find_element_by_partial_link_text('15239687008').text
            print(text)
            return True
        except:
            return False

    def tearDown(self):
        self.driver.quit()

if __name__=="__main__":
    unittest.main()











