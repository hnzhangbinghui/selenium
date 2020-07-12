#coding=utf-8
import xlrd
from selenium import webdriver
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
if __name__=="__main__":
    filepath="C:\\Users\\zhangbinghui_v\\PycharmProjects\\zbh_python\\python+selenium\\test.xlsx"
    sheetName="Sheet1"
    data=ExcelUtil(filepath,sheetName)
    print(data.dict_data())
''' for a in data.dict_data():
        driver=webdriver.Firefox()
        driver.get("http://jgdj.hnsft.gov.cn:8088/sft/login")
        driver.find_element_by_id("accountName").send_keys(a.get('username'))
        driver.find_element_by_id('password').send_keys(a.get('password'))
        driver.find_element_by_class_name('button_blue').click()
'''
