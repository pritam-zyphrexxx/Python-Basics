import random

def main():

    selection = int(input("Enter your chice: "))

    if selection == 1:

        print("We are here playing a little game of : Snake - Water - Gun")

        Choice_for_g1 = input("Enter your choice: ")
        swg(Choice_for_g1)

    elif selection == 2:

        n = int(input("Enter the length of the password: "))
        password(n)

    elif selection == 3:

        dice()

    elif selection == 4:

        coin_toss()

def swg(user):

    Choices = ["Snake", "Water", "Gun"]
    random_choice = random.choice(Choices)
    user = user.capitalize()

    if user == random_choice:
        print(f"Your Choice: {user}")
        print(f"System's Choice: {random_choice}")
        print(f"It's a draw...")

    elif (user == "Gun" and random_choice == "Snake") or (user == "Snake" and random_choice == "Water") or (user == "Water" and random_choice == "Gun"):
        print(f"Your Choice: {user}")
        print(f"System's Choice: {random_choice}")
        print("You won !")

    else:
        print(f"Your Choice: {user}")
        print(f"System's Choice: {random_choice}")
        print(f"You loose !")

    main()

def main():

    selection = int(input("Enter your chice: "))

    if selection == 1:

        print("We are here playing a little game of : Snake - Water - Gun")

        Choice_for_g1 = input("Enter your choice: ")
        swg(Choice_for_g1)

    elif selection == 2:

        n = int(input("Enter the length of the password: "))
        password(n)

    elif selection == 3:

        dice()

    elif selection == 4:

        coin_toss()

