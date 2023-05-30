class Animal():#abstract class is one that never expect to  beinstantiated ,yet never actually except to create an instance of class.it basiclly only serve as a base class

    def __init__(self,name):#constructor of the class
        self.name=name 
    def speak(self):#as we write myanimal=animal() this never actually excepted to be instantiated.this basiclly to be only ued as a base class
        raise NotImplementedError ("subclass must implement this abstract method")      
class Dog(Animal):
    def speak(self):
        return self.name +"  say woof!"
class Cat(Animal):
    def speak(self):
        return self.name +"  say meow"   
fido=Dog("fido")
isis=Cat("isis")
print(fido.speak())
print(isis.speak())