import time
import sys
import os

class Bear:
    def __init__(self, hunger, happiness, name) -> None:
        self.hunger = hunger
        self.happiness = happiness
        self.name = name
    
    def display(self):
        output = f"{self.name} {self.hunger} {self.happiness} {self.get_image()}"
        print(output, end="\r")
    
    def update(self):
        self.hunger -= 5
        self.happiness -= 3
        
        self.hunger = max(self.hunger, 0)
        self.happiness = max(self.happiness, 0)


    def get_image(self):
        resting = "ʕ •ᴥ•ʔ"
        sad = "ʕ ´•̥̥̥ ᴥ•̥̥̥`ʔ"    
        output = ""
        if self.hunger <= 50:
             output = sad
        else:
             output = resting
        if self.happiness <= 50:
            output = sad
        else:
            output = resting
        return output
    def feed(self):
        pass

    def play(self):
        pass

def redraw_screen(bear):
    os.system("clear")
    print(f"{bear.name}")
    print(f"Hunger: {bear.hunger}")
    print(f"Happiness: {bear.happiness}")
    print(bear.get_image())
    print("---------------------------")
    print("What do you want to do?")
    print("[1] Feed")
    print("[2] Play")
    print("[3] Do nothing")
    print("[4] Quit")
    print("---------------------------")

bear_name = input("Choose a name for your bear: ")

bear = Bear(100, 100, bear_name)

def feed(self):
    self.hunger = min(self.hunger + 20, 100)

def play(self):
    self.happiness = min(self.happiness + 20, 100)

while True:
    redraw_screen(bear)

    choice = input("Choose: ")

    if choice == "1":
        bear.feed()
    elif choice == "2":
        bear.play()
    elif choice == "4":
     sys.exit(0)
    bear.update()
    bear.display()
    time.sleep(1)


#TODO: define feed and play. figure out how to have a global print so that the output constantly stays at top
