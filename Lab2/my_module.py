
import copy
import math
import random

# Uppgift 1

def scope_testing_function(x, x_list):
    print("Inside function: x=" + str(x) + " and x_list=" + str(x_list) + " and y=" + str(y))
    x = 1
    x_list[0] = 1
    print("Inside function: x=" + str(x) + " and x_list=" + str(x_list) + " and y=" + str(y))
    x_list = [1, 2, 3, 4]
    print("Inside function: x=" + str(x) + " and x_list=" + str(x_list) + " and y=" + str(y))
    return x

x_list = [11, 22, 33, 44]
x = 11
y = 22
print("Outside function: x=" + str(x) + " and x_list=" + str(x_list) + " and y=" + str(y))

scope_testing_function(x, x_list)
print("Outside function: x=" + str(x) + " and x_list=" + str(x_list) + " and y=" + str(y))

# Uppgift 2

def my_function(x):
    return math.sin(x)**2 + x*x


# Uppgift 3

def roll_dice(n):
    return random.randint(1,n)

# Uppgift 4


def my_sort_list(l):
    for j in range(len(l)):
        for i in range(len(l)-j-1):
            if l[i] > l[i+1]:
                tmp = l[i+1]
                l[i+1] = l[i]
                l[i] = tmp
    return l


# Uppgift 5


def bandit_language(s):
    tmp = ""
    for i in range(len(s)):
        if (s[i] == 'a' or s[i] == 'e' or s[i] == 'i' or s[i] == 'o' or s[i] == 'u' or ord(s[i]) < 97 or ord(s[i]) > 122):
            tmp += s[i]
        else:
            tmp += s[i] + 'o' + s[i]
    return tmp
