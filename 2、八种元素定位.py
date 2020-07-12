'''自动化四个步骤：获取元素，操作元素，获取返回结果，断言（返回结果与期望结果是否一致），最后自动出测试报告'''

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
driver.find_element_by_partial_link_text('hao123').click()

driver.refresh()  #刷新新页面
driver.forward()  #切换到下一页
driver.set_window_size(600,800)
time.sleep(3)
driver.maximize_window()  #将浏览器窗口最大化
#对网页进行截屏，截屏后指定保存路径+文件名称+后缀
driver.get_screenshot_as_file("D:\\test.png")
#driver.close()  #关闭当前窗口
driver.quit()  #退出关闭浏览器




'''selenium的webdriver提供了八种基本的元素定位方法，前面六种是通过元素的属性来直接定位的，后面的xpath和css定位更加灵活，需要重点掌握其中一个。

1.通过id定位：find_element_by_id()
2.通过name定位：find_element_by_name()
3.通过class定位：find_element_by_class_name()
4.通过tag定位：find_element_by_tag_name()
5.通过link定位：find_element_by_link_text()
6.通过partial_link定位：find_element_by_partial_link_text()
7.通过xpath定位：find_element_by_xpath()
8.通过css定位：find_element_by_css_selector()'''



















