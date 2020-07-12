#coding=utf-8
import unittest,os,time,sys
import HtmlTestRunner
'''
report_path=os.getcwd()
now=time.strftime('%y-%m-%d %H:%M',time.localtime(time.time()))  #获取当前信息并且以前面的格式输出
title="自动化测试报告"
report_rapash=os.path.join(report_path,title+'.html')  #组成一个测试报告的路径
print(report_rapash)'''

#导入用例
def case_all():
    case_pash='C:\\Users\zhangbinghui_v\PycharmProjects\zbh_python'
    discover=unittest.defaultTestLoader.discover(case_pash,pattern='testcase.py')
    #添加用例，在case_path的路径下，所有已ceshi开头（pattern='ceshi*.py’）的文件都当做用例文件执行；
    return discover
if __name__=='__main__':
    #fp=open(report_rapash,'w',encoding='utf-8')  #保存报告文件
    #print(fp)

    runner=unittest.TextTestRunner()
    runner.run(case_all())  #执行用例
    #fp.close()