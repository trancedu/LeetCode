from abc import ABCMeta, abstractmethod
class Subject(metaclass=ABCMeta):
    @abstractmethod
    def get_content(self):
        pass 
    
    @abstractmethod
    def set_content(self, content):
        pass
    
class RealSubject(Subject):
    def __init__(self, filename):
        self.filename = filename
        with open(self.filename, "r") as f:
            print("Read file from disk")
            self.content = f.read()
    
    def get_content(self):
        return self.content 
    
    def set_content(self, content):
        with open(self.filename, "w") as f:
            f.write(content)
        self.content = content
    
# sub = RealSubject("test.txt")
# sub.get_content()

# Save memory cost by using virtual proxy
class VirtualProxy(Subject):
    # 构造时不调用真实对象的构造函数
    def __init__(self, filename):
        self.filename = filename
        self.subj = None 
    
    def get_content(self):
        if not self.subj:
            self.subj = RealSubject(self.filename)
            return self.subj.get_content()
        return self.subj.get_content()
    
    def set_content(self, content):
        if not self.subj:
            self.subj = RealSubject(self.filename)
        self.subj.set_content(content)

print(VirtualProxy("test.txt").get_content())

class ProtectedProxy(Subject):
    def __init__(self, filename):
        self.subj = RealSubject(filename)
    
    def get_content(self):
        return self.subj.get_content()
    
    def set_content(self, content):
        raise PermissionError("You don't have permission to set content")

subj = ProtectedProxy("test.txt")
print(subj.get_content())
# subj.set_content("Hello World")