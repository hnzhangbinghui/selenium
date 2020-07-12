'''获取页面title的方法可以直接用driver.title获取到，然后也可以把获取到的结果用做断言。
介绍另外一种方法去判断页面title是否与期望结果一种,提到的expected_conditions模块里的title_is和title_contains两种方法
'''

'''1.首先看下源码,如下
class title_is(object):
    """An expectation for checking the title of a page.
    title is the expected title, which must be an exact match
    returns True if the title matches, false otherwise."""
    翻译：检查页面的title与期望值是都完全一致，如果完全一致，返回Ture,否则返回Flase
    def __init__(self, title):
        self.title = title
    def __call__(self, driver):
        return self.title == driver.title
2.注释翻译：检查页面的title与期望值是都完全一致，如果完全一致，返回True,否则返回Flase
3.title_is()这个是一个class类型，里面有两个方法
4.__init__是初始化内容，参数是title，必填项
5.__call__是把实例变成一个对象，参数是driver，返回的是self.title == driver.title，布尔值'''
#判断title的作用是判断此页面是否是所需的页面

#coding=utf-8
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
driver=webdriver.Firefox()
driver.get("https://www.baidu.com")
#第一种方法打印title
print(driver.title)
#第二种判断是否是这个title
title=EC.title_is('百度一下，你就知道')(driver)   #（注意）语法这样写
print(title)
#第三种方法判断title是否包含响应的内容
tt=EC.title_contains("百度一下")(driver)
print(tt)






















