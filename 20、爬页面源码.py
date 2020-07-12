'''有时候通过元素的属性的查找页面上的某个元素，可能不太好找，
这时候可以从源码中爬出想要的信息。selenium的page_source方法可以获取到页面源码。
'''
'''selenium的page_source方法很少有人用到，小编最近看api不小心发现这个方法，
于是突发奇想，这里结合python的re模块用正则表达式爬出页面上所有的url地址，可以批量请求页面url地址，看是否存在404等异常'''
#通过selenium的page_source方法可以直接返回页面源码
#coding=utf-8
from selenium import webdriver
import re
driver=webdriver.Firefox()
driver.get("https://www.cnblogs.com/laozhangceshi/")
page=driver.page_source
print(page)
#通过re的正则匹配的非贪婪模式，利用findall方法返回一个list集合，可以打印页面所有的超链接
url_list=re.findall('href=\"(.*?)\"',page,re.S)  #re.S表示：'.' 匹配任意字符，若指定了re.S，则可以匹配换行符
urlall=[]
for url in url_list:
    if "http" in url:
        print(url)
        urlall.append(url)

print('本网页所有超链接个数：',len(urlall))


'''正则表达式中，“.”的作用是匹配除“\n”以外的任何字符，也就是说，它是在一行中进行匹配。
这里的“行”是以“\n”进行区分的。a字符串有每行的末尾有一个“\n”，不过它不可见。
如果不使用re.S参数，则只在每一行内进行匹配，如果一行没有，就换下一行重新开始，不会跨行。
而使用re.S参数以后，正则表达式会将这个字符串作为一个整体，将“\n”当做一个普通的字符加入到这个字符串中，在整体中进行匹配。'''















