#%%

from numpy import _2Tuple


i = 0

while i <= 4:
    print ("Hello everybody")
    i = i + 1 

#%%
beatles = ["John", "Paul", "George", "Ringo"] 

numbers = [1, 2, 3, 4]

mixed_values = [1, True, "abcd"]
# %%
print(len(beatles))
# %%
print(numbers[1])
# %%

beatles = ["John", "Paul", "George", "Ringo"]

print(beatles[2])

# %%

def print_list(list):
    index = 0

    while index <= len(list) - 1:
        print(list[index])
        index = index + 1

elements = ["maria", "santiago", "pepe"]
print_list(elements)
# %%

ramones = ["Johnnie", "Joey", "Markee", "Dee-dee"]

philippes = ["Philippe", "Pepe"]

print(ramones + philippes)
print(philippes * 4)
# %%

beatles = ["John", "Paul", "George", "Ringo"] 

beatles[3] = "Pepe"

print(beatles)

beatles[3] = "Ringo"

print(beatles)
# %%

coding_club = []

coding_club.append("Karmele")

coding_club.append("Phillipe")

print(coding_club)
# %%

beatles = ["John", "Paul", "George", "Ringo"]

def print_list_with_for(list):
    for element in list:
        print(element)


def print_list_with_while(list):
    index = 0

    while index <= len(list) - 1:
        print(list[index])
        index = index + 1

print_list_with_for(beatles)
print_list_with_while(beatles)
# %%
