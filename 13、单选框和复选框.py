#单选框是圆的；下图复选框是方的，这个是业界的标准

#coding=utf-8
from selenium import webdriver
import time
driver=webdriver.Firefox()
driver.get("file:///C:/Users/zhangbinghui_v/Desktop/%E5%8D%95%E9%80%89%E6%A1%86%E5%A4%8D%E9%80%89%E6%A1%86.html")
#单选框
driver.find_element_by_id('boy').click()
time.sleep(3)
driver.find_element_by_id('girl').click()
time.sleep(3)
#全部勾选复选框，通过获取所有的元素，然后通过for循环，依次点击

f=driver.find_elements_by_xpath(".//*[@type='checkbox']")
print(f)
for i in f:
    i.click()
    time.sleep(2)
'''find_elements是不能直接点击的，它是复数的，
所以只能先获取到所有的f对象，然后通过for循环去一个个点击操作'''
#判断是否选中：is_selected()
'''有时候这个选项框，本身就是选中状态，如果我再点击一下，它就反选了，这可不是我期望的结果，那么可不可以当它是没选中的时候，我去点击下；
当它已经是选中状态，我就不点击呢？那么问题来了：如何判断选项框是选中状态？
    2.判断元素是否选中这一步才是本文的核心内容，点击选项框对于大家来说没什么难度。获取元素是否为选中状态，打印结果如下图。
    3.返回结果为bool类型，没点击时候返回False,点击后返回True，接下来就很容易判断了，既可以作为操作前的判断，也可以作为测试结果的判断 '''
driver.find_element_by_id('c1').click()
s=driver.find_element_by_id('c1').is_selected()
print(s)
r=driver.find_element_by_id('boy').is_selected()
print(r)































