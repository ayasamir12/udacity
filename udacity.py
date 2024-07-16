
import time
import random
def choice1():
       score = 0
       #if player score is 0 he loses
       print("You find a monster infront of your face")
       print("What will you do?")
       time.sleep(2)
       print("Enter 1 to run away from him")
       time.sleep(2)
       print("Enter 2 to beat him with your tool")
       user_input=input("Please enter 1 or 2:")
       while True:
           if user_input=="1" or user_input=="2":
               break
           user_input=input("Please enter 1 or 2:")
       if user_input=="1":
           print("You were caught by the monster")
           time.sleep(2)
           print("You lost!")
           
           time.sleep(2)
       else:
           print("You beat him , he lost consciousness")
           score += 50
           #you earned 50 points
           time.sleep(2)
           print("You won!")
       play_again()    
def choice2():
    print("You went inside the grave yard and found a magical wand")
    time.sleep(2)
    print("You decide to take it to help you")
    time.sleep(2)
    colors = ["red", "blue", "cyan", "purple", "yellow", "orange"]
    random.choice(colors)
    print("Your wand color is:", random.choice(colors))
    time.sleep(2)
    print("You found a ghost")
    time.sleep(2)
    print("Enter 1 to hide from him")
    time.sleep(2)
    print("Enter 2 cast a spell")
    user_input=input("Please enter 1 or 2:")
    while True:
         if user_input=="1" or user_input=="2":
             break
         user_input=input("Please enter 1 or 2:")
    if user_input=="1":
        print("The ghost kept searching, he found you")
        time.sleep(2)
        print("You lost!")
        time.sleep(2)
    else:
        print("You cast a spell on him , he disappeared")
        time.sleep(2)
        print("You won!")
    play_again()
def play_again():
    choice = input("Would you like to play again?")
    while choice not in ["yes", "no"]:
        choice = input("Would you like to play again?")
    if choice == "yes":
        start()
    elif choice == "no":
        print("Thanks for playing")
def start():
    print("Welcome to the enchanted forest, a place of mystery and wonder, you are surrounded by towering trees, their branches reaching towards the sky.")
    time.sleep(2)
    print("But be warned, for this forest holds secrets and challenges. Hidden treasures, mythical creatures,Will you uncover the forest's mysteries?")
    time.sleep(2)
    print("To your right there is an abandoned house")
    time.sleep(2)
    print("Infront of you there is a grave yard")
    score += 100
    #your intial score is 100 points
    time.sleep(2)
    print("In your hand you have a sharp tool")
    tools = ["Axe", "Knife", "Peeler", "Saw", "Sharp Scissors"]
    random.choice(tools)
    print("Your sharp tool is:" ,random.choice(tools) )
    time.sleep(2)
    print("Enter 1 to knock on the door of the house.")
    time.sleep(2)
    print("Enter 2 to enter the grave yard.")
    time.sleep(2)
    print("What would you like to do?")
    user_input=("Please enter 1 or 2:")
    while True:
        if user_input=="1" or user_input=="2":
            break
        user_input=input("Please enter 1 or 2:")
    if user_input=="1":
        choice1()
    else:
        choice2()
start()    
        
        