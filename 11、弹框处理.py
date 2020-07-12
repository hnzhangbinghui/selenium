'''不是所有的弹出框都叫alert，在使用alert方法前，先要识别出到底是不是alert。先认清楚alert长什么样子，下次碰到了，就可以用对应方法解决。
alert\confirm\prompt弹出框操作主要方法有：()
text：获取文本值
accept() ：点击"确认"
dismiss() ：点击"取消"或者叉掉对话框
send_keys() ：输入文本值 --仅限于prompt,在alert和confirm上没有输入框'''


'''先用switch_to_alert（）方法切换到alert弹框上
可以通过text方法获取弹窗的文本信息
accept（）点击确认
dismiss（）相当于点击右上角X，取消弹出框'''
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.action_chains import ActionChains
from selenium import webdriver
import time
#打开本地网页地址配置
url="file://C:/Users/zhangbinghui_v/Desktop/alter.html"
driver=webdriver.Firefox()
driver.get(url)
time.sleep(3)
#driver.find_element_by_id('alert').click()   #alter
#driver.find_element_by_id('confirm').click()  #confirm
driver.find_element_by_id('prompt').click()   #prompt
time.sleep(3)
t=driver.switch_to.alert    #alter的后面的括号不能加
t.send_keys("欧阳树乘凉")
print(t.text)
time.sleep(3)
t.accept()  #点击确认
#t.dismiss() #取消




































