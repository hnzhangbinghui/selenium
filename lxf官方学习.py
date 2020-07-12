print(r'zhang\\bing\nhui')#转移字符的打印

print('''zhang
bing
hui
hello''')
#多行换行的打印


#变量赋值的变化
aa='abc'
b=aa
aa='sss'
print(b)

print('%d-%02d' %(3,1))
print('%.2f' %3.1415)

print("growth rate:%d%%" % 22)

print("age:%12d,tizhong:%s" %(22,444))

#列表当中的二维数组
list1=['zhang','binghui']
list2=['aaa','bbb',list1,'ddd']
print(len(list2))
print(list2)
print(list1[0])
print(list2[2][0])

list1.append('laozhang')
print(list1)
print(list2)
print('\n')
#这是因为input()返回的数据类型是str，str不能直接和整数比较，必须先把str转换成整数。Python提供了int()函数来完成这件事情：
age=input("input your age : ")
abs=int(age)
if abs<33:
    print("hello")
else:
    print("nihao")

#循环求和
sum=0
for x in range(100):
    sum=sum+x
print(sum)
sum1=0
for x in list(range(100)):
    sum1=sum1+x
print(sum1)

sum2=0
n=99
while n>0:
    sum2=sum2+n
    n=n-1
print(sum2)
























