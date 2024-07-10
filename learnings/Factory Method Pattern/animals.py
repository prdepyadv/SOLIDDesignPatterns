"""
You task here will be to create a parameterized version of the Factory Method pattern for creating different 
types of animals with some context data.

The factory will receive a parameter to determine which animal type to create and a dictionary containing the 
context data for initializing the animal objects.
Task: Create an Animal Factory that can create different types of animals (e.g., Dog, Cat, Fish) based 
on the input parameter and context data.

1. Create an abstract Animal class.
2. Create concrete animal classes, e.g., Dog, Cat, and Fish, that inherit from the Animal class.
3. Create an AnimalFactory class with a create_animal method that takes a parameter to determine which type 
of animal to create and a dictionary containing context data for initializing the animal objects.
    a. Add such context data such as name, age to initialize the Animal data with. NOTE that we are asking 
    you to use Dictionary as the data bag for the initialization of each Animal.

4. Test the AnimalFactory class to create different types of animals.

"""

from abc import ABC, abstractmethod
from enum import Enum


# Step 0: Create an enumeration for animal types
class AnimalType(Enum):
    DOG = "Dog"
    CAT = "Cat"
    FISH = "Fish"


# Step 1: Create an abstract Animal class
class Animal(ABC):
    @abstractmethod
    def get_info(self) -> object:
        pass


# Step 2: Create concrete animal classes
class Dog(Animal):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def get_info(self):
        return self.name, self.age


class Cat(Animal):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def get_info(self):
        return self.name, self.age


class Fish(Animal):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def get_info(self):
        return self.name, self.age


# Step 3: Create an AnimalFactory class
class AnimalFactory:
    def create_animal(self, animal_type: AnimalType, context: dict) -> Animal:
        if animal_type == AnimalType.DOG:
            animal = Dog(context["name"], context["age"])
        elif animal_type == AnimalType.CAT:
            animal = Cat(context["name"], context["age"])
        elif animal_type == AnimalType.FISH:
            animal = Fish(context["name"], context["age"])
        else:
            raise ValueError("Invalid Animal Type")

        return animal


# Step 4: Test the AnimalFactory class
def main():
    animal_factory = AnimalFactory()

    dog_context = {"name": "Buddy", "age": 3}
    dog = animal_factory.create_animal(AnimalType.DOG, dog_context)
    print(dog.get_info())  # Output: ('Buddy', 3)

    cat_context = {"name": "Whiskers", "age": 2}
    cat = animal_factory.create_animal(AnimalType.CAT, cat_context)
    print(cat.get_info())  # Output: ('Whiskers', 2)

    fish_context = {"name": "Goldie", "age": 1}
    fish = animal_factory.create_animal(AnimalType.FISH, fish_context)
    print(fish.get_info())  # Output: ('Goldie', 1)


if __name__ == "__main__":
    main()
