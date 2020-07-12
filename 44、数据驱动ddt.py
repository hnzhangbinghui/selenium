'''在设计用例的时候，有些用例只是参数数据的输入不一样，比如登录这个功能，操作过程但是一样的。
如果用例重复去写操作过程会增加代码量，
对应这种多组数据的测试用例，可以用数据驱动设计模式，一组数据对应一个测试用例，用例自动加载生成。
'''
'''一、环境准备
1.安装ddt模块，打开cmd输入pip install ddt在线安装
>>pip install ddt'''

'''
数据驱动原理
1、测试数据为多个字典的list类型，
2、测试类前添加修饰@ddt.ddt
3、case前加修饰@ddt.data()
4、运行后用例会自动加载成三个单独的用例
'''
'''
#coding=utf-8
import ddt
import unittest
#测试数据
testData=[{'username':'15239687008','password':'123'},
          {'username':'15239687008','password':'123'},
          {'username':'15239687008','password':'123'},]
@ddt.ddt
class Test(unittest.TestCase):
    def setUp(self):
        print('start')
    def tearDown(self):
        print('END')
    @ddt.data(*testData)
    def test_ddt(self,data):
        print(data)
if __name__=='__main__':
    unittest.main()
'''

























#coding=utf-8
import ddt
import unittest
import time
from selenium import webdriver
import xlrd
'''testData=[{'username':'15239687008','password':'123'},
          {'username':'15239687008','password':'1234'},
          {'username':'15239687009','password':'123'}]'''

class ExcelUtil():
    def __init__(self,ecelPath,sheetName):
        self.data=xlrd.open_workbook(ecelPath)
        self.table=self.data.sheet_by_name(sheetName)
        self.keys=self.table.row_values(0) #获取第一行作为key值
        self.rowNum=self.table.nrows    #获取总行数
        self.colNum=self.table.ncols    #获取总列数

    def dict_data(self):
        if self.rowNum<=1:
            print("总行数小于1")
        else:
            r=[]
            j=1
            for i in range(self.rowNum-1):
                s={}
                #从第二行开始取对应values的值
                values=self.table.row_values(j)
                for x in range(self.colNum):
                    s[self.keys[x]]=values[x]
                r.append(s)
                j+=1
            return r
filepath="C:\\Users\\zhangbinghui_v\\PycharmProjects\\zbh_python\\python+selenium\\test.xlsx"
sheetName="Sheet1"
data=ExcelUtil(filepath,sheetName)
testData=data.dict_data()

@ddt.ddt
class Blog(unittest.TestCase):
    def setUp(self):
        self.driver=webdriver.Firefox()
        self.driver.get("http://jgdj.hnsft.gov.cn:8088/sft/login")
        self.driver.implicitly_wait(30)
    def login(self,username,password):
        self.driver.find_element_by_id('accountName').send_keys(username)
        self.driver.find_element_by_id('password').send_keys(password)
        self.driver.find_element_by_class_name('button_blue').click()
        time.sleep(3)
    def is_login_success(self):
        try:
            text=self.driver.find_element_by_id('label-1017').text
            print(text)
            return True
        except:
            return False
    @ddt.data(*testData)
    def test_login(self,data):
        print("当前测试数据%s" %data)
        #调用测试方法
        self.login(data["username"],data['password'])
        result=self.is_login_success()
        self.assertTrue(result)

if __name__=='__main__':
    unittest.main()



















