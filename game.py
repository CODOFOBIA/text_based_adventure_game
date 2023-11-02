# build the game object
# build the character controller
# build the character tracker
# set mobility limitations
# measure the direction of character movement
import random

# character object



       

# Environment object
class Environment:
    init_env = "You are running from a horde of zombies and reached a safe house in a forest. You have no other option other than to go inside."
    def __init__(self):
        self._env = None
        # self.auto_gen_responses = ["Already there", f"I'm already in the {self.currentEnv}"]

        self.furniture = ["bed", "table", "lamp", "drawer", "stove", "lighter"]
        self.env_descr = {"bed" : "A warm and soft bed",
                        "lighter" : "Can be used to light the stove",
                        "stove" : "Can be used to cook some meal",
                        "shelter" : "Too dark, need to find a lamp"}
        
        self.inventory = ["light"]

    def entrance(self):
        if self.currentEnv != "entrance":
            print(f"{self.env_descr.get('shelter')}")
            self.currentEnv = "entrance"
            print(self.currentEnv)

        elif self.currentEnv == "entrance":
            print("Already there")

    def bedroom(self):
        if self.currentEnv != "bedroom":
            print("going upstairs")
            print(f"{self.env_descr.get('bed')}")
            self.currentEnv = "bedroom"
            print(self.currentEnv)

        elif self.currentEnv == "bedroom":
            print("Already there")

    def Basement(self):
        if self.currentEnv != "basement":
            print("going to basement")
            print("its too dark")
            self.currentEnv = "basement"
            print(self.currentEnv)

        elif self.currentEnv == "basement":
            print("Already there")
        
    def armory(self):
        if self.currentEnv != "armory":
            if "keys to armory" not in self.inventory:
                print("need to find the keys to armory")
                self.currentEnv = "basement"
                print(self.currentEnv)
            else:
                print("Armory acessed!!")
                self.currentEnv = "armory"

        elif self.currentEnv == "armory":
            print("already there")

    @property
    def currentEnv(self):
        return self._env
    
    @currentEnv.setter
    def currentEnv(self, new_env):
        self._env = new_env

    def interaction(self):

        print("searching...")
        if self.currentEnv == "entrance":
            items = ["cell", "candle", "lighter", "map", "torch"]
            self.inventory.extend(items)
            print(self.inventory)
            
        elif self.currentEnv == "basement":
            items = ["keys to armory", "gasoline can", "torch", "red tape", "baseball  bat", "large gears"]
            self.inventory.extend(items)
            print(self.inventory)
        

    
            
class Character(Environment):
    def __init__(self, name, weapon_pri = None, weapon_sec = None, third_weapon = "knife"):
        super().__init__()
        self.name = name

        self.weapon_pri = weapon_pri
        self.weapon_sec = weapon_sec
        self.third_weapon = third_weapon
        self.crafted_items = []

        self.health = 100
        self.level = 1
        self.directions = ["north", "south", "east", "west"]
        # self.user_input = input(f"Enter your move --> ").lower()


    def attack(self):
        if self.weapon_sec != None or self.weapon_pri != None:
            print("shooting...")


    def controls(self):
        while self.moves in self.directions:
            user_input = input(f"Enter your move --> ").lower()
            if user_input == "north":
                print("heading north")
            elif user_input == "south":
                print("heading south")
            elif user_input == "east":
                print("heading east")
            elif user_input == "west":
                print("heading west")
            else:
                print("Enter a valid direction")
    
    def actions(self):
        light_on = False
        if "light" in self.inventory:
            if light_on == False:
                if self.currentEnv == "entrance":
                    print("A beautifully decorated room")
                    light_on = True
                elif self.currentEnv == "basement":
                    print("a room full of access to all kinds of hardwares")
                    light_on = True
                elif self.currentEnv == "armory":
                    print("looks like this house is fully prepared to defend those walkers")
                    light_on = True
                elif light_on == True:
                    print("it is already lighted")
        else:
            print("not in inventory")
    
    def charLevel(self):
        pass

    def charHealth(self):
        pass

    def craft(self):
        pass
             

class TextBasedAdventureGame:
    def __init__(self):
        self.hero = Character("Raiyan")
        self.actions = ["light", "cook", "sleep"]

    
    def setActions(self):
        if self.hero.currentEnv != None:
            action = input(f"choose an action from {self.actions}: ")
            if action in self.actions:
                self.hero.actions()

    
    def run_game(self):
        cmd = input("Enter cmd (start/quit): ")
        print(self.hero.init_env)
        while True:
            if cmd == "start":
                move = input("your call: ")
                if "in" in move or "entrance" in move:
                    self.hero.entrance()
                    self.setActions()

                elif "bedroom" in move:
                    self.hero.bedroom()

                elif "basement" in move:
                    self.hero.Basement()
                    self.setActions()
                
                elif "armory" in move:
                    self.hero.armory()
                    self.setActions()

                elif move == "search": 
                    self.hero.interaction()
            
            elif cmd == "quit":
                confirm = input("Are you sure (y/n): ")
                if confirm == "y":
                    break
                else:
                    cmd = input("Enter cmd (start/quit): ")
    
                    

game = TextBasedAdventureGame()
game.run_game()