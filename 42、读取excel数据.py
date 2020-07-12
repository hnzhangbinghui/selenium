'''当登录的账号有多个的时候，我们一般用excel存放测试数据，本节课介绍，python读取excel方法，并保存为字典格式。
1.先安装xlrd模块，打开cmd，输入pip install xlrd在线安装
>>pip install xlrd'''

'''如果excel数据中有纯数字的一定要右键》设置单元格格式》文本格式，要不然读取的数据是浮点数
（先设置单元格格式后编辑，编辑成功左上角有个小三角图标）'''
#coding=utf-8
import xlrd
data=xlrd.open_workbook('test.xlsx')   #打开表
table=data.sheet_by_name('Sheet1') #通过表中响应tab的名称
print(table)
nrows=table.nrows  #获取总行数
ncols=table.ncols  #获取总列数
print(ncols)
print(nrows)
print(table.row_values(0))
print(table.col_values(0))

#重要，封装读取方法
#最终读取的数据是多个字典的list类型数据，第一行数据就是字典里的key值，从第二行开始一一对应value值

#coding=utf-8
import xlrd
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


































