#web页面常用的一些操作元素方法，可以统称为行为事件
#1、简单操作
#coding:utf-8
from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys   #导入键盘模块
from selenium.webdriver.common.action_chains import ActionChains   #导入鼠标模块
'''perform()执行所有actionchains的足有行为，move_to_element()鼠标悬停'''
driver=webdriver.Firefox()
driver.get("http://www.baidu.com")
driver.implicitly_wait(5)
'''
#把鼠标悬停在搜索页面设置的按钮上
mouse=driver.find_element_by_link_text("设置")
ActionChains(driver).move_to_element(mouse).perform()  #模拟鼠标移动到设置这个地方
a=driver.find_element_by_link_text("搜索设置")           #找到鼠标点击设置之后的页面元素
ActionChains(driver).double_click(a).perform()          #对元素进行双击操作'''

#把鼠标点击登录按钮
denglu=driver.find_element_by_link_text("登录")
time.sleep(3)
ActionChains(driver).double_click(denglu).perform()
time.sleep(3)
driver.find_element_by_id('TANGRAM__PSP_10__footerULoginBtn').click()  #点击弹框上面的用户名登录
time.sleep(3)
driver.find_element_by_id('TANGRAM__PSP_10__userName').send_keys('欧阳树乘凉')
time.sleep(2)
driver.find_element_by_id('TANGRAM__PSP_10__password').send_keys('hnzbh260208')
driver.find_element_by_id('TANGRAM__PSP_10__password').submit()


'''账号退出
account=driver.find_element_by_link_text('欧阳树乘凉')
ActionChains(driver).move_to_element(account).perform()
tc=driver.find_element_by_link_text("退出")
ActionChains.double_click(tc).perform()'''


#driver.find_element_by_id('kw').send_keys('张冰辉')
#如果在有些地方，用submit的话，会报错，又没有搜索点按钮，引入键盘操作；
#driver.find_element_by_id('kw').send_keys(Keys.CONTROL,'a')  #模拟全选
#driver.find_element_by_id('kw').send_keys(Keys.CONTROL,'c')  #模拟复制
#driver.find_element_by_id('kw').click()
#driver.find_element_by_id('kw').send_keys(Keys.CONTROL,'v')   #模拟粘贴
#driver.find_element_by_id('kw').send_keys(Keys.ENTER)   #引入键盘，模拟回车键

#driver.find_element_by_id('kw').submit()   #submit模拟回车操作
#driver.find_element_by_id('su').click()
time.sleep(5)
driver.maximize_window()
driver.refresh()
driver.close()



'''键盘F1到F12：send_keys(Keys.F1) 把F1改成对应的快捷键

复制Ctrl+C：send_keys(Keys.CONTROL,'c') 

粘贴Ctrl+V：send_keys(Keys.CONTROL,'v') 

 全选Ctrl+A：send_keys(Keys.CONTROL,'a') 

剪切Ctrl+X：send_keys(Keys.CONTROL,'x') 

制表键Tab:  send_keys(Keys.TAB) 

这里只是列了一些常用的，当然除了键盘事件，也有鼠标事件'''