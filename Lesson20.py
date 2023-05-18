# Polymorphism

# խնդիր 1
class Animal:
    def __init__(self, name, age, foot_count):
        self.name = name
        self.age = age
        self.foot_count = foot_count

    def __str__(self):
        return "Animals"


class Monkey(Animal):
    def __init__(self, sound, name, age, foot_count):
        Animal.__init__(self, name, age, foot_count)
        self.sound = sound

    def print(self):
        print("Monkey have", "\nsound:", self.sound, "\nname:", self.name, "\nage:", self.age, "\nfoot count:",
              self.foot_count)


class Donkey(Animal):
    def __init__(self, sound, name, weight, foot_count):
        Animal.__init__(self, name, weight, foot_count)
        self.sound = sound
        self.weight = weight

    def print(self):
        print("Donkey have", "\nsound:", self.sound, "\nname:", self.name, "\nweight:", self.weight, "\nfoot_count:",
              self.foot_count)


donkey = Donkey("bray", "Rex", 46, 4)
donkey.print()
monkey = Monkey("calls, screams, hoots, barks, and chatters", "King-kong", 12, 4)
monkey.print()


# խնդիր 2
class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def max_speed(self):
        return "I Dont know yet"


class BMW(Car):
    def __init__(self, brand, model):
        Car.__init__(self, brand, model)

    def max_speed(self):
        return "The maximum speed of the BMW is 346 km/h"


class Ferrari(Car):
    def __init__(self, brand, model):
        Car.__init__(self, brand, model)

    def max_speed(self):
        return "The maximum speed of the Ferrari is 350 km/h"


bmw = BMW("BMW", "E60")
print(bmw.max_speed())
print("Model of BMW-", bmw.model)
ferrari = Ferrari("Ferrari", "LaFerrari")
print(ferrari.max_speed())
print("Model of Ferrari-", ferrari.model)




class Cat:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def info(self):
        print(f"I am a cat. My name is {self.name}. I am {self.age} years old.")

    def make_sound(self):
        print("Meow")


class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def info(self):
        print(f"I am a dog. My name is {self.name}. I am {self.age} years old.")

    def make_sound(self):
        print("Bark")


cat1 = Cat("Kitty", 2.5)
dog1 = Dog("Fluffy", 4)
print(type(cat1))
print(type(dog1))

for animal in (cat1, dog1):
    animal.make_sound()
    animal.info()
    animal.make_sound()
