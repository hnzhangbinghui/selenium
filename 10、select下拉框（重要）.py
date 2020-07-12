#coding:utf-8
from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys   #导入键盘模块
from selenium.webdriver.common.action_chains import ActionChains   #导入鼠标模块
from selenium.webdriver.support.select import Select      #导入select模块

'''perform()执行所有actionchains的足有行为，move_to_element()鼠标悬停'''
driver=webdriver.Firefox()
driver.get("http://www.baidu.com")
driver.implicitly_wait(5)
driver.maximize_window()
mouse=driver.find_element_by_link_text("设置")
ActionChains(driver).move_to_element(mouse).perform()  #模拟鼠标移动到设置这个地方
a=driver.find_element_by_link_text("搜索设置")           #找到鼠标点击设置之后的页面元素
ActionChains(driver).double_click(a).perform()

'''1、定位select里的选项有多种方式，这里先介绍一种简单的方法：二次定位
2.基本思路，先定位select框，再定位select里的选项'''
#分两步，先定位下拉框，在点击选项
'''#第一种办法
s=driver.find_element_by_id('nr')
time.sleep(5)                    #(重要)这个等待时间必须添加否则会报错
s.find_element_by_xpath("//option[@value='50']").click()
driver.find_element_by_class_name('prefpanelgo').submit()  #点击保存按钮
time.sleep(3)'''

#导入select模块，直接根据属性或索引定位，然后通过selet选项的索引来定位选择对应选项（从0开始计数）
#如选择第三个选项：select_by_index(2)

s=driver.find_element_by_id('nr')      #获取对应的元素
time.sleep(5)
#选择对应不同的下拉框的值
Select(s).select_by_index(2)  #通过索引
time.sleep(3)
Select(s).select_by_value('20')  #通过value的值
time.sleep(2)
Select(s).select_by_visible_text("每页显示10条")
time.sleep(3)
s.click()
driver.find_element_by_class_name('prefpanelgo').click() #点击保存按钮
#处理弹框操作
t=driver.switch_to.alert     #alter后面不需要括号；
time.sleep(3)
print(t.text)
t.accept()

driver.quit()

'''
select的其他功能：
select_by_index()  :通过索引定位
select_by_value()  :通过value值定位
select_by_visible_text() :通过文本值定位
deselect_all()          ：取消所有选项
deselect_by_index()     ：取消对应index选项
deselect_by_value()      ：取消对应value选项
deselect_by_visible_text() ：取消对应文本选项
first_selected_option()  ：返回第一个选项
all_selected_options()   ：返回所有的选项'''



























