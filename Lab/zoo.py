class Zoo:
    __animals = 0

    def __init__(self, name:str):
        self.name = name
        self.mammals = []
        self.fishes = []
        self.birds = []

    def add_animal(self, species, name):
        if species == "mammal":
            self.mammals.append(name)
        elif species == "fish":
            self.fishes.append(name)
        elif species == "bird":
            self.birds.append(name)
        Zoo.__animals += 1

    def get_info(self, species):
        type_of_animals = ""
        if species == "mammal":
            type_of_animals = f"Mammals in {self.name}: {', '.join(self.mammals)}\nTotal animals: {Zoo.__animals}"
        elif species == "fish":
            type_of_animals = f"Fishes in {self.name}: {', '.join(self.fishes)}\nTotal animals: {Zoo.__animals}"
        elif species == "bird":
            type_of_animals = f"Birds in {self.name}: {', '.join(self.birds)}\nTotal animals: {Zoo.__animals}"

        return type_of_animals

zoo_name = input()
zoo = Zoo(zoo_name)
number_of_lines = int(input())

for _ in range(number_of_lines):
    type_and_animal = input()
    type_, animal = type_and_animal.split()
    zoo.add_animal(type_,animal)

species_type = input()
print(zoo.get_info(species_type))