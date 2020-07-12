#数组包括二维三维数组；
users=[1,2]
users.append(3)
print(users)

users.insert(1,111)
users.insert(2,222)
print(users)

users.remove(111)
print(users)

aa=users.pop()
print(aa)
print(users)

new_users=users*3
print(new_users)

new_users+=[666,777]
print(new_users)

#记录元素出现的个数
print(new_users.count(666))
#对数组进行排序
new_users.sort()
print(new_users)
#对数组进行倒序排序
new_users.reverse()
print(new_users)

#start: 计数从 start 开始。默认是从 0 开始。例如range（5）等价于range（0， 5）;
#end: 计数到 end 结束，但不包括 end。例如：range（0， 5） 是[0, 1, 2, 3, 4]没有5
#step：步长，默认为1。例如：range（0， 5） 等价于 range(0, 5, 1)
aaa=[]
#多维数组
for i in range(10):
    aaa.append([i])
    for j in range(10):
        aaa[i].append(j)
print(aaa)

#创建一个宽度为3，高度为4的数组；
list=[[0]*3]*4
print(list)

list[1][1]=5
print(list)
#这样做是修改了所有列，是因为是一个含有一个空列表元素的列表,所以[[]]*3表示3个指向这个空列表元素的引用,修改任何
#一个元素都会改变整个列表:

#创建多维数组；
bb=[[]for i in range(3)]
print(bb)
bb[0].append(222)
bb[1].extend(users)
bb[2].extend(new_users)
print(bb)


myList = [([0] * 3) for i in range(4)]
print(myList)









