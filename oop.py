class Dog():
    #class object attribute
    #same for any instance of a class
    species='mammal'
    def __init__(self, breed, name):
        # user define attributes
        #we take in argument
        #assign it using self.attribute_name
        #method atrribute
        self.breed = breed
        self.name = name
        
    #Operation/Action---->method are always inside the clas and it is same like function
    def bark(self,number):#any arugment can be provided here  
        print("woof! My Name is {} and the number is {}".format(self.name,number))# number no need of self to connect with the attribute

my_dog = Dog('huskie','cute')
print(type(my_dog))
print(my_dog.breed)
print(my_dog.name)
print(my_dog.species)
print(my_dog.bark(10))
b

