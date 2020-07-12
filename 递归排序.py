'''
1,递归用一种通俗的话来说就是自己调用自己，但是需要分解它的参数，
2,让它解决一个更小一点的问题，当问题小到一定规模的时候，
3,需要一个递归出口返回。'''


#阶乘

#coding=utf-8



def fact(n):
    if n==0:
        return 1
    else:
        return n*fact(n-1)
a=input("请输入阶乘的数：")
print(fact(int(a)))





























