#coding=utf-8
import time
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
from selenium.webdriver.support import expected_conditions as EC  #作用判断元素是否存在

driver=webdriver.Firefox()
driver.get("http://www.baidu.com")
time.sleep(3)
print(EC.title_contains("百度一下")(driver))



driver.maximize_window()
mouse=driver.find_element_by_partial_link_text("设置")
ActionChains(driver).move_to_element(mouse).perform()
time.sleep(1)
driver.find_element_by_partial_link_text("搜索设置").click()
select=driver.find_element_by_id("nr")

time.sleep(3)
Select(select).select_by_index(2)
time.sleep(2)
Select(select).select_by_value('20')
time.sleep(3)
Select(select).select_by_visible_text("每页显示50条")
time.sleep(3)
select.find_element_by_xpath("//*[@id='nr']/option[1]").click()
time.sleep(3)
driver.find_element_by_class_name('prefpanelgo').submit()
#判断弹框结果，是否弹出
#t=driver.switch_to.alert     #alter后面不需要括号
result=EC.alert_is_present()(driver)    #EC判断元素是否存在
if result:
    print(result.text())
    result.eccept()
else:
    print("alert未弹出!!!")



