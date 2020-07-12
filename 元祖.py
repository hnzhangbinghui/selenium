#Python的元组与列表类似，不同之处在于元组的元素不能修改。
#元祖是小括号表示
#元祖比较简单，只需要在括号中添加元素，并使用都好隔开即可

tup1=()
print(tup1)

tup2=(1,2,3)
print(tup2)
print(tup2[1])

#元祖的值不能修改，但是可以对元祖进行连接组合

tup3=('aaa','sss','ddd')
tup4=tup2+tup3
print(tup4)

tup4=tup4+tup4
print(tup4)

