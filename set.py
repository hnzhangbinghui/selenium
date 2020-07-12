#set和dict类似，也是一组key的集合，但不存储value。由于key不能重复，所以，在set中，没有重复的key。
#要创建一个set，需要提供一个list作为输入集合：
s=set([1,2,3])
print(s)

#注意，传入的参数[1, 2, 3]是一个list，而显示的{1, 2, 3}只是告诉你这个set内部有1，2，3这3个元素，显示的顺序也不表示set是有序的。。

ss=set([1,2,3,2,1,2,3])
print(ss)  #重复元素在set中自动别过滤掉

#添加add方法添加元素到set
#remove()方法可以删除元素
s.add(4)
print(s)
s.remove(3)
print(s)

#set可以看成数学意义上的无序和无重复元素的集合，因此，两个set可以做数学意义上的交集、并集等操作：
print("交集:",s&ss)  #交集
print("并集:",s|ss)  #并集

#str是不变对象，而list是可变对象。
a=['c','a','b']
a.sort()
print(a)

b='abc'
print(b.replace('a','A'))
print(b)



















