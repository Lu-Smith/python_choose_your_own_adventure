user_name = input("Type your name: ")
print("Welcome", user_name, "to your adventure")

answer = input("Your are on a dirt road, it has come to the end and you go left or right. Which way you would like to go? ").lower()

if answer == "left":
    answer = input("You come to a river, you can walk around it or swim accross? Type walk to walk, swim to swim across. ")

    if answer == "swim":
        print("You swam accross and were eaten by a crocodile.")
    elif answer == "walk":
        print("You walked for many miles, ran out of water and you lost the game.")
    else:
        print("Not a valid option. You loose. ")

elif answer == "right":
    answer = input("You come to a bridge it looks wobbly, do you want to cross it or head back? (cross/back) ")

    if answer == "cross":
        answer = input("You cross the bridge and you meet a stranger. Do you talk to them? (yes/no) ")

        if answer == "yes":
            print("You talk to the stranger and they gave you a gold. You won!")
        elif answer == "no":
            print("You ignore the stranger, and he killed you. You lost.")
        else:
            print("Not a valid option. You loose. ")

    elif answer == "back":
        print("You go back and loose.")
    else:
        print("Not a valid option. You loose. ")
else:
    print("Not a valid option. You loose. ")


print("Thank you for trying!")