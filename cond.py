n=int(input("Enter a number: \n"))

if n>=18:
    print("You are eligible to vote")
elif n<0:
    print("Enter a valid age")
else:
    print("You are not eligible to vote")


# greatest number--#1

a=int(input("Enter first number: \n"))
b=int(input("Enter second number: \n"))
c=int(input("Enter third number: \n"))
d=int(input("Enter fourth number: \n"))

print(f"greatest number is: {max(a,b,c,d)}")


# greatest number--#2

num=[a,b,c,d]
m=max(num)
print(f"greatest number is: {m}")


# greatest number--#3

if a>=b and a>=c and a>=d:
    print(f"greatest number is: {a}")
elif b>=a and b>=c and b>=d:
    print(f"greatest number is: {b}")
elif c>=a and c>=b and c>=d:
    print(f"greatest number is: {c}")
else:
    print(f"greatest number is: {d}")


# spam comment...

comment=input("Enter your comment: \n")

comment=comment.lower()
if "make a lot of money".lower() in comment:
    spam=True
elif "buy now".lower in comment:
    spam=True
elif "subscribe this".lower in comment:
    spam=True
elif "click this".lower in comment:
    spam=True
else:
    spam=False
if spam:
    print("This is a spam comment")
else:
    print("This is not a spam comment") 


# Name check...

l=["nayan","saumik","hermoni","pritam","alok"]

print(len(l))

name=input("Enter your name: \n")
if name in l:
    print("Your name is present in the list")
else:
    print("Your name is not present in the list")


# 