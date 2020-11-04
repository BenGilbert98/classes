# Classes, objects and instantiation

# How to create a class
# Syntax: class <class_name> (capitalized)
# good naming convention is required

# Classes are a way to bring data and functionality together

class Dog:
    animal_kind = "Canine"

    # defining class variable
    def bark(self):  # self refers to current class
        return "Woof"


# In order to execute a class we have to create an object of this class
Fido = Dog()  # creating an object of our Dog class

print(Fido.animal_kind)
print(Fido.bark())

Fido.animal_kind = "Big Dog" # Changes value of animal kind for Fido object only
print(Fido.animal_kind)

Lassie = Dog() # Creating an object of our Dog class
print(Lassie.animal_kind)
print(Lassie.bark())
