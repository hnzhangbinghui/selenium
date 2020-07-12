#coding=utf-8
from selenium import webdriver  #导入浏览器的webdriver模块
import time
driver=webdriver.Firefox()
driver.get("http://www.baidu.com")
time.sleep(5)  #设置休眠时间为3秒，也可以是小数，单位是秒
driver.back()  #返回上一页
driver.refresh()  #刷新新页面
driver.forward()  #切换到下一页
#driver.set_window_size(600,800)
time.sleep(3)
driver.maximize_window()  #将浏览器窗口最大化
#对网页进行截屏，截屏后指定保存路径+文件名称+后缀
driver.get_screenshot_as_file("D:\\test.png")
driver.close()  #关闭当前窗口
#driver.quit()  #退出关闭浏览器

















































