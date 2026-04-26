import random


# File opening for reading only.....

f = open("Text files/file.txt") # Same as f = open("file.txt", "r")
data = f.read()
print(data)

read = f.readlines()  # It do read a file's every line ----> line - by - line
print(read, type(read))

line1 = f.readline()  # It do read a file's each line at a time
print(line1, type(line1))
line2 = f.readline()  # It do read a file's each line at a time
print(line2, type(line2))

f.close()

# File opening for writing.....

s = "My name is Pritam Raj.\nI'm trying file writing with python."

f2 = open("file1.txt", "w") # "w" ------> opens file in write mode.....
f2.write(s)
f2.close()

# File opening for appending.....

f3 = open("Text files/file.txt", "a") # "a" ------> adds the given in the end of the file.....

f3.write(f"{s}\n")

f3.close()



#  Using with statement we don't have to close file explicitely.....

with open("Text files/file-with.txt") as f:
    print(f.read())

#  checking occurance of a word in a file.....

s='''Twinkle twinkle little star,
how I wonder what you are...'''

with open("Text files/poem.txt") as p:
    c = p.read()
    print(c)
    
    if ("twinkle" in c.lower()):
        print(f"Yes it is !")
    else:
        print(f"Oops !")

# adding a gamescore and further appending and updating high scores......

def game():
    
    random_number = random.randint(1,100)

    guessed = int(input("Enter your guess [between 1 to 100]: "))
    no_of_guesses = 1


    while not (guessed>=1 and guessed<=100):
        guessed = int(input("Guess within 1 to 100: "))
        
    while(random_number != guessed):
        if(random_number > guessed):
            guessed = int(input(f"Guess higher than {guessed}: "))
        else:
            guessed = int(input(f"Guess lower than {guessed}: "))
        no_of_guesses += 1
        

    print("You guessed it correct.")
    print(f"System guessed: {random_number}")
    print(f"Total Guesses: {no_of_guesses}")

    score = no_of_guesses

    with open("Text files/high-score.txt", "a") as hs:
        hs.write(f"New high score is: {score}\n")

    return score

game()

# Saving multiplication table of 2 to 20 and saving it in different files in a folder......

def mult():
    for i in range (2, 21):
        to_be_saved = ""

        print(f"Multiplication table of {i}")

        for j in range(1,11):
            line = (f"{i} X {j} = {i*j}")
            print(line)
            to_be_saved += f"{line} \n"


        with open(f"Text files/table/multiplication table of {i}.txt", "w") as t:
            t.write(to_be_saved)

mult()

# replacing a word from a file....

word = "donkey"
with open("Text files/file2.txt", "r") as f:
    s = f.read()
    s1 = s.lower().replace(word, "######")


with open("Text files/file2.txt", "w")as r:
    r.write(s1)

# now replacing a list of censored words from the file......

words = ["donkey", "fool", "idiot", "stupid", "dumb", "rubbish", "trash", "nonsense", "silly", "useless"]
with open("Text files/file2.txt", "r") as f:
    s = f.read()
    
for word in words:
    s = s.lower().replace(word, "#"*len(words))


with open("Text files/file2.txt", "w")as r:
    r.write(s)


# checking if a string is in the given file or not.....

with open("Text files/file.txt") as f:
    content = f.read()

    if "Python".lower() in content:
        print(f"Yes it contains !")
    else:
        print(f"No, it doesn't contains !")

# checking the line no. of a string.....

with open("Text files/file.txt") as f:
    content = f.readlines()

lineno = 1
for line in content:
    if "python" in line:
        print(f"Yes it contains !, Line number is: {lineno}")
        break
    lineno +=1
else:
    print(f"No, it doesn't contains !")

# renaming a file.....

