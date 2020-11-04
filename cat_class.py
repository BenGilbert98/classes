# Create a Cat class

# one function MEOW
# create 2 class level variables
# create 3 objects
# Display all information with each object
# Change the class variable values in each object and display
# Pseudo code each block of code

class Cat:  # Creates a class of Cat with variables animal_kind and leg_number
    animal_kind = "Feline"
    leg_number = 4

    def MEOW(self):  # Defines function of meow within the class cat which returns "Meow"
        return print("MEOW")


cat1 = Cat()     # Creates 3 objects within the class of Cat
cat2 = Cat()
cat3 = Cat()


print("Cat1")
print(cat1.animal_kind)
print(cat1.leg_number)

print("Cat2")
print(cat2.animal_kind)
print(cat2.leg_number)

print("Cat3")
print(cat3.animal_kind)
print(cat3.leg_number)

cat1.leg_number = 5
cat2.leg_number = 6
cat3.leg_number = 7
print("\n")
print("New Cats")
print("\n")

print("Cat1")
print(cat1.animal_kind)
print(cat1.leg_number)

print("Cat2")
print(cat2.animal_kind)
print(cat2.leg_number)

print("Cat3")
print(cat3.animal_kind)
print(cat3.leg_number)