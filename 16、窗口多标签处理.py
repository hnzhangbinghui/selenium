'''用Selenium遇到多个浏览器窗口或单个浏览器多个标签（Tab）的状况时，往往都不太好处理，这里将介绍两种处理方法。'''

#encoding=utf-8
from selenium import webdriver
import time
driver=webdriver.Firefox()
driver.get("http://www.baidu.com")
time.sleep(3)
driver.find_element_by_link_text('把百度设为主页').click()
time.sleep(3)
ha=driver.window_handles
print(ha)
for handle in ha:
    if driver.current_window_handle != handle:
        driver.switch_to.window(handle)
        time.sleep(3)

driver.find_element_by_link_text("帮助中心").click()
print(driver.current_window_handle)
driver.switch_to.window(ha[0])
time.sleep(2)
driver.find_element_by_link_text("hao123").click()
driver.get_screenshot_as_file("D:\\test.png")
time.sleep(2)
driver.close()

#还可以通过JS来操作；https://i.cnblogs.com/EditArticles.aspx?opt=1





































