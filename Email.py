import smtplib
#1，生成smtp对象
smtpobj=smtplib.SMTP('smtp.163.com',465)  #传入邮箱供应商的域名和端口，并得到SMTP的对象；
print(type(smtpobj)) # 确定对象是一个smtp对象
#2，给服务器打招呼
smtpobj.ehlo()
print(smtpobj.ehlo())   #像smtp服务器打招呼，这种问候是smtp的第一步，对于建立服务器的连接很重要；否则，以后调试会导致错误；
#如果返回的是250，代表成功了；
#3,开始TLS 加密，如果你链接smtp的服务器的端口好是587，及时TLS加密，需要调用starttls（）方法，这是为链接加密的必须步骤；
    #如果你链接的是465的端口，即是SSL加密，加密已经设置好了，你可以跳过这一步；
# smtpobj.starttls()
# print(smtpobj.starttls())
#star

