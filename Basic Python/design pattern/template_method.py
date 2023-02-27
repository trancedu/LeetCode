from abc import ABCMeta, abstractmethod, ABC
import time 

class Window(metaclass=ABCMeta):
    @abstractmethod
    def start(self):
        pass
    
    @abstractmethod
    def repaint(self):
        pass
    
    @abstractmethod
    def stop(self):
        pass
    
    def run(self): # template method
        self.start()
        while True:
            try:
                self.repaint()
                time.sleep(1)
            except KeyboardInterrupt:
                break 
        self.stop()
    # did not implement the details of the methods
    
class MyWindow(Window):
    def __init__(self, msg) -> None:
        self.msg = msg
        
    def start(self):
        print('start')
    
    def repaint(self):
        print('repaint')
        print(self.msg)
    
    def stop(self):
        print('stop')

        
m = MyWindow('hello world')
m.run() 
            
            