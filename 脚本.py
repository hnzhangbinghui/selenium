#coding=utf-8
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains #引入鼠标事件
from selenium.webdriver.common.keys import Keys  #需要引入key包
import time
driver=webdriver.Chrome()
driver.get("http://10.179.101.85:9133/construct/#/process")
shijian=driver.find_element_by_xpath('/html/body/div[2]/div[2]/div[2]/button[1]')
driver.maximize_window()
time.sleep(2)
#ActionChains(driver).double_click(shijian).perform()#双击点开事件录入的按钮
chakan=driver.find_element_by_xpath('//*[@id="app"]/div[2]/div[2]/table/tr[2]/td[12]/button[4]')
ActionChains(driver).double_click(chakan).perform()
time.sleep(5)
sgmc=driver.find_element_by_xpath('//*[@id="app"]/div[2]/div[3]/div/div[2]/div[2]/div[1]/div/div[1]/input')
sgmc.clear()
sgmc.send_keys('python自动测试')
time.sleep(5)
quxiao=driver.find_element_by_xpath('//*[@id="app"]/div[2]/div[3]/div/div[2]/div[2]/div[2]/div[2]/button[1]')
ActionChains(driver).double_click(quxiao).perform()
time.sleep(5)
driver.quit()



