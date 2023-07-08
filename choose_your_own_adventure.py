user_name = input("Type your name: ")
print("Welcome", user_name, "to your adventure")

answer = input("Your are on a dirt road, it has come to the end and you go left or right. Which way you would like to go? ").lower()

if answer == "left":
    answer = input("You come to a river, you can walk around it or swim accross? Type walk to walk, swim to swim across. ")

    if answer == "walk":
        print("You swam accross and were eaten by a crocodile.")
    elif answer == "swim":
        print("You walked for many miles, ran out of water and you lost the game.")
    else:
        print("Not a valid option. You loose. ")

elif answer == "right":
    print("")
else:
    print("Not a valid option. You loose. ")
