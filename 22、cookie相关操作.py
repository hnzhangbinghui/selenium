'''虽然cookie相关操作在平常ui自动化中用得少，偶尔也会用到，
1、比如登录有图形验证码，可以通过绕过验证码方式，添加cookie方法登录。
2、登录后换账号登录时候，也可作为后置条件去删除cookie然后下个账号登录'''

'''1.获取cookies方法直接用：get_cookies()
2.先启动浏览器，获取cookies，打印出来发现是空：[]
3.打开博客首页后，重新获取cookies,打印出来，就有值了'''



#coding=utf-8
from selenium import webdriver
import time
driver=webdriver.Firefox()
#启动浏览器后获取cookies
print(driver.get_cookies())
driver=webdriver.Firefox()
driver.get("http://www.cnblogs.com/")
driver.find_element_by_link_text("登录").click()
driver.find_element_by_id('input1').send_keys('15239687008')
driver.find_element_by_id('input2').send_keys('zbh@911915')
driver.find_element_by_id('remember_me').click()

time.sleep(5)
driver.find_element_by_id('signin').click()

time.sleep(5)
#打开主页后获取cookies
print(driver.get_cookies())
driver.refresh()
time.sleep(5)
#获取cookie当中name的值
print(driver.get_cookie(name='.CNBlogsCookie'))
#清楚指定的cookie，刷新页面，看是否需要从新登录
driver.delete_cookie(name='.CNBlogsCookie')
#driver.delete_all_cookies()
time.sleep(3)
driver.refresh()
driver.find_element_by_partial_link_text("登录").click()
#再次登录
driver.find_element_by_id('input1').send_keys('15239687008')
driver.find_element_by_id('input2').send_keys('zbh@911915')
driver.find_element_by_id('remember_me').click()
time.sleep(5)
driver.find_element_by_id('signin').click()
'''
六、cookie操作的几个方法
1.get_cookies()：获取所有cookies
2.driver.get_cookie（name）：获取指定name的cookie:
3.清除指定cookie：delete_cookie()
4.delete_all_cookies()：清除所有cookies
5.add_cookie(cookie_dict):添加cookie的值'''

























