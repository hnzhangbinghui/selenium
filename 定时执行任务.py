import time
import threading
'''第一种方法是，直接添加sleep一段时间，
缺点是，不容易控制，且sleep是堵塞函数；
def timer(n):  
    #每n秒执行一次
    while True:    
        print(time.strftime('%Y-%m-%d %X',time.localtime()))    
        yourTask()  # 此处为要执行的任务    
        time.sleep(n)
'''
'''
第二种方法：threading的Timer
'''
# def printHello():
#     print("Start...",time.strftime('%Y-%m-%d %X',time.localtime()))
#     #间隔 5 秒执行一次；
#     timer=threading.Timer(5,printHello)
#     timer.start()
# if __name__=='__main__':
#     # 5秒后执行代码
#     timer = threading.Timer(5, printHello)
#     timer.start()

'''
第三种方法：sched模块
'''
#coding='utf-8'
import os
import sched
#初始化sched模块的schedule类
#第一个参数是一个可以返回时间戳的函数，第二个参数可以在定时未到达之前阻塞
schedule=sched.scheduler(time.time,time.sleep)

def execute_command(cmd,inc):
    print('执行主程序。。。')
    #终端上显示当前计算机的连接情况
    os.system(cmd)
    schedule.enter(inc,0,execute_command,(cmd,inc))
def main(cmd,inc=60):
    #enter 四个参数分别是：间隔时间，优先级（用于同时间到达的两个事件同时执行时确定顺序），被调用的函数，给触发函数的参数（元祖形式）
    schedule.enter(0,0,execute_command,(cmd,inc))
    schedule.run()
#每60s查看一下网络连接情况
if __name__=='__main__':
    main('netstat -an',60)




#https://www.cnblogs.com/lizm166/p/8169028.html




