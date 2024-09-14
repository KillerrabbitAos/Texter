import tools
import os

clear = lambda: os.system('clear')

class location:
    def __init__(self, isAvailable:bool):
        self.isAvailable = isAvailable
        


locations = {
    "school": location(isAvailable=True)
}

class Container:
    def __init__(self, items, size):
        self.items = items
        self.size = size
        
class Person:
    def __init__(self, name="Henry", age=12, location="school", health=100, friends=[], inventory=Container(items=[], size=[10]), home="beng", action="doing nothing"):
        self.name = name
        self.age = age
        self.location = location
        self.health = health
        self.friends = friends
        self.inventory = inventory
        self.home = home
        self.action = action
    def walkTo(self, destination):
        if destination in locations:
            if locations[destination].isAvailable:
                self.action = f"walking to {destination}"
                print(f"walking to {destination}.")
                self.location = destination
            else:
                self.action= f"looking for {destination}"
                
        else:
                self.action= f"looking for {destination}"
                
    def prompt(self, input):
        input = input.lower()
        if input.startswith("walk to"):
            self.walkTo(input.split("walk to ")[1])
            
    
            
        
        
player = Person()



def intro():
        player.name=input("Name: ")
        player.age=input("Age: ")
        player.location="School"
        player.health=100
        clear()
        tools.draw(f"Welcome to Texter {player.name}!", 2, 0.5)

    

def render():
    indicator = "█░"
    bar = "_"
    healthBar = (tools.convert_to_string(([indicator] * (int(player.health / 20)))))
    
    namebar = "_" + tools.convert_to_string([bar] * int(12 - (len(player.name)/2))) + player.name + tools.convert_to_string([bar] * int(12 - (len(player.name)/2))) + "_"
    
    if player.action.startswith("walking to"):
        status = f"You are at {player.location}"
    else:
        status = f"You are {player.action}"
    return (f"""
     {namebar}
    |health: {healthBar}        
                              |
    |{status}. 
     _________________________|  
    """     
    )
    
    
def runGame():
    clear()
    intro()
    clear()
    while True:
        print(render())
        player.prompt(input(": "))
        clear()
    
    


   
    
