from abc import ABC, abstractmethod
class Absclass(ABC):
    def print(self,x):
        
        print("passed value", x)
    
    @abstractmethod
    def task(self):
        print("WE are inside absclass/ diddy party")
    
class testClass(Absclass):
    def task(self):
        print("We are inside text_class task")

testObj = testClass()
testObj.task()

testObj.print(100)

print()
o1 = Absclass()
o1.task