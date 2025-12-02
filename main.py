import time
import sys
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

bear_name = input("Choose a name for your bear: ")

bear = Bear(100, 100, bear_name)


while True:
    print("What do you want to do?")
    print("[1] Feed")
    print("[2] Play")
    print("[3] Do nothing")
    print("[4] Quit")

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


