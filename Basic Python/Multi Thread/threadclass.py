from threading import Thread
import time 

class myThread(Thread):
    def __init__(self, name, count):
        super().__init__()
        self.count = count
        self.setName(name)
        self.setDaemon(True) # set as daemon thread, so main thread will not wait for this thread to finish
    
    def run(self):
        for i in range(self.count):
            print(f"{self.getName()} - {i}\n", end="")
            time.sleep(0.01)

thread1 = myThread("A", 10)
thread2 = myThread("B", 10)

thread1.start()
thread2.start()

print("Main Thread End")