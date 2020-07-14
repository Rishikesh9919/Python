print("Welcome to the Oregon Trail")
print("You set off with your family west.")
def survive_1():
    print("\nYou Hear a Scream. A bear attacks you and your brother.You have a choice:")
    print("a. Grab Your Gun\nb. Run for your Life")
    
    option = input("Enter your choice: ")
    if option == "a":
        print("You shoot the bear and survive.")
        return "alive"
    elif option == "b":
        print("You run away, but later bear catched you and you died.\nGame Over")
        return "dead"
    else:
        print("You Fail to do anything and you died.\nGame Over")
        return "dead"

def survive_2():
    print("\nA Mystic meets you on the road and says He's Thinking of two numbers between 1 and 10. You must guess a number between his numbers or you will die.")
    option = int(input("Enter number: "))
    if option > 4 and option < 8:
        print("You guessed right and survived.")
        return "alive"
    else:
        print("You Guessed Wrong,The mystic magic puts a splell on you and you died.\nGame Over")
        return "dead"

def survive_3():
    print("\nYou have to coss a land known for snakes.\nPick a number between 10 and 15. If you pick the unlucky number you die.\nGame Over")
    option = int(input("Enter number: "))
    if option < 10 or option > 15:
        print("You couldn't follow the rules and died.\nGame Over")
        return "dead"
    else:
        if option != 13:
            print("The snake does not attacked you and you survive.")
            return "alive"
        else:
            print("You knew that was an unlucky number. Snakes bite you and you died.\nGame Over")
            return "dead"

import random
alive = "alive"
while alive == "alive":
    survive_number = random.randint(1,3)
    if survive_number == 1:
        alive = survive_1()
    elif survive_number == 2:
        alive = survive_2()
    elif survive_number == 3:
        alive = survive_3()






    
