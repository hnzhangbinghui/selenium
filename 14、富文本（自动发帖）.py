'''富文本编辑框是做web自动化最常见的场景，有很多小伙伴遇到了不知道无从下手，
本篇以博客园的编辑器为例，解决如何定位富文本，输入文本内容'''

#coding=utf-8
from selenium import webdriver
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.action_chains import ActionChains
import time
driver=webdriver.Firefox()
driver.get("http://www.cnblogs.com/")
driver.find_element_by_link_text("登录").click()
driver.find_element_by_id('input1').send_keys('15239687008')
driver.find_element_by_id('input2').send_keys('zbh@911915')
driver.find_element_by_id('remember_me').click()
time.sleep(2)
driver.find_element_by_id('signin').click()
b=driver.find_element_by_xpath('/html/body/div[1]/div/div/form/div[4]/div/div/div[2]/div[2]/div/div[3]')
ActionChains(driver).move_to_element(b).perform()
driver.find_element_by_xpath('/html/body/div[1]/div/div/form/div[4]/div/div/div[2]/div[2]/div/div[2]/div[1]/div[3]/span[1]').click()
time.sleep(2)
driver.maximize_window()
driver.find_element_by_link_text('我的博客').click()
time.sleep(3)
driver.find_element_by_link_text('管理').click()
time.sleep(2)
driver.find_element_by_link_text('添加新随笔').click()
driver.find_element_by_id('Editor_Edit_txbTitle').send_keys('富文本测试')
#重点要讲的富文本的编辑，这里编辑框有个iframe，所以需要先切换
driver.switch_to.frame('Editor_Edit_EditorBody_ifr')
driver.find_element_by_id('tinymce').send_keys('   富文本测试1富文本测试1富文本测试1富文本测试1文本测试1富文本测试1')
time.sleep(2)
driver.find_element_by_id('tinymce').send_keys('富文本测试2')
time.sleep(2)
driver.find_element_by_id('tinymce').send_keys('富文本测试3')
driver.quit()










































