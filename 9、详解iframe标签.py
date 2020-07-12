'''Frame与Iframe两者可以实现的功能基本相同，不过Iframe比Frame具有更多的灵活性。
frame是整个页面的框架，iframe是内嵌的网页元素，也可以说是内嵌的框架
'''
'''Iframe标记又叫浮动帧标记，可以用它将一个HTML文档嵌入在一个HTML中显示。
它和Frame标记的最大区别是在网页中嵌入 的<Iframe></Iframe>所包含的内容与整个页面是一个整体，
而<Frame>< /Frame>所包含的内容是一个独立的个体，是可以独立显示的。
另外，应用Iframe还可以在同一个页面中多次显示同一内容，而不必重复这段内 容的代码。'''
'''1.这里iframe的切换是默认支持id和name的方法的，当然实际情况中会遇到没有id属性和name属性为空的情况，这时候就需要先定位iframe
    2.定位元素还是之前的八种方法同样适用，这里我可以通过tag先定位到，也能达到同样效果'''
#coding:utf-8
from selenium import webdriver
import time
driver=webdriver.Firefox()
driver.get("https://mail.163.com/")
driver.implicitly_wait(10)
#切换iframe
iframe=driver.find_element_by_tag_name('iframe')
driver.switch_to.frame(iframe)


driver.find_element_by_id('auto-id-1548314685813.j-inputtext dlemail').send_keys('hnzhangbinghui')
time.sleep(2)
driver.find_element_by_id('auto-id-1548316072916').send_keys('laozhang260208')
time.sleep(2)
driver.find_element_by_id('dologin').click()


#释放iframe，重新回到主页面上面
driver.switch_to.default_content()




'''还得更新'''






































