
class Animal:
    def __init__(self, name, species):
        self.name = name
        self.species = species


    def speak(self):
        return f"{self.name} says hello!"


    def describe(self):
        return f"{self.name} is a {self.species}."


dog = Animal("Buddy", "Dog")

# Call the methods
print(dog.speak())     
print(dog.describe())   
