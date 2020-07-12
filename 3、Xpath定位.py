'''XPath即为XML路径语言，它是一种用来确定XML1（标准通用标记语言3的子集）文档中某部分位置的语言。
反正小编看这个介绍是云里雾里的，通俗一点讲就是通过元素的路径来查找到这个元素的，相当于通过定位一个对象的坐标，来找到这个对象。'''

#属性定位，通过元素的id，name，class这些属性定位

#coding=utf-8
from selenium import webdriver  #导入浏览器的webdriver模块
import time
driver=webdriver.Firefox()
driver.get("http://www.baidu.com")

driver.find_element_by_id('kw').send_keys('张冰辉')
driver.find_element_by_id('su').click()
time.sleep(5)  #设置休眠时间为3秒，也可以是小数，单位是秒
driver.back()  #返回上一页
time.sleep(5)

driver.find_element_by_xpath('/html/body/div[1]/div[1]/div/div[3]/a[2]').click()

time.sleep(6)
driver.find_element_by_xpath('//*[@id="site"]/div/ul/li[10]/a').click()
time.sleep(5)

driver.refresh()  #刷新新页面
#driver.forward()  #切换到下一页
driver.set_window_size(600,800)
time.sleep(5)
driver.maximize_window()  #将浏览器窗口最大化
#对网页进行截屏，截屏后指定保存路径+文件名称+后缀
driver.get_screenshot_as_file("D:\\test.png")
#driver.close()  #关闭当前窗口
driver.quit()  #退出关闭浏览器


















































