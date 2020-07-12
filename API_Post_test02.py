import requests  # 导包
import unittest

# 请求url
new_url='http://10.122.189.79/api/program/auth/getToken'
# 请求头
headers = {'content-type': 'application/x-www-form-urlencoded'}
# data格式的请求参数
data ={"itcode":"zhangbinghui","ImgCode":True}
# 发送链接接口，得到response对象
res = requests.post(new_url, json=data)

print(res.status_code)  # 响应的状态码
print(res.text)  # 文本格式
print(res.content)  # 响应的内容
print(res.headers)
print(res.url)  # 请求的URL
print(res.json())  # json格式
print(res.json()['data'])  #得到响应json的键值
