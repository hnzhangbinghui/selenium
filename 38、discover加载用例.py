#coding=utf-8
import unittest
import os
import HtmlTestRunner
#用例路径
case_path=os.path.join(os.getcwd())
print(case_path)
#报告存放路径
report_path=os.path.join(os.getcwd(),"report")
print(report_path)
def all_case():
    discover=unittest.defaultTestLoader.discover(case_path,pattern="testcase*.py",top_level_dir=None)
    print(discover)
    return discover

if __name__=='__main__':
    #suite=unittest.TestSuite()
    #suite.addTests(discover)
    runner=unittest.TextTestRunner()
    runner.run(all_case())
