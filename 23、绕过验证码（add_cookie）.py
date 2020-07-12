'''验证码这种问题是比较头疼的，对于验证码的处理，不要去想破解方法，这个验证码本来就是为了防止别人自动化登录的。
如果你能破解，说明你们公司的验证码吗安全级别不高，那就需要提高级别了。
对于验证码，要么是让开发在测试环境弄个万能的验证码，如：1234，要么就是尽量绕过去，如本篇介绍的添加cookie的方法'''
#添加cookie方法：driver.add_cookie（）
#1.add_cookie(cookie_dict)方法里面参数是cookie_dict，说明里面参数是字典类型。

'''2.源码官方文档介绍：
add_cookie(self, cookie_dict)
Adds a cookie to your current session.
:Args:
- cookie_dict: A dictionary object, with required keys - "name" and "value";
optional keys - "path", "domain", "secure", "expiry"
Usage:
driver.add_cookie({'name' : 'foo', 'value' : 'bar'})
driver.add_cookie({'name' : 'foo', 'value' : 'bar', 'path' : '/'})
driver.add_cookie({'name' : 'foo', 'value' : 'bar', 'path' : '/', 'secure':True})
3.从官方的文档里面可以看出，添加cookie时候传入字典类型就可以了，等号左边的是name，等号左边的是value。
4.把前面抓到的两组数据（参数不仅仅只有name和value），写成字典类型：
{'name':'.CNBlogsCookie','value'：'2C3AE01E461B2D2F1572D02CB936D77A053089AA2xxxx...'}
{'name':'.Cnblogs.AspNetCore.Cookies','value':'CfDJ8Mmb5OBERd5FqtiQlKZZIG4HKz_Zxxx...'}'''

'''、cookie组成结构

1.用抓包工具fidller只能看到cookie的name和value两个参数，实际上cookie还有其它参数
2.cookie参数组成，以下参数是我通过get_cookie（name）获取到的，
参考上一篇：Selenium2+python自动化40-cookie相关操作
cookie ={u'domain': u'.cnblogs.com',
            u'name': u'.CNBlogsCookie',
            u'value': u'xxxx',
            u'expiry': 1491887887,
            u'path': u'/',
            u'httpOnly': True,
            u'secure': False}
name：cookie的名称
value：cookie对应的值，动态生成的
domain：服务器域名
expiry：Cookie有效终止日期
path：Path属性定义了Web服务器上哪些路径下的页面可获取服务器设置的Cookie
httpOnly：防脚本攻击
secure:在Cookie中标记该变量，表明只有当浏览器和Web Server之间的通信协议为加密认证协议时，
浏览器才向服务器提交相应的Cookie。当前这种协议只有一种，即为HTTPS。'''
#coding=utf-8
from selenium import webdriver
import time
driver=webdriver.Firefox()
driver.get('https://www.cnblogs.com/laozhangceshi/')

#添加cookie #可以通过get_cookies()去抓取
c1={'name': '.CNBlogsCookie',
    'value': 'DDAD632F8C50E6D93245C700860D863837C548255888E0350AAFA1C13E7782E8918C54A6CA8255E5E4BC08448F3660475C0F67BD06116FFBD5C7BEA4B9A6670DAE83548B0A2F549CECFA7802B6BC0432338FF43D7035141E4A563EB8B76A091E566E4565',
    'path': '/',
    'domain': '.cnblogs.com',
    'secure': False,
    'httpOnly': True,
    'expiry': 1551345663}
c2={'name': '.Cnblogs.AspNetCore.Cookies',
    'value': 'CfDJ8KlpyPucjmhMuZTmH8oiYTMIi6ujuCOwTXiNySIliDBAkCD7FjaggBvMRr0kKgU1ukgYlwBaXfEieYsJzdcNzPbwiP_I0kjyk-RlmY4ZLpu8MG_PH2PO9AEz9x0hIcnABLWU7JQz2eHLBBMM2OKe3N8zD7ZcliQVaZe-6RaAHSRpkK3E_Xpg4qFhiVuUfJV7tUf5PZh9DKSHFc6PfUVk-0VoYveb7b2_8qFqiW6iKTu5rN8mC558WvID7Tg8c9kwYANB0S0NDmw0fUS2v1jxShSxAypwZb2cP1zwtt5MoCE5WmvycUPXH4rcWwLRkCwKlg',
    'path': '/',
    'domain': '.cnblogs.com',
    'secure': False,
    'httpOnly': True,
    'expiry': 1551345663}
driver.add_cookie(c1)
driver.add_cookie(c2)

time.sleep(3)
driver.refresh()


'''几点需要注意：
1.登录时候要勾选下次自动登录按钮。
2.add_cookie（）只添加name和value，对于博客园的登录是不成功。
3.本方法并不适合所有的网站，一般像博客园这种记住登录状态的才会适合。'''




























