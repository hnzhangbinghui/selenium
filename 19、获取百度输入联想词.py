'''1、首先在百度输入框输入关键词，如：博客，然后输入框下方会自动匹配出关键词。
2.这时候可以用firebug工具定位到联想出来的词，可以看到下方匹配出来的词都有共同的class属性，这时候就可以全部定位到了'''

#coding=utf-8
from selenium import webdriver
import time
driver=webdriver.Firefox()
driver.get("http://www.baidu.com")
a=input('你要搜索的词汇：')
driver.find_element_by_id('kw').send_keys(a)
time.sleep(3)
bd=driver.find_elements_by_class_name('bdsug-overflow')
for i in bd:
    print(i.get_attribute("data-key"))

if len(bd)>1:
    bd[1].click()
    print(driver.current_url)
else:
    print("未找到匹配的词")



