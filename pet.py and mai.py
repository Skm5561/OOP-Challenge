
class Pet:
    def __init__(self, name="Pegion"):
        self.name = name
        self.hunger = 5
        self.energy = 5
        self.happiness = 5
        self.tricks = []

    def eat(self):
        self.hunger = max(self.hunger - 3, 0)
        self.happiness = min(self.happiness + 1, 10)
        print(f"{self.name} ate some food. Yum! Happiness increased!")

    def sleep(self):
        self.energy = min(self.energy + 5, 10)
        print(f"{self.name} took a nap. Energy restored!")

    def play(self):
        if self.energy >= 2:
            self.energy -= 2
            self.happiness = min(self.happiness + 2, 10)
            self.hunger = min(self.hunger + 1, 10)
            print(f"{self.name} played and had fun!")
        else:
            print(f"{self.name} is too tired to play. Let them rest!")

    def get_status(self):
        print(f"\n--- {self.name}'s Status ---")
        print(f"Hunger: {self.hunger}/10")
        print(f"Energy: {self.energy}/10")
        print(f"Happiness: {self.happiness}/10")
        print("----------------------------\n")

    def train(self, trick):
        self.tricks.append(trick)
        self.happiness = min(self.happiness + 1, 10)
        print(f"{self.name} learned a new trick: {trick}!")

    def show_tricks(self):
        print(f"\n{self.name}'s Tricks:")
        if self.tricks:
            for trick in self.tricks:
                print(f"• {trick}")
        else:
            print("No tricks learned yet.")
        print()




main.py

 from pet import Pet

def main():
    pegion = Pet()  # Creates a Pet object named Pegion

    pegion.get_status()      # Check initial status
    pegion.eat()             # Feed Pegion
    pegion.sleep()           # Let Pegion rest
    pegion.play()            # Let Pegion play
    pegion.train("spin")     # Teach a trick
    pegion.train("fly in circles")
    pegion.show_tricks()     # Show learned tricks
    pegion.get_status()      # Final status update

if __name__ == "__main__":
    main()



