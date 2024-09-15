import tools
import os


def clear():
    return os.system("clear")


class thing:
    def __init__(self, image=""":)"""):
        self.image = image


class Container:
    def __init__(self, items: dict, size: int):
        self.items = items
        self.size = size


# things
class menu(thing):
    def __init__(self, items=["A menu:)"]):
        self.items = items
        pass


class location:
    def __init__(
        self,
        isAvailable: bool,
        things: dict = {"nothing": "nothing"},
        name="random place",
    ):
        self.name = name
        self.isAvailable = isAvailable
        self.things = things

    def __str__(self):
        return self.name


uknown = location(isAvailable=False, name="uknown")


class Person:
    def __init__(
        self,
        name="Henry",
        age=12,
        location=uknown,
        health=100,
        friends=[],
        inventory=Container(items={}, size=[10]),
        home="beng",
        action="doing nothing",
    ):
        self.name = name
        self.age = age
        self.location = location
        self.health = health
        self.friends = friends
        self.inventory = inventory
        self.home = home
        self.action = action


kummelbyPizzeriaMenu = menu()
kummelbyPizzeriaMenu.image = """
####################
##Pepperonipizza####
####################
######Calzone######
####################
#####barnpizza######
####################
####################
####################
####################
####################
"""
kummelbyPizzeriaChef = Person(name="Peter", age="52")
school = location(isAvailable=True, name="school")
kummelbyPizzeria = location(
    isAvailable=True,
    things={"menu": kummelbyPizzeriaMenu, "the chef": kummelbyPizzeriaChef},
    name="Kummelby pizzeria",
)
kjellOchCompany = location(isAvailable=True, name="Kjell och Company")
locations = {
    "school": school,
    "kummelby pizzeria": kummelbyPizzeria,
    "kjell och company": kjellOchCompany,
}


map = thing(
    image="""
            
            
            
###map###


"""
)


class Player:
    def __init__(
        self,
        name="Henry",
        age=12,
        location=school,
        health=100,
        friends=[],
        inventory=Container(items={"map": map}, size=[10]),
        home="beng",
        action="doing nothing",
    ):
        self.name = name
        self.age = age
        self.location = location
        self.health = health
        self.friends = friends
        self.inventory = inventory
        self.home = home
        self.action = action
        self.view = ""

    def walkTo(self, destination):
        if destination in locations:
            if locations[destination].isAvailable:
                self.action = f"walking to {destination}"
                print(f"walking to {destination}.")
                self.location = locations[destination]
            else:
                self.action = f"looking for {destination}"

        else:
            self.action = f"looking for {destination}"

    def prompt(self, input):
        input = input.lower()
        if input.startswith("walk to"):
            self.walkTo(input.split("walk to ")[1])
        if input == "look around":
            self.action = "looking around"
        if input.startswith("look at"):
            thing = input.split("look at ")[1]
            if thing in self.location.things:
                self.action = f"looking at {thing}"
                self.view = self.location.things[thing].image
            elif thing in self.inventory.items:
                self.action = f"looking at your {thing}"
                self.view = self.inventory.items[thing].image
        if input.startswith("pick up"):
            item = input.split("pick up ")[1]
            if item in self.location.things:
                self.action = f"picking up {item}"
                self.inventory.items.update({str(item): self.location.things[item]})
                self.location.things.pop(item)
            else:
                self.action = f"looking for {item}"


player = Player()


def intro():
    player.name = input("Name: ")
    player.age = input("Age: ")
    player.location = school
    player.health = 100
    clear()
    tools.draw(f"Welcome to Texter {player.name}!", 2, 0.5)


def render():
    indicator = "█░"
    bar = "_"
    healthBar = tools.convert_to_string(([indicator] * (int(player.health / 20))))

    if healthBar.endswith("░"):
        healthBar = healthBar + "█"
    inventory = (", ").join(player.inventory.items)
    namebar = (
        "_"
        + tools.convert_to_string([bar] * int(14.5 - (len(player.name) / 2)))
        + player.name
        + tools.convert_to_string([bar] * int(14.5 - (len(player.name) / 2)))
        + "_"
    )
    status = f"You are {player.action}"
    if player.action.startswith("walking to") or player.action == "doing nothing":
        status = f"You are at {player.location}"
        player.action = "doing nothing"
    elif player.action.startswith("picking up"):
        item = player.action.split("picking up")[1]
        player.action = "doing nothing"
        status = f"you picked up the{item}"
    elif player.action.startswith("looking around"):
        status = "You see: " + (", ").join(player.location.things)

    return (
        f"""
     {namebar}
    |health: {healthBar}        
                                   | items in inventory: {inventory}
    |{status}. 
     ______________________________|  
    """
        + player.view
    )


def runGame():
    clear()
    intro()
    clear()
    while True:
        print(render())
        player.prompt(input(": "))
        clear()
