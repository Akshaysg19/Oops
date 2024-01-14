class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        pass

class Dog(Animal):  # Inheriting from the Animal class
    def bark(self):
        print("Woof!")

class Cat(Animal):  # Inheriting from the Animal class
    def meow(self):
        print("Meow!")

my_dog = Dog("Buddy")
my_cat = Cat("Whiskers")

my_dog.bark()