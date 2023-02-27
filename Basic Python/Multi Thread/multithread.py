from threading import Thread
import time 

def task(count: int, **kwargs):
    print(kwargs.get("name", "thread") + " start")
    for n in range(count):
        print(n)
        time.sleep(0.01)

# 创建线程
thread1 = Thread(target=task, args=(10,), kwargs={"name": "thread1"})
thread2 = Thread(target=task, args=(20,), kwargs={"name": "thread2"})

# 启动线程
thread1.start()
thread2.start()

# 如果想要等两个完成后再执行下面的代码，可以使用join方法
thread1.join()
thread2.join()

print("Main Thread End")
