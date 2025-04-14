class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        print("I say something")

class Dog(Animal):

    def say(self):
        print(f"My name is {self.name}")

dog = Dog('Misha')
dog.say()
dog.speak()