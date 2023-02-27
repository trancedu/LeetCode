from abc import ABCMeta, abstractmethod

class Observer(metaclass=ABCMeta):
    @abstractmethod
    def update(self, notice): # once notice is updated, all observers will be notified
        pass
    
class Notice:
    def __init__(self):
        self.observers = []
    
    def attach(self, obs):
        if obs not in self.observers:
            self.observers.append(obs)
    
    def detach(self, obs):
        if obs in self.observers:
            self.observers.remove(obs)
        
    def notify(self):
        for obs in self.observers:
            obs.update(self)


class StaffNotice(Notice):
    def __init__(self, company_info=None):
        super().__init__()
        self.__company_info = company_info
    
    @property
    def company_info(self):
        return self.__company_info

    @company_info.setter
    def company_info(self, info):
        self.__company_info = info
        self.notify()
    
# obj = StaffNotice('abc')
# obj.company_info = 'xyz'
# print(obj.company_info)



class Staff(Observer):
    def __init__(self):
        self.company_info = None 
    
    def update(self, notice):
        self.company_info = notice.company_info
        
    
notice = StaffNotice("Initial Notice")
s1 = Staff()
s2 = Staff()
notice.attach(s1)
notice.attach(s2)
print(s1.company_info)
notice.company_info = "New Notice"
print(s1.company_info)
print(s2.company_info)
notice.detach(s2)
notice.company_info = "Notice 3"
print(s1.company_info)
print(s2.company_info)