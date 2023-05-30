class Dog():
    def __init__(self,name):
        self.name=name
    def speak(self):
        return self.name+" says woof!"
    
class Cat():
    def __init__(self,name):
        self.name=name
    def speak(self):
        return self.name+" says meow"
niko=Dog("niko")#instance of class
felix=Cat("FELIX")#instance of class
#we can show by iteration polymorphism
for pet in[niko,felix]:#we can say pet speak so this take in some pet ,it doesnt really care if its dog or cat because whta its going to do inside of the function is just take pet object and then call it to speak
    print(type(pet))
    print(pet.speak())#polymorphism:both nikko and felix share same  method name speak
# we can show plymorphism by function and this is more commonly use
def pet_speak(pet):#it doesnot care its dog or cat it just go inside the function speak
    print(pet.speak())
pet_speak(niko)
pet_speak(felix)

print(niko.speak())
print(felix.speak())