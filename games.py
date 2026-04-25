import random

# Snake Water Gun game.....

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

# Random pasr generator ---------->

def password(n):
    chararcters = "qwertyuioplkjhgfdsazxcvbnmQWERTYUIOPLKJHGFDSAZXCVBNM1234567890!@#"

    password = "".join(random.sample(chararcters, n))

    print(f"Your password is: {password}")

# Dice Simlator ------------->

def dice():

    number_on_dice = random.randint(1,6)

    print(number_on_dice)

# Coin Toss ------------>

def coin_toss():

    l = ["Heads", "Tails"]
    coin_tossed = random.choice(l)

    print(coin_tossed)

# 

# Use functions ......

# Snake - Water - Gun ---------->

print("We are here playing a little game of : Snake - Water - Gun")

Choice_for_g1 = input("Enter your choice: ")
swg(Choice_for_g1)

# Random Password generatr ----------->

n = int(input("Enter the length of the password: "))
password(n)


# Dice Simlator ------------->

dice()

# Coin Toss ------------>

coin_toss()

