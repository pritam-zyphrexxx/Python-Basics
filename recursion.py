# Practices

#  Print firt n natural numbers.....

def sfn(n):
    if (n==1):
        return 1
    return sfn(n-1) + n

n = int(input("Enter the number= "))
print(sfn(n))

#  Print pattern.....

# ***
# **
# *

def pat(n):
    if (n==0):
        return 
    print("*"*n)
    pat(n-1)
    
n = int(input("Enter the number= "))
pat(n)

# Remove a word from list and strip it at the same time.....


def ras(l, item):
    n=[]
    for item in l:
       n.append(item.strip("an"))
    return n

l=["Pritam", "Rohan", "Nayan", "uno", "apple", "an"]

print(ras(l,"an"))