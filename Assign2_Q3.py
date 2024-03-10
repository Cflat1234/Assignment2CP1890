from dataclasses import dataclass

@dataclass

#animal class with species and name attributes. defaults are ""
class Animal:
    name: str = ""
    species: str = ""

#property to get the name
    @property
    def get_name(self):
        return self.name

    @get_name.setter
    def get_name(self, value):
        self.name = value

#property to get the species
    @property
    def get_species(self):
        return self.species

    @get_species.setter
    def get_species(self, value):
        self.species = value

#speak method (had return instead of print so it would print properly in the final ouput)
    def speak(self):
        return "*Animal sound*"

#dog child class with a breed attribute and default of ""
@dataclass
class Dog(Animal):
    breed: str = ""

#property to get the dog breed
    @property
    def get_breed(self):
        return self.breed

    @get_breed.setter
    def get_breed(self, value):
        self.breed = value

#overwriting the speak method
    def speak(self):
        return "Woof!"

#same thign with the cat class, except it has a color attribute with a default of ""
@dataclass
class Cat(Animal):
    color: str = ""

    def speak(self):
        return "Meow!"

#main
def main():
    #instanciating the classes and provinding data
    dog = Dog("Max", "Dog", "Golden Retriver")
    cat = Cat("Whiskers","Cat", "Orange")

#printing the output
    print("Dog: ")
    print(f"Name: {dog.name}")
    print(f"Species: {dog.species}")
    print(f"Breed: {dog.breed}")
    print(f"Sound: {dog.speak()}")

    print("\nCat:")
    print(f"Name: {cat.name}")
    print(f"Species: {cat.species}")
    print(f"Color: {cat.color}")
    print(f"Sound: {cat.speak()}")

if __name__ == "__main__":
    main()

