'''有时候一个页面上有多个对象需要操作，如果一个个去定位的话，比较繁琐，这时候就可以定位一组对象。'''
'''webdriver 提供了定位一组元素的方法，跟前面八种定位方式其实一样，只是前面是单数，这里是复数形式：find_elements '''

#coding=utf-8
from selenium import webdriver
import time
import random  #导入随机函数
driver=webdriver.Chrome()
driver.implicitly_wait(5)  #隐式等待5秒
driver.get("http://www.baidu.com")
driver.find_element_by_id("kw").send_keys("测试部落")
driver.find_element_by_id('su').submit()
time.sleep(5)
driver.maximize_window()
s=driver.find_elements_by_partial_link_text('部落')  #得到的s是一个列表
print(s[0].text)
for i in s:
    print(i.get_attribute("href"))   #获取href属性，打印出url地址


#打印20,30之间的随机的整数
'''import random
t=random.randint(20,30)
print(t)'''
t=random.randint(0,7)
'''a=s[t].get_attribute("href")
print(a)
driver.get(a)'''
s[t].click()  #随机点击模仿用户的动作









































