
##############################
# Hello world!
##############################


from math import *


##############################
# Activity 4 - Loop "for"
##############################

##############################
# Cours

# C1 - Loop "for"

for i in range(10):
    print(i*i)


# C2 - Loop "for"

mysum = 0
for i in range(20):
    mysum = mysum + i
print(mysum)


# C3

print(list(range(10)))
print(list(range(10,20)))
print(list(range(10,20,2)))   


# C4 - Nesting of loops

for x in [10,20,30,40,50]:
    for y in [3,7]:
        print(x+y)

##############################
# Questions

# Q1 
# Cubes
for i in range(101):
    print(i**3)

for i in range(10,21):
    print(i**4)

for i in range(0,101,5):
    print(sqrt(i))


# Q2
# Powers of 2
for k in range(1,11):
    print(2**k)


# Q3
# Minimum of a function by scanning
for i in range(101):
    x = i/100
    y = x**3 - x**2 - 1/4*x + 1
    print("x =",x,"y =",y)

# Q4
# Volume of ball equal to 100
for i in range(50):
    R = i/10
    V = 4/3 * 3.14 * R**3
    print("R =",R,"V =",V)    

