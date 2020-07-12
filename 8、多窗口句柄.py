'''有些页面的链接打开后，会重新打开一个窗口，对于这种情况，想在新页面上操作，就得先切换窗口了。
获取窗口的唯一标识用句柄表示，所以只需要切换句柄，我们就能在多个页面上灵活自如的操作了。'''
#切换句柄，共两种方法，一种是通过for循环，if判断来切换；二种是直接通过所有句柄的列表进行切换；

#coding:utf-8
from selenium import webdriver
import time
driver=webdriver.Firefox()
driver.get("http://bj.ganji.com/")
time.sleep(3)

driver.find_element_by_link_text('房东直租').click()
time.sleep(3)
driver.maximize_window()
#元素有属性，浏览器的窗口其实也有属性的，只是你看不到，浏览器窗口的属性用句柄（handle）来识别
h=driver.current_window_handle  #获取当前网页的句柄
print(driver.title)   #打印第二个句柄
ah=driver.window_handles  #获得所有网页的句柄


driver.switch_to.window(ah[0])    #切换到第一个句柄
print(driver.title)
driver.find_element_by_link_text('登录').click()

#driver.switch_to.window(ah[1])
#print(driver.title)



#driver.find_element_by_link_text('品牌公寓').click()
'''for handle in ah:
    if handle!=h:
        driver.switch_to.window(handle)   #注意to和Windows之间是点，下划线已经无法使用了；
        print(driver.title)
        print(handle)
        '''






























































