import requests  # 导包

# 请求url
new_url='http://10.122.189.79/api/program/paymentMode/initPaymentMode'
# 请求头
headers = {'content-type': 'application/x-www-form-urlencoded'}
# data格式的请求参数
data ={"programId":"670018230","market":"CH","businessGroup":"PCG","programType":"T1 Distributor"}
# 发送链接接口，得到response对象
res = requests.post(new_url, json=data,timeout=1)

print(res.status_code)  # 响应的状态码
print(res.text)  # 文本格式
print(res.content)  # 响应的内容
print(res.headers)
print(res.url)  # 请求的URL
print(res.json())  # json格式
print(res.json()['msg'])  #得到响应json的键值
print('*****响应时间*****')
print(res.elapsed)
print(res.elapsed.total_seconds())   #总时长，单位是秒
print(res.elapsed.microseconds)   # 获取微秒部分，大于0小于1秒
print(res.elapsed.seconds)  #秒，大于0小于1天
print(res.elapsed.days)
print(res.elapsed.max,res.elapsed.min)
print(res.elapsed.resolution)  #最小时间单位


# #json格式的请求参数
# json={
#     "data":[{'flag': 'mobile',
#       'password': 'e9f5c5240c0bb39488e6dbfbdb1517e0',
#       'mobile_phone':' ********'}]
#     }
# #res = requests.post(new_url,json=json, headers=headers)
#
# #可以通过导入json包，把data格式转换为json对象
# import json
# j=json.dump(data)
#
# #响应数据json格式和text的区别
# #1，json格式返回的是字典类型，可以通过键名方式来获取响应的值，获取方式是json()['键名']
# #2，text格式返回的是字符串类型，无法通过键名方式来获取响应的值
#

#参考URL:https://www.cnblogs.com/jingdenghuakai/p/11805013.html








