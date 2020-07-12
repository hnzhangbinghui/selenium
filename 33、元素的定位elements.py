'''江湖传言，武林中流传八种定位，其中xpath是宝刀屠龙，css是倚天剑。
除了这八种，其实还有十种定位方法，眼看就快失传了，今天小编让失传已久的定位方法重出江湖！
一、十八种定位方法
前八种是大家都熟悉的，经常会用到的
1.id定位：find_element_by_id(self, id_)
2.name定位：find_element_by_name(self, name)
3.class定位：find_element_by_class_name(self, name)
4.tag定位：find_element_by_tag_name(self, name)
5.link定位：find_element_by_link_text(self, link_text)
6.partial_link定位find_element_by_partial_link_text(self, link_text)
7.xpath定位：find_element_by_xpath(self, xpath)
8.css定位：find_element_by_css_selector(self, css_selector）
这八种是复数形式
9.id复数定位find_elements_by_id(self, id_)
10.name复数定位find_elements_by_name(self, name)
11.class复数定位find_elements_by_class_name(self, name)
12.tag复数定位find_elements_by_tag_name(self, name)
13.link复数定位find_elements_by_link_text(self, text)
14.partial_link复数定位find_elements_by_partial_link_text(self, link_text)
15.xpath复数定位find_elements_by_xpath(self, xpath)
16.css复数定位find_elements_by_css_selector(self, css_selector
这两种就是快失传了的
find_element(self, by='id', value=None)
find_elements(self, by='id', value=None)'''
'''二、element和elements傻傻分不清
1.element方法定位到是是单数，是直接定位到元素
2.elements方法是复数，这个学过英文的都知道，定位到的是一组元素，返回的是list队列
3.可以用type()函数查看数据类型'''
'''2.这里重点介绍下用elements方法如何定位元素，当一个页面上有多个属性相同的元素时，然后父元素的属性也比较模糊，不太好定位。
这个时候不用怕，换个思维，别老想着一次定位到，可以先把相同属性的元素找出来，取对应的第几个就可以了。'''
#coding=utf-8
from selenium import webdriver
driver=webdriver.Firefox()
driver.get("http://www.baidu.com")
eles=driver.find_elements_by_class_name('mnav')
for ele in eles:
    print(ele.text)

eles[0].click()


import re
page=driver.page_source
print(page)
#通过re的正则匹配的非贪婪模式，利用findall方法返回一个list集合，可以打印页面所有的超链接
url_list=re.findall('href=\"(.*?)\"',page,re.S)  #re.S表示：'.' 匹配任意字符，若指定了re.S，则可以匹配换行符
urlall=[]
for url in url_list:
    if "http" in url:
        print(url)
        urlall.append(url)


#得到此时此刻的时间
import time
now=time.strftime('%Y-%m-%d %H:%M:%S')
print(now)
print(now+'result.html')

