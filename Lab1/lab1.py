import math as m
import numpy as np

# UPPGIFT 1

nice_name = "Kim"
print(nice_name)
long_name = ""
for i in range(33):
    long_name = long_name+nice_name
print(long_name)


# UPPGIFT 2
x = str(input("Vad heter du?"))
for i in range(39):
    print(x)

# UPPGIFT 3

while True:
    x = str(input("Vad heter du? "))
    if x==0:
        break
    if "Sauron" == x:
        print("Hej då")
        break
    else:
        print("Hej " + x)


#  UPPGIFT 4

print(1==0.99)
print(1==0.9999999)
print(1==0.99999999999999999)

# UPPGIFT 5

x = int(input("Enter number n: "))
value = (m.pi**2)/6
approx = 0
for i in range(1, x):
    approx += 1/(i**2)
print("Exact value= ", value)
print("Approximate value: ", approx)
