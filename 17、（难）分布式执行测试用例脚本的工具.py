'''Selenium grid是用来分布式执行测试用例脚本的工具，比如测试人员经常要测试多浏览器的兼容性，那就可以用到grid了。
下面就来介绍如何在多个浏览器上运行同一份脚本。'''
''''使用grid所需要的文件：1.Selenium server（即selenium-server-standalone-x.xx.x.jar）；
2.grid配置文件（该文件负责提供主机和浏览器信息）；
3.测试脚本。'''

#1、grid配置文件的内容
'''该文件定义了一个方法，该方法存放了一个字典，分别给本机分配了2个不同的端口并指定了不同的浏览器
（4444是grid hub的默认端口，5555这个是一个node的端口，后续会介绍）'''
def grid():
    d={
        'http://127.0.0.1:4444/wd/hub':'firefox',
        'http://127.0.0.1:5555/wd/hub':'internet explorer',
    }
    return d
#2、测试脚本
#encoding=utf-8
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import time,os.path
import grid_module
for host,browser in grid_module.grid().items():
    driver=webdriver.Remote(
        command_executor==host,
        desired_capabilities={
            'platform':'ANY',
            'browserName':browser,
            'version':'',
            'javascriptEnabled':True
        }
    )
    driver.get("http://www.baidu.com")
    driver.find_element_by_id('kw').send_keys('中国')
    driver.find_element_by_id('su').click()
    time.sleep(3)
    if driver.title=='中国_百度搜索':
        print('title匹配')
    else:
        print('title不匹配')
    driver.close()

#太难了，待看



































