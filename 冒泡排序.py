list=[1,33,10,7,54,78,9,24,67,100]
s=range(len(list)-1)
for i in range(len(list)-1):
    for j in range(len(list)-1):
        #如果前面的数大就下沉
        if list[j]>list[j+1]:
            list[j],list[j+1]=list[j+1],list[j]
print(list)
import random





'''
list2=[1,33,10,7,54,78,9,24,67,100]
print(list2.sort())
print(list2)

a=[1,2,3,4,5,6,7,8,9]

random.shuffle(a)
print(a)

print(random.choice("zhangbinghui"))
print(random.sample("zhangbinghui",4))
print(random.randrange(1,100,6))

'''
