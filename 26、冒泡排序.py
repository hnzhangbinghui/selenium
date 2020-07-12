'''
概念：冒泡排序（Bubble Sort），是一种计算机领域的较简单的排序算法。
它重复地走访过要排序的数列，一次比较两个元素，如果他们的顺序错误就把他们交换过来。
走访数列的工作是重复地进行直到没有再需要交换，也就是说该数列已经排序完成。
这个算法的名字由来是因为越大的元素会经由交换慢慢“浮”到数列的顶端，故名。'''
'''算法原理:
冒泡排序算法的运作如下：（从后往前）
>比较相邻的元素。如果第一个比第二个大，就交换他们两个。
>对每一对相邻元素作同样的工作，从开始第一对到结尾的最后一对。在这一点，最后的元素应该会是最大的数。
>针对所有的元素重复以上的步骤，除了最后一个。
>持续每次对越来越少的元素重复上面的步骤，直到没有任何一对数字需要比较'''

#交=10
# 换两个数
#coding=utf-8
a=10
b=20
#设置一个临时变量c
c=a
a=b
b=c
#python里面交换还有更简单的
#a,b=b,a
print('a=',a,'b=',b)

#遍历比较相邻的数
#coding=utf-8
list=[1,333,10,7,54,78,9,24,67]
s=range(len(list)-1)
for i in s:
    for j in range(len(list)-1):
        #如果前面的数大就下沉
        if list[j]>list[j+1]:
            list[j],list[j+1]=list[j+1],list[j]
            print(j)
            print(list)
print(list)

#在python里面的排序，可以通过sort（）函数搞定
list1=[1,2,4,6,7,88,97,654,45657]
list1.sort()
print(list1)


'''random() 方法返回随机生成的一个实数，它在[0,1)范围内。
注意：random()是不能直接访问的，需要导入 random 模块，然后通过 random 静态对象调用该方法。


'''
import random
print(random.random())
print(random.random())
for i in range(6):
    print(random.randint(1,33))

print(random.randint(1,16))  #生成1到16之间的整数型随机数
print(random.random())       #生成0到1之间的随机浮点数
print(random.uniform(1.1,5.6))  #生成他们之间的随机浮点数，区间可以不是整数
print(random.choice('zhangbinghui')) #从序列中随机选取一个元素
print(random.randrange(1,100,2))  #生成1到100的间隔为2的随机整数
a=[1,3,6,8,33,45]
random.shuffle(a)    #随机排序列表
print(a)

















