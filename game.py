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
                        "shelter" : "A well decorated spacious room",
                        "basement": "Looks like this is place is well suited to defy the chaos outside"}
        
        self.inventory = ["light"]
        self.enemies = False

    def entrance(self):
        if self.currentEnv != "entrance":
            print(self.env_descr.get('shelter'))
            self.currentEnv = "entrance"
            print(self.currentEnv)

        elif self.currentEnv == "entrance":
            print("Already there")

    def bedroom(self):
        if self.currentEnv != "bedroom":
            print("going upstairs")
            print(self.env_descr.get('bed'))
            self.currentEnv = "bedroom"
            print(self.currentEnv)

        elif self.currentEnv == "bedroom":
            print("Already there")

    def Basement(self):
        if self.currentEnv != "basement":
            print("going to basement")
            print(self.env_descr.get('basement'))
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
                self.currentEnv = "armory"
                print("The armory doors slowly slid open")
                print("among the weapon hangers and tables a zombie sprang onto me")

        elif self.currentEnv == "armory":
            print("already there")

    @property
    def currentEnv(self):
        return self._env
    
    @currentEnv.setter
    def currentEnv(self, new_env):
        print(f"Setting environment to {new_env}")
        self._env = new_env

    def interaction(self):

        print("searching...")
        if self.currentEnv == "entrance":
            items = ["cell", "candle", "lighter", "map", "torch"]
            self.inventory.extend(items)
            print(f"found: {items}")
            
        elif self.currentEnv == "basement":
            items = ["keys to armory", "gasoline can", "torch", "red tape", "baseball  bat", "large gears"]
            self.inventory.extend(items)
            print(f"found: {items}")
        
        elif self.currentEnv == "armory":
            items = ["9mm glock 20", "band aids", "9mm mags"]
            self.inventory.extend(items)
            
    
        

    
            
class Character():
    def __init__(self, name, weapon_pri = None, weapon_sec = None, third_weapon = "knife"):
        self.name = name

        self.weapon_pri = weapon_pri
        self.weapon_sec = weapon_sec
        self.third_weapon = third_weapon
        self.crafted_items = []

        self.health = 100
        self.level = 1
        self.directions = ["north", "south", "east", "west"]
        self.actions = ["attack", "dodge", "fall back", "shoot"]
        self.env = Environment()


    def controls(self):
        while True:
            user_input = input(f"Enter your move --> ").lower()
            if user_input in self.directions:
                print(f"heading {user_input}")
            else:
                print("Enter a valid direction")
    
    def set_actions(self):
        print(f"Current environment: {self.env.currentEnv}")  # Debugging line
        if self.env.currentEnv == "armory":
            print("after")
            act = input(f"what would you like to do? {self.actions} ").strip().lower()
            if act == "attack":
                if self.weapon_pri is not None or self.weapon_sec is not None or self.third_weapon is not None:
                    print("With chilling precision you blew its head off saving yourself")
                else:
                    print("You died")
            elif act == "dodge":
                print("You died")
            elif act == "fall back":
                print("you died")
        else:
            print("before")

    def charLevel(self):
        pass

    def charHealth(self):
        pass

    def craft(self):
        pass
             

class TextBasedAdventureGame():
    def __init__(self):
        self.hero = Character("Raiyan")
        # self.env = Environment()
        
 
    def run_game(self):
        cmd = input("Enter cmd (start/quit): ")
        print(self.hero.env.init_env)  # Access the Environment instance through the Character's env attribute
        while True:
            if cmd == "start":
                move = input("your call: ")
                if "in" in move or "entrance" in move:
                    self.hero.env.entrance()

                elif "bedroom" in move:
                    self.hero.env.bedroom()

                elif "basement" in move:
                    self.hero.env.Basement()
                    
                elif "armory" in move:
                    self.hero.env.armory()
                    self.hero.set_actions()

                elif move == "search":
                    self.hero.env.interaction()

            elif cmd == "quit":
                confirm = input("Are you sure (y/n): ")
                if confirm == "y":
                    break
                else:
                    cmd = input("Enter cmd (start/quit): ")
    
                    

game = TextBasedAdventureGame()
game.run_game()