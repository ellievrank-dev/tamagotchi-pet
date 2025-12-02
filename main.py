import time
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
        return resting


# --- MAIN PROGRAM --- 
bear_name = input("Choose a name for your bear: ")
bear = Bear(100, 100, bear_name)

while True:
    bear.update()
    bear.display()
    time.sleep(3)