from threading import Thread
from queue import Queue

class MsgProducer(Thread):
    def __init__(self, name, queue, count):
        super().__init__()
        self.setName(name)
        self.queue = queue
        self.count = count
    
    def run(self):
        for i in range(self.count):
            print(f"{self.getName()} Sent {i}\n", end="")
            self.queue.put(f"{self.getName()} - {i}", block=True)
    
class MsgConsumer(Thread):
    def __init__(self, name, queue):
        super().__init__()
        self.setName(name)
        self.queue = queue
        self.setDaemon(True)
    
    def run(self):
        while True:
            msg = self.queue.get(block=True)
            print(f"{self.getName()} Received {msg}\n", end="")

queue = Queue(maxsize=3)
p1 = MsgProducer("Producer1", queue, 10)
p2 = MsgProducer("Producer2", queue, 10)
p3 = MsgProducer("Producer3", queue, 20)
r1 = MsgConsumer("Consumer1", queue)
r2 = MsgConsumer("Consumer2", queue)
threads = [p1, p2, p3, r1, r2]
for t in threads:
    t.start()
    
for p in threads:
    if isinstance(p, MsgProducer):
        p.join()
        
print("Main Thread End\n", end="")
# If main thread ends, r1 and r2 will end because they are daemon threads
# So we need to wait for p1, p2 and p3 to finish, then end main thread