#列表推导式，求0-9的平方和；
a=sum(x*x for x in range(10))
print(a)

#python使用lambda表示匿名函数，匿名函数只能是表达式
add=lambda x,y:x*y
print(add(2,2))

#列表元素能改变，元祖元素不能改变；
#同时给元素赋值
aa,bb=1,2
print(aa,bb)
aa,bb=bb,aa
print(aa,bb)

#删除和清空字典的元素
usernames={"name1":"zhangsan","age":"23"}
print(usernames)
#删除字典元素
del usernames["name1"]
print(usernames)
#清空字典
usernames.clear()
print(usernames)


#列表append函数
list_cars=[1,2,3,4,5,6]
print(list_cars*2)
list_cars.append("zhang")
list_cars+=list_cars
print(list_cars)

#列表的insert方法：list.insert(index, obj)
list_cars.insert(0,222)
print(list_cars)
#利用extend方法追加一列元素到末尾；append是追加一个；
list2=[11,22,33]
list_cars.extend(list2)
print(list_cars)

#Python index() 方法检测字符串中是否包含子字符串 str ，
#如果指定 beg（开始） 和 end（结束） 范围，则检查是否包含在指定范围内，
#该方法与 python find()方法一样，只不过如果str不在 string中会报一个异常。
print(list2.index(22))

#通过in来判断一个值是不是在列表当中；
print(11 not in list2)

list2.remove(11)
print(list2)
aa=list2.pop()
print(aa)
#列表之间他通过  +  运算符，也可以  *  运算符；
print(list2+[44,55])
print(list2)
print(list2*3)

print(abs(-4))
print(sum([2,3,4,5]))
print(sum([1,2,3,4,5],6))











