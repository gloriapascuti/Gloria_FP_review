
class Animal:

    def __init__(self, name, race):
        self.race = race
        self.name = name

    def speak(self):
        pass

    def talk(self):
        return f"Example of Animal speaking: {self.name} {self.race} {self.speak()}"

# class

class Dog(Animal):
    def __init__(self, name, race):
        super().__init__(name, race)

    def speak(self):
        return "bark bark i'm a dog"


if __name__ == '__main__':
    bully: Animal = Animal("BOB", "Americal Bully")
    print(bully.talk())
    bully = Dog("BOB", "Americal Bully")
    print(bully.talk())

    pass