class Dog:
    def __init__(self, name, age, coat_color):
        self.name = name
        self.age = age
        self.coat_color = coat_color

    def description(self):
        print(f"{self.name} is {self.age} years old.")

    def get_info(self):
        print(f"{self.name}'s coat color is {self.coat_color}.")


class JackRussellTerrier(Dog):
    def __init__(self, name, age, coat_color, special_skill):
        super().__init__(name, age, coat_color)
        self.special_skill = special_skill

    def special_ability(self):
        print(f"{self.name} has a special skill: {self.special_skill}.")


class Bulldog(Dog):
    def __init__(self, name, age, coat_color, weight):
        super().__init__(name, age, coat_color)
        self.weight = weight

    def show_weight(self):
        print(f"{self.name}'s weight is {self.weight} kg.")


if __name__ == "__main__":
    # Creating Dog objects
    dog1 = Dog("Buddy", 3, "Brown")
    dog2 = Dog("Max", 5, "Black")

    # Calling methods of Dog class
    dog1.description()
    dog1.get_info()

    dog2.description()
    dog2.get_info()

    # Creating JackRussellTerrier object
    jack_russell = JackRussellTerrier("Jackie", 2, "White and Brown", "Agility")

    # Calling methods of JackRussellTerrier class and its parent class
    jack_russell.description()
    jack_russell.get_info()
    jack_russell.special_ability()

    # Creating Bulldog object
    bulldog = Bulldog("Rocky", 4, "White", 25)

    # Calling methods of Bulldog class and its parent class
    bulldog.description()
    bulldog.get_info()
    bulldog.show_weight()
