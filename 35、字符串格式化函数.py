'''Python2.6 开始，新增了一种格式化字符串的函数 str.format()，它增强了字符串格式化的功能。
基本语法是通过 {} 和 : 来代替以前的 % 。
format 函数可以接受不限个参数，位置可以不按顺序。'''

#不设置位置
print("{}".format("hello"," zhangbinghui"))
print("{}{}".format("zhang","binghui"))
#设置指定位置
print("{0}{1}".format("hello","zhang","binghui"))
print("{1}{0}{1}".format(",hello,","zhangbinghui"))

#可以通过字典设置参数
site={"name":"菜鸟网络","url":"www.baidu.com"}
print("网站名：{name}，地址：{url}".format(**site))   #关键字参数

#通过列表索引设置参数
list=["菜鸟网络","www.baidu.com"]
print("网站名:{0[0]},地址：{0[1]}".format(list))    #"0"是必须写的















