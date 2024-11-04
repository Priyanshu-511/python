class Animal:
    def __init__(self, Name):
        self.Name = Name

class Pet:
    def __init__(self, walking):
        self.walking = walking

class Wild:
    def __init__(self, walking):
        self.walking = walking

class Dog(Animal, Pet):
    def __init__(self, Name, walking):
        Animal.__init__(self, Name)
        Pet.__init__(self, walking)

dog = Dog("Buddy", "Four foot")
print(f"Name: {dog.Name},\nWalking: {dog.walking}")
