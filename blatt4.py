# -*- coding: utf-8 -*-

# ------------
# Aufgabe 1
# ------------
def power(a,b):
    return a*power(a,b-1) if b != 0 else 1

for i,j in ((1,2),(2,2),(3,2),(4,3)):
    print(power(i,j))

def sum_digits(n):
    return n if n < 10 else n%10+sum_digits(n//10)

for i in (0,5,123,141683):
    print(sum_digits(i))

def remove_spaces(text):
    if text == "":
        return text
    elif text[0] == " ":
        return remove_spaces(text[1:])
    else:
        return text[0]+remove_spaces(text[1:])

for i in ("","Hello","This is a test"," This is a test "):
    print(remove_spaces(i))

# ------------
# Aufgabe 2
# ------------
list_1 = [1, 5, 3, 7, 2, 9]
half_list = len(list_1)//2
print(list_1[0], list_1[-1])
print(list_1[0:half_list])
print(list_1[half_list:])

list_2 = ["Amsterdam", "Berlin", "London", "Madrid", "Paris", "Stockholm", "Wien"]
list_21 = [var for var in list_2 if len(var)>6]
list_22 = [var for var in list_2 if var[-1]=="n"]
print(list_21)
print(list_22)

list_3 = ["Kreuz", "Pik", "Herz", "Karo"]
list_4 = ["Ass", "Koenig", "Dame", "Bube", "10", "9", "8", "7", "6", "5", "4", "3", "2"]
list_5 = [(i,j) for i in list_3 for j in list_4]
poker_hand = list_5[5:26:5]
print(poker_hand)
# ------------
# Aufgabe 3
# ------------
def min_max(list):
    return [min(list),max(list)]

print(min_max([3, 1, 5, 7, 2, 8]))
print(min_max(["London", "Berlin", "Paris", "Rom", "Wien"]))

def split_list(list, threshold):
    list_down = [var for var in list if var<threshold]
    list_up = [var for var in list if var not in list_down]
    return (list_down, list_up)

for i,j in (([3, 8, 5, 1, 9], 5),
            ([3, 8, 5, 1, 9], 1),
            ([3, 8, 5, 1, 9], 10),
            ([], 5)):
    print(split_list(i,j))

def combine_lists(list_1, list_2):
    if list_1 == []:
        return list_2
    elif list_2 == []:
        return list_1
    else:
        return [list_1[0],list_2[0],*combine_lists(list_1[1:],list_2[1:])]

print(combine_lists([1, 3], [2, 4]))
print(combine_lists([2, 4], [10, 20, 30, 40]))
print(combine_lists([10, 20, 30], [1, 3]))
print(combine_lists([], [1, 3]))
print(combine_lists([], []))
# ------------
# Aufgabe 4
# ------------
import random
def generate_landscape(n,p):
    def obstacle():
        return "#" if random.random()<0.5 else "@"
    return [[obstacle() if p > random.random() else "." for _ in range(n)] for _ in range(n)]

def print_landscape(landscape):
    for path in landscape:
        print(*path)

def mark_paths(landscape):
    n = len(landscape)
    for i in range(n):
        if "#" not in landscape[i] and "@" not in landscape[i]:
            landscape[i]="*"*len(landscape[i])

l = generate_landscape(10, 0.2)
print_landscape(l)
mark_paths(l)
print()
print_landscape(l)