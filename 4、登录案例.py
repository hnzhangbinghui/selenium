#登录案例
#coding=utf-8
from selenium import webdriver
import time
driver=webdriver.Firefox()
driver.get("https://www.263.net/")
time.sleep(3)
driver.maximize_window()
ele1=driver.find_element_by_id('username')
ele1.clear()
ele1.send_keys('zhangbinghui@camelotchina.com')
time.sleep(2)
ele2=driver.find_element_by_id('userTypePwd')
ele2.clear()
ele2.send_keys('zbh15239687008')
time.sleep(2)
driver.find_element_by_id('wmSubBtn').click()
time.sleep(6)
#检查是否登录成功,通过.text方法获取这个元素的文本属性,一定要定位好元素
driver.find_element_by_class_name('userIcon').click()
time.sleep(3)
name=driver.find_element_by_partial_link_text('zhangbinghui@camelotchina.com').text
print('登录的账号是：%s' %name)
if name=='张冰辉zhangbinghui@camelotchina.com':
    print("恭喜你，登录成功")
else:
    print("登录成功")
#退出登录
driver.find_element_by_id('linkLogOut').click()
#关闭浏览器
driver.quit()



























