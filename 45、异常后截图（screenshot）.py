'''在执行用例过程中由于是无人值守的，用例运行报错的时候，我们希望能对当前屏幕截图，留下证据。
在写用例的时候，最后一步是断言，可以把截图的动作放在断言这里，那么如何在断言失败后截图呢？'''
'''
截图方法：
1.get_screenshot_as_file(self, filename)
--这个方法是获取当前window的截图，出现IOError时候返回False,截图成功返回True。
filename参数是保存文件的路径。
Usage:
driver.get_screenshot_as_file('/Screenshots/foo.png')
2.get_screenshot_as_base64(self)
--这个方法也是获取屏幕截图，保存的是base64的编码格式，在HTML界面输出截图的时候，会用到。
比如，想把截图放到html测试报告里。
Usage:
driver.get_screenshot_as_base64()
3.get_screenshot_as_png(self)
--这个是获取屏幕截图，保存的是二进制数据，很少用到.
Usage:
driver.get_screenshot_as_png()
'''
'''二、异常后截图
1.为了能抛异常，把定位登录按钮的id换了个错的id。
2.给图片命名时候加个时间戳，避免同一个文件名称被覆盖掉。
3.文件路径，这里直接写的文件名称，就是跟当前的脚本同一个路径。如果图片输出到其它文件路径，需要些文件的绝对路径了。
4.截图的结果，如果没截到图返回False,截图成功会返回True。'''

#coding=utf-8
import time
from selenium import webdriver
import unittest
from selenium.webdriver.support import expected_conditions as EC

class Login(unittest.TestCase):
    def setUp(self):
        url="http://jgdj.hnsft.gov.cn:8088/sft/login"
        self.driver=webdriver.Firefox()
        self.driver.get(url)

    def test_denglu(self):
        try:
            self.driver.find_element_by_id('accountName').send_keys('15239687008')
            self.driver.find_element_by_id('password').send_keys('123')
            #密码错误，会抛出异常
            self.driver.find_element_by_class_name('button_blue').click()
            #判断登录成功页面是否有此账号
            time.sleep(5)
            self.driver.refresh()
            time.sleep(5)
            locator=('id','label-1017')
            result=EC.text_to_be_present_in_element(locator,'张冰辉1')(self.driver)
            self.assertTrue(result)
        except Exception as msg:
            print("异常原因%s" %msg)
            nowTime=time.strftime("%Y%m%d.%H.%M.%S")
            self.driver.get_screenshot_as_file('异常报错%s.jpg' %nowTime)
            raise
    def tearDown(self):
        self.driver.quit()
if __name__=='__main__':
    unittest.main()

























