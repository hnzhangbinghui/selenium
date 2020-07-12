# 参看URL:https://blog.csdn.net/weixin_41522164/article/details/82919571
#coding=utf-8
import smtplib  #发送邮件
from email.header import Header
from email.mime.text import MIMEText   #专门发送正文
from email.mime.multipart import MIMEMultipart #发送多个部分
from email.mime.application import MIMEApplication #发送附件
from email.utils import parseaddr, formataddr

#附件路径
file=r'D:\PycharmProjects\My_Book\2020-03-15 22-10-51beautiful.html'

def send_One_Email():
    smtp_server = 'smtp.163.com'  # 发送邮箱服务器
    port=25 #设置发送服务器的端口号，这里有SSL和TSL两种形式
    email_text='测试自动发送附件'
    from_addr = 'hnzhangbinghui@163.com'  # 发送邮箱
    to_addr = 'xiaoxiao.liu01@hand-china.com'  # 接受邮箱
    passwd = 'zbh123456'  # 发送邮箱密码
    # msg = MIMEText('SMTP测试邮件', 'plain', 'utf-8')  # 编写text的类型的邮箱正文
    #构建一个邮件体，正文，附件
    msg=MIMEMultipart()
    msg['Subject'] = Header('TEST', charset='utf-8')
    msg['from'] = from_addr
    msg['to'] = to_addr
    #构建正文
    part_text=MIMEText(email_text)
    msg.attach(part_text)

    #构建邮件附件
    part_attach1=MIMEApplication(open(file,'rb').read())  #打开附件
    part_attach1.add_header('Content-Disposition','attachment',filename='测试报告') #为附件命名
    msg.attach(part_attach1) #添加附件

    smtpobj = smtplib.SMTP(host=smtp_server, port=25)  # 生成SMTP邮箱对象
    print(type(smtpobj))  # 查看邮箱对象类型
    smtpobj.login(user=from_addr, password=passwd)  # 登陆邮箱
    smtpobj.sendmail(from_addr,to_addr, msg.as_string())  # 发送邮件
    print("发送邮箱成功")

i=1
for i in range(30):
    i+=1
    send_One_Email()