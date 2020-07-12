'''我们在登录网站的时候，通常需要输入用户名、密码和验证码，那么有没有办法绕过登录环节呢？
有两种方法可以解决这个问题，一种是利用chrome浏览器的用户配置，一种是利用cookie'''
'''
第一步：如果之前未登录过该网站，在手工登录的时候，要勾选下次自动登录
第二步：利用chrome://version查看User Data的路径,用户的配置信息都放在User Data目录下
第三步：构建python代码
这里值得注意的是：
1. --user-data-dir 要写正确(--user-data-dir或user-data-dir都是可以的)，我看很多博文里都写成了–user-data-dir，经过测试，发现后者是无法加载用户配置的
2. get后的url为登陆后页面的url，这也契合我们的目的：即绕过登录页面，直接查看登陆后的页面
第四步：python代码运行之前，请关闭已打开的chrome浏览器
否则，chromedriver会挂起，后面打开url的操作不会执行，这一点请参考《Selenium chromedriver hangs if I specify user-data-dir in Chrome options》:
看来这个和远程调试有关系，如果想用调试器来进入用户配置，为了避免chromedriver尝试连接调试器而导致的挂起，必须关闭已经存在的chrome会话
第五步：运行代码，观察结果
结果是符合预期的，因为看到的用户名，我的博客和退出选项
'''

#coding=utf-8
from selenium import webdriver
import time
import argparse
#1、通过添浏览器配置添加缓存数据绕过登录
#option=webdriver.ChromeOptions()
#option.add_argument("--user-data-dir=C:\\Users\\zhangbinghui_v\\AppData\\Local\\Google\\Chrome\\User Data")
#driver=webdriver.Chrome(options=option)
driver=webdriver.Firefox()
driver.get("https://www.cnblogs.com/")
'''三. 加载用户配置并不是万能的
利用ChromeOptions()加载用户配置的前提是，我们要访问页面的url在浏览器的每次会话中都是相同的，
如果同一页面每次会话的url变化，这意味着可能要改变一下策略了，以QQ邮箱为例，每次浏览器会话中首页的url都是不同的
从上面两张图中，可以明显发现这个sid是变动的，sid又是什么呢？请参考《详解SID之终结篇》，里面有句话是：
"SID即安全标识符(System IDentifier)，它用来标识用户身份的。当系统每次创建用户都会分配一个唯一的SID，每个帐户的SID都是不重复的"
'''
#2通过添加cookies绕过登录

#添加cookie #可以通过get_cookies()去抓取
c1={'name': '.CNBlogsCookie',
    'value': 'DDAD632F8C50E6D93245C700860D863837C548255888E0350AAFA1C13E7782E8918C54A6CA8255E5E4BC08448F3660475C0F67BD06116FFBD5C7BEA4B9A6670DAE83548B0A2F549CECFA7802B6BC0432338FF43D7035141E4A563EB8B76A091E566E4565',
    #'path': '/',
    'domain': '.cnblogs.com',
    #'secure': False,
    #'httpOnly': True,
    'expiry': 1551345663}
c2={'name': '.Cnblogs.AspNetCore.Cookies',
    'value': 'CfDJ8KlpyPucjmhMuZTmH8oiYTMIi6ujuCOwTXiNySIliDBAkCD7FjaggBvMRr0kKgU1ukgYlwBaXfEieYsJzdcNzPbwiP_I0kjyk-RlmY4ZLpu8MG_PH2PO9AEz9x0hIcnABLWU7JQz2eHLBBMM2OKe3N8zD7ZcliQVaZe-6RaAHSRpkK3E_Xpg4qFhiVuUfJV7tUf5PZh9DKSHFc6PfUVk-0VoYveb7b2_8qFqiW6iKTu5rN8mC558WvID7Tg8c9kwYANB0S0NDmw0fUS2v1jxShSxAypwZb2cP1zwtt5MoCE5WmvycUPXH4rcWwLRkCwKlg',
   # 'path': '/',
    'domain': '.cnblogs.com',
   # 'secure': False,
   # 'httpOnly': True,
    'expiry': 1551345663}
driver.add_cookie(c1)
driver.add_cookie(c2)

time.sleep(3)
driver.refresh()



























