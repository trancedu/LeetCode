from abc import ABCMeta, abstractmethod

class Handler(metaclass=ABCMeta):
    @abstractmethod
    def handle_leave(self, day):
        pass
    
class GeneralManager(Handler):
    def handle_leave(self, day):
        if day <= 10:
            print(f"Leave approved by {self.__class__.__name__} for {day} days")
        else:
            print(f"Leave rejected by {self.__class__.__name__} for {day} days")

class DepartmentManager(Handler):
    def __init__(self):
        self.next = GeneralManager()
        
    def handle_leave(self, day):
        if day <= 5:
            print(f"Leave approved by {self.__class__.__name__} for {day} days")
        else:
            print(f"Not decided by {self.__class__.__name__} for {day} days")
            self.next.handle_leave(day)
        
class ProjectDirector(Handler):
    def __init__(self) -> None:
        self.next = DepartmentManager()
        
    def handle_leave(self, day):
        if day <= 3:
            print(f"Leave approved by {self.__class__.__name__} for {day} days")
        else:
            print(f"Not decided by {self.__class__.__name__} for {day} days")
            self.next.handle_leave(day)
            
day = 80
h = ProjectDirector()
h.handle_leave(day)