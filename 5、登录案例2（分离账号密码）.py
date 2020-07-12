'''上面的代码能实现登录，但整个代码跟记流水账一样，没什么可读性。如果我想换个账号登录，这时候还得找到登录的账号和密码位置，比较费时。
    2.我们可以把登录和退出写出两个函数，这样看起来更舒服一点。
    3.把登录的账号和密码参数化'''


#coding:utf-8
from selenium import webdriver
import time
#登录函数
def login(driver,user,password):
    driver.get("https://www.263.net/")
    time.sleep(5)
    driver.maximize_window()
    driver.find_element_by_id('username').send_keys(user)
    time.sleep(2)
    driver.find_element_by_id('userTypePwd').send_keys(password)
    time.sleep(2)
    driver.find_element_by_id('wmSubBtn').click()
#退出函数
def logout(driver):
    time.sleep(3)
    driver.find_element_by_class_name('userIcon').click()
    time.sleep(2)
    driver.find_element_by_id('linkLogOut').click()
    time.sleep(2)
    driver.quit()
#主函数
if __name__=="__main__":
    driver=webdriver.Firefox()
    login(driver,'zhangbinghui@camelotchina.com','zbh15239687008')
    print('nihao')
    logout(driver)














































