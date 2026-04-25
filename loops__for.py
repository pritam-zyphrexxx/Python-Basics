for i in range(1,6):
    print(i)


# Break statement...

for i in range(1,11):
    if i==5:
        break
    print(i)


# Continue statement...

for i in range(1,11):
    if i==5: # skips the number 5
        continue
    print(i)


# Pass statement...

for i in range(1,11):
    if i==5: # does nothing when i is 5
        pass
    print(i)

# Elements of a list...***1

l=["apple","banana","mango"]

for i in range(0,len(l)):
    print(l[i])

# Greet names in list starts with "s" or "S"...


l=["sneha", "pritam", "nayan", "Shubh"]

Greet='''Hello, name! 
Good Morning.'''

for i in l:
    if i.lower().startswith("s"):
        print(Greet.replace("name",i) + "\n")



# Elements of a list...***2

l=[1,2,3,4,5,]

for i in l:
    print(i)


# Sum of n natural numbers...

sum = 0
for i in range(0,10):
    sum = sum + i
print(sum)


# Factorial of a number...

fact=1

for i in range(1,10):
    fact =fact*i
print(fact)


# Print a pattern...

for i in range(1,10):
    print("*"*i)


# Print even numbers...

for i in range (1,21):
    if i%2==0:
        print(i)

# Print odd numbers...

for i in range (1,21):
    if i%2!=0:
        print(i)
else:
    print("Done")



# Chech whether the given number is prime or not...


n=int(input("enter the number: "))

if n>2: 
    for i in range(2,n):

        if n%i==0:
            print("not prime")
            break
    else:
        print("prime")

else:
    print("neither prime nor composite")



# Print multiplication table in reverse order...***1

n=10
t=[]

for i in range(1,11):
    l=f"{n} x {i} = {i*n}"
    t.append(l)
t.reverse() 

for i in range(0,len(t)):
    print(t[i])



# Print multiplication table in reverse order...***2



n=10
t=[]

for i in range(1,11):
    l=f"{n} x {i} = {i*n}"
    t.append(l)
t.reverse() 

for i in range(0,len(t)):
    print(t[i])



# Print pattern...

# *
# **
# ***


for i in range(1,4):
    print("*"*i)



# Print pattern...

#    *
#   ***
#  *****

n=int(input("enter the number: "))

for i in range(1,n+1):
    print(" "*(n-i),end="")
    print("*"*(2*i-1))

# Print hollow square pattern...

# ***
# * *
# ***

n=int(input("enter the number: "))

for i in range(1,n+1):
    if (i==1 or i==n):
        print("*"*n)

    else:
        print("*"+" "*(n-2)+"*")



# Print hollow diamond pattern...

## upper part.....

n=int(input("enter the number: "))

for i in range(1,n+1):
    if (i==1 ):
        print(" "*(n-i) + "*")
    else:
        print(" "*(n-i)+"*"+" "*(2*i-3)+"*")

## lower part.....

for i in range(n-1,0,-1):
    if (i==1):
        print(" "*(n-i)+"*")
    else:
        print(" "*(n-i)+"*"+" "*(2*i-3)+"*")


# Print hollow diamond pattern...

n=int(input("enter the number: "))

## upper part.....
for i in range(1,n+1):
    print(" "*(n-i)+ "*"*(2*i-1))

## lower part.....

for i in range(n-1,0,-1):
    print(" "*(n-i)+ "*"*(2*i-1))