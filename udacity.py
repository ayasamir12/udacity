import time
import random
from typing import Tuple
import sys, signal


score = 0
# COLOR = (69, 69, 69)


def exit():
    print("\nbyeeeeeeeeeee", end="")
    print(f"\033[0m", end="")
    sys.exit(0)


def signal_handler(*args):
    exit()
signal.signal(signal.SIGINT, signal_handler)


def custom_print(data: str, sep: float=0.0125, color: Tuple[int, int, int]=(198, 47, 222), safe: bool=True, *args, **kwargs):
    try:
        global COLOR
        color = COLOR
    except NameError:
        color = color

    r, g, b = color
    print(f"\033[38;2;{r};{g};{b}m", end="")
    for s in data:
        print(s, flush=True, end="")
        time.sleep(sep)
    if safe:
        print()
    return color

COLOR = custom_print("", safe=False)


def custom_input(data):
    custom_print(data, safe=False)
    return input(">> ")


from typing import Tuple
import sys, signal


score = 0
# COLOR = (69, 69, 69)


def exit():
    print("\nbyeeeeeeeeeee", end="")
    print(f"\033[0m", end="")
    sys.exit(0)


def signal_handler(*args):
    exit()
signal.signal(signal.SIGINT, signal_handler)


def custom_print(data: str, sep: float=0.0125, color: Tuple[int, int, int]=(198, 47, 222), safe: bool=True, *args, **kwargs):
    try:
        global COLOR
        color = COLOR
    except NameError:
        color = color

    r, g, b = color
    print(f"\033[38;2;{r};{g};{b}m", end="")
    for s in data:
        print(s, flush=True, end="")
        time.sleep(sep)
    if safe:
        print()
    return color

COLOR = custom_print("", safe=False)


def custom_input(data):
    custom_print(data, safe=False)
    return input(">> ")


def choice1():
    global score
    print(score, "score", flush=True)

    custom_print("You find a monster infront of your face")
    custom_print("What will you do?")
    custom_print("Enter 1 to run away from him")
    custom_print("Enter 2 to beat him with your tool")
    user_input = custom_input("Please enter 1 or 2:")

    while user_input not in ("1", "2"): user_input = custom_input("Please enter 1 or 2:")
    if user_input=="1":
        custom_print("You were caught by the monster")
        custom_print(f"You lost!")

    else:
        custom_print("You beat him , he lost consciousness")
        score += 50

        custom_print("You won!")
    play_again()


def choice2():
    global COLOR, score
    custom_print("You went inside the grave yard and found a magical wand")
    custom_print("You decide to take it to help you")
    colors = {
        'red': (255, 0, 0),
        'blue': (0, 0, 255),
        'cyan': (0, 255, 255),
        'purple': (128, 0, 128),
        'yellow': (255, 255, 0),
        'orange': (255, 165, 0)
    }
    color = random.choice(list(colors.keys()))
    r, g, b = colors[color]
    custom_print("")
    custom_print(f"Your wand color is:", safe=False)
    print(f"\033[38;2;{r};{g};{b}m", color, "\033[0m", end="", flush=True)
    custom_print("You found a ghost")
    custom_print("Enter 1 to hide from him")
    custom_print("Enter 2 cast a spell")

    user_input = custom_input("Please enter 1 or 2:")
    while (user_input) not in ("1", "2"): user_input = custom_input("Please enter 1 or 2:")

    if user_input=="1":
        custom_print("The ghost kept searching, he found you")

        custom_print("You lost!")

    else:
        custom_print("You cast a spell on him , he disappeared")

        score += 100
        custom_print("You won!")
    play_again()


def play_again():
    global score
    custom_print(f"With a score of {score}")
    choice = custom_input("Would you like to play again?")
    while (choice) not in ["yes", "no"]: choice = custom_input("Would you like to play again?")
    if choice == "yes":
        start()
    elif choice == "no":
        custom_print("Thanks for playing")
        exit()


def start():
    global score
    custom_print("Welcome to the enchanted forest,\n\
a place of mystery and wonder, you are surrounded by towering trees,\n\
their branches reaching towards the sky.")
    custom_print("But be warned, for this forest holds secrets and challenges. Hidden treasures, mythical creatures,Will you uncover the forest's mysteries?")
    custom_print("To your right there is an abandoned house")
    custom_print("Infront of you there is a grave yard")

    custom_print("In your hand you have a sharp tool")
    tools = ["Axe", "Knife", "Peeler", "Saw", "Sharp Scissors"]
    custom_print(f"Your sharp tool is: {random.choice(tools)}")
    custom_print("Enter 1 to knock on the door of the house.")
    custom_print("Enter 2 to enter the grave yard.")
    custom_print("What would you like to do?")
    choices = ("1", "2")
    user_input = custom_input("Please enter 1 or 2:")
    while (user_input) not in choices: user_input = custom_input("Please enter 1 or 2:")
    if user_input=="1":
        choice1()
    else:
        choice2()


def main():
    try:
        start()
    except Exception as e:
        print(f"Sorry, I messed up in:\n{e.with_traceback(e.args)}")
        exit()
main()
