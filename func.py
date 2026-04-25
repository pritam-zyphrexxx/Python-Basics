def avg():
    a = int(input("Enter the number= "))
    b = int(input("Enter the number= "))
    c = int(input("Enter the number= "))

    average=((a+b+c)/3)
    print(f"average = {average:.2f}")
    return average

a=avg()
print(f"{a:.2f}")

def greet(name):
    print(f"good day, {name}")
    return "done"

a= greet("Pritam")
print(a)

def fact(n):
    if (n==1 or n==0):
        return 1
    return n * fact(n-1)

n = int(input("Enter the number= "))
print(fact(n))

fact(n)


#  Practices

# Functions

# greatest number of three numbers.....
def great(a,b,c):
    if (a>b and a>c):
        print(a)
    elif (b>a and b>c):
        print(b)
    else:
        print(c)

print(great(1,2,3))

# Celsius to Fahrenheit.....

def ctf(temp):
    fh =(9*temp)/5 +32
    return fh

temp=int(input("Celcius o Fahrenheit: "))
print(f"{round(ctf(temp),2)} °F")

#  inches to centimeters.....

def itc(n):
    cm=n*2.54
    return cm

n = int(input("Enter the number= "))
print(itc(n))


#  multiplication table.....

def table(n):
    for i in range(1, 11):
        print(f"{n} X {i} = {n*i}")

n = int(input("Enter the number= "))
table(n)

