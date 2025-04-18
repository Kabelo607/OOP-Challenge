class Pet:
    def __init__(self, name):
        self.name = name
        self.hunger = 5      
        self.energy = 5
        self.happiness = 5

    def eat(self):
        self.hunger = max(0, self.hunger - 3)
        self.happiness = min(10, self.happiness + 1)

    def sleep(self):
        self.energy = min(10, self.energy + 5)

    def play(self):
        self.energy = max(0, self.energy - 2)
        self.happiness = min(10, self.happiness + 2)
        self.hunger = min(10, self.hunger + 1)

    def get_status(self):
        print(f"Pet: {self.name}")
        print(f"Hunger: {self.hunger} (0 = full, 10 = very hungry)")
        print(f"Energy: {self.energy} (0 = tired, 10 = fully rested)")
        print(f"Happiness: {self.happiness} (0-10)")

bobby = Pet("Bobby")



bobby.eat()

bobby.sleep()

bobby.play()

bobby.get_status()