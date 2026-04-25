# i=1

i=1
while(i<6):
    print(i)
    i+=1


# Elements of a list...

l=["apple","banana","mango"]

i=0

while(i<len(l)):
    print(l[i])
    i+=1


# Sum of n natural numbers...

n=int(input("Enter a number: "))

i=1
sum=0

while(i<=n):
    sum=sum+i
    
    i+=1

print(sum)

# Factorial of a number...

n=int(input("Enter a number: "))

fact=1

i=1

while(i<=n):
    fact=fact*i
    i+=1
print(fact)

# Print a pattern...

n=int(input("Enter a number: "))

i=1

while(i<=n):
    print("\\"*i)
    i+=1


