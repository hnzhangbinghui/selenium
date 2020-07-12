'''在做结果判断的时候，经常想判断某个元素中是否存在指定的文本，如登录后判断页面中是账号是否是该用户的用户名。
在前面的登录案例中，写了一个简单的方法，但不是公用的，在EC模块有个方法是可以专门用来判断元素中存在指定文本的：text_to_be_present_in_element。
另外一个差不多复方法判断元素的value值：text_to_be_present_in_element_value'''

#coding=utf-8
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
driver=webdriver.Firefox()
driver.get("http://www.baidu.com")
#判断元素中的text文本是否包含预期的字符串
locator=("name","tj_trnews")
text="新闻"

result=EC.text_to_be_present_in_element(locator,text)(driver)
print(result)

#判断某个元素的value属性值是否包含预期的字符串
locator1=("id","su")
text1="百度一下"
result1=EC.text_to_be_present_in_element_value(locator1,text1)(driver)
print(result1)