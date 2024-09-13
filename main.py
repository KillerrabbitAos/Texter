import random
import time
import re
import tools

player_X = 0
player_Y = 0

run = True
run2 = True
run3 = True
admin = False
haveBeenAdmin = False
adminRounds = 0


def scene(number):
    import time
    if number == 1:
        print(f"Whilst {player.action} you stumble upon Mr. Pancake")
        time.sleep(1)
        current_conversation = True
        while current_conversation:
            subcommand = input("What will you say to Mr. Pancake?: ")
            print(f"{subcommand} to you too {player.name}!")
            if subcommand.lower() == "hello":
                current_conversation = False
                number = number + 1
    
    if number == 2:

        print(f"{player.name} meet a chicken!")
    
    if number == 3:
        print(f"Whilst {player.action} you stumble upon a monkey")
        time.sleep(1)
        current_conversation = True
        while current_conversation:
            subcommand = input("What will you say to it?: ")
            print(f"OhOaHHAAaa")
            


# persons
player = tools.Person("steve", 12, "school", 100, ["steve", "Alex"], [], "unknown", "doing nothing")
Steve = tools.Person("steve", 12, "home", 100, ["Alex", player.name], [], "unknown", "doing nothing")
Alex = tools.Person("steve", 12, "school", 100, ["Steve", player.name], [],
                    "unknown", "doing nothing")

# locations
school = tools.Location(True, True)
places = ["school"]
# indicators
indicator = "█░"

health_indicator_bar = (tools.convert_to_string(
    ([indicator] * (int(player.health / 10)))))

# main loops
while run:

    while run2:
        print("Welcome to Texter!")
        print("")
        print("It´s time to make your character.")
        player.name = input("Character Name: ")
        current_scene = 0
        tools.draw(f"Welcome to Texter {player.name}!", 2, 0.5)
        while run3:
            choice = (random.randint(0, 100))
            current_scene = current_scene + 1
            current_conversation = False
            player.action = "doing nothing"
            hurt = 0
            heal = 0
            health_indicator_bar = (tools.convert_to_string(
                ([indicator] * (int(player.health / 10)))))

            if current_scene == 1:
                tools.draw((f"health:{health_indicator_bar} friends:{len(player.friends)}"), 3, 1)
            else:
                print(
                f"health:{health_indicator_bar} friends:{len(player.friends)}")

            command = input("Write here: ")

            if command == "__admin__":
                subCommand = input("print OK after the semicolon to confirm, if not, just click enter;")
                if subCommand == "OK":
                    admin = True
                    haveBeenAdmin = True
                    print("you are now __admin__")
                else:
                    print("Ok. You are not __admin__")
            if command == "__deAdmin__":
                if admin:
                    subCommand = input("print OK after the semicolon to confirm, if not, just click enter;")
                    if subCommand == "OK":
                        admin = False
                        print("You are no longer __admin__")
                else:
                    print("Nothing changed. You are not __admin__")
            if command == "haveBeenAdmin?":
                if haveBeenAdmin:
                    print(f"Yes (for {adminRounds})")
                else:
                    print("No")
            

                
            
            if choice:
                Steve.location = player.location
            if command.startswith("walk to"):
                place = (command.split()[2])
                if place in places:
                    print(f"You began walking to {place}")
                    player.action = f"Walking to {player.location}"
                    player.location = place
                else:
                    player.action = f"Looking for {player.location}"

            if Steve.location == player.location:
                current_conversation = tools.Conversation([Steve])

            if command == "health":
                print(f"Your health is {player.health}.")
            if command == "location":
                print(f"Location: {player.location}")
            if command == "friends":
                print(player.friends)
            if command == "items":
                print(player.items)
            if command == "admin?":
                if admin:
                    print("yes")
                else:
                    print("no")

            scene(current_scene)


            if admin:
                if command.startswith("hurt"):
                    hurt = re.findall(r"\d", command)
                    hurt = tools.convert_to_string(hurt)
                    print(hurt)
                if command.startswith("heal") and command != "health":
                    heal = re.findall(r"\d", command)
                    heal = tools.convert_to_string(heal)
                    print(heal)

            if admin:
                adminRounds = adminRounds + 1

            player.health = player.health - int(hurt)
            player.health = player.health + int(heal)
            
            if player.location == "School":
                if school.Player_Presence == True:
                    print("You are already at school.")
                else:
                    school.Player_Presence = True
                    print("you are now at school")

