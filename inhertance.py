class Animal():#base class
    def __init__(self):
      print("Animal Created")
    def who_am_i(self):#method
       print("Iam an animal")
    def eat(self):#method
       print("I am eating")
class Dog(Animal): #it will inherit the method of anmial class.matlb animal ka method operation or action inherit karega dog class{derived class }
   def __init__(self):
      Animal.__init__(self)#create instance of animal class
      print("Dog created")
   def who_am_i(self):#overwritten in new class
       print("Iam a DOG") 
   def eat(self):#method of new class
       print("I am a Dog and eating")
   def bark( self):#its own method of new class
       print("woof!")
mydog=Dog()           
myanimal=Animal()
myanimal.eat()
myanimal.who_am_i()
mydog.bark()
mydog.eat()#in dog class we dont have the eat or who am i method.i was able to derive them from my base class of animal
        # this is the main idea of inheritance
mydog.who_am_i()#here the output is i am a dog if its is overwriten in new class