'''在web页面中经常会遇到table表格，特别是后台操作页面比较常见。本篇详细讲解table表格如何定位。'''

'''table特征
    1.table页面查看源码一般有这几个明显的标签：table、tr、th、td
    2.<table>标示一个表格
    3.<tr>标示这个表格中间的一个行
    4.</th> 定义表头单元格
    5.</td> 定义单元格标签，一组<td>标签将将建立一个单元格，<td>标签必须放在<tr>标签内'''
#coding=utf-8
from selenium import webdriver
driver=webdriver.Firefox()
driver.get('file:///C:/Users/zhangbinghui_v/Desktop/table.html')
t=driver.find_element_by_xpath('/html/body/table/tbody/tr[2]/td[1]')
print(t.text)




#补充：有些小伙伴可能会遇到table在ifame上的情况，这时候就需要先切换iframe了




































