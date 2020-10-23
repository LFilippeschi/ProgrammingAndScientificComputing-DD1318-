
import my_module

# Uppgift 1

""" y = 222
x = 111
x_list = [111, 222, 333, 444]
print("Outside module: x=" + str(x) + " and x_list=" + str(x_list) + " and y=" + str(y))
my_module.scope_testing_function(x, x_list)
print("Outside module: x=" + str(x) + " and x_list=" + str(x_list) + " and y=" + str(y))
 """

# Uppgift 2
""" x=1
print(my_module.my_function(x))
 """
# Uppgift 3

""" print(my_module.roll_dice(20))
 """
# Uppgift 4

""" l= [2,5,1,7,1,4,10,0,-5]
print(l)
my_module.my_sort_list(l)
print(l) """

# Uppgift 5
""" message = input("Enter a message: ")
message = my_module.bandit_language(message)
print(message) """

# Uppgift 6


def make_bandit_dictionary(d):
    for x in d:
        for i in range(len(d[x])):
            d[x][i] = my_module.bandit_language(d[x][i])
    return d


animals = {'tiger': ['claws', 'sharp teeth', 'four legs', 'stripes'],
           'elephant': ['trunk', 'four legs', 'big ears', 'gray skin'],
           'human': ['two legs', 'funny looking ears', 'a sense of humor']
           }
# print(animals)
# make_bandit_dictionary(animals)
# print(animals)

# Uppgift 6
