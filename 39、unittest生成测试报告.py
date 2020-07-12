#coding=utf-8
import unittest
import os
import HtmlTestRunner
import sys


#用例路径
case_path=os.path.join(os.getcwd())
print(case_path)
#报告存放路径
report_path=os.path.join(os.getcwd())
print(report_path)
def all_case():
    discover=unittest.defaultTestLoader.discover(case_path,pattern="testcase*.py",top_level_dir=None)
    #print(discover)
    #discover=discover.encode()
    return discover


if __name__=='__main__':
    import HtmlTestRunner
    import time
    now = time.strftime('%Y-%m-%d %H:%M:%S')
    report_abcpath=os.path.join(report_path,"result.html")

    fp=open(report_abcpath,'wb')

    runner=HtmlTestRunner.HTMLTestRunner(stream=fp,
                                         report_title="生成HTML报告",
                                         descriptions="执行用例测试",
                                         output='utf-8')
    runner.run(all_case())
    fp.close()
