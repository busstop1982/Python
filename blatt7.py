# -*- coding: utf-8 -*-

# ------------
# Aufgabe 1
# ------------

# Komplexität: Liste mit n Elementen wird bei jedem Durchgang halbiert -> O(log(n))
def binary_search(data: list, elem: int) -> int:
    low = 0
    index = -1
    high = len(data) - 1
    while low <= high:
        mid = (low + high) // 2
        if elem == data[mid]:
            index = mid
            high = mid - 1
        elif elem < data[mid]:
            high = mid - 1
        else:
            low = mid + 1
    return index


def test_search() -> None:
    m = [1, 5, 5, 5, 5, 5, 5, 7, 8, 10, 12, 13, 18, 18, 18, 18, 18, 18, 19]
    print(binary_search(m, 5))
    print(binary_search(m, 18))
    print(binary_search(m, 1))
    print(binary_search(m, 0))
    print(binary_search(m, 19))
    print(binary_search(m, 100))


test_search()


# ------------
# Aufgabe 2
# ------------

# Komplexität: durchläuft maximimal 2*n Einträge (diagonal durch, ohne den wert zu finden) -> in O(n)
def matrix_search(matrix: list, value: int) -> bool:
    """startet links unten, geht mit jeder iteration eine zelle nach rechts/rechts oben wenn der wert dort kleiner
    gleich dem gesuchten ist, sonst nach oben."""

    def hop(x: int, y: int):
        if matrix[x][y + 1] <= value:
            return x, y + 1
        elif matrix[x - 1][y + 1] <= value:  # kann ein paar durchläufe sparen
            return x - 1, y + 1
        else:
            return x - 1, y

    i = len(matrix) - 1
    j = 0
    while i > -1 and j < len(matrix) - 1:
        if matrix[i][j] is value:
            return True
        i, j = hop(i, j)
    return False


def test_matrix_search() -> None:
    m = [[1, 3, 3, 4, 5],
         [1, 3, 4, 4, 6],
         [2, 3, 4, 5, 6],
         [3, 5, 5, 6, 8],
         [4, 5, 8, 9, 9]]
    print([matrix_search(m, i) for i in range(11)])


test_matrix_search()


# ------------
# Aufgabe 3
# ------------

# Komplexität: liste wird einmal beim finden der beiden werte durchlaufen (im schlechtesten fall ganz) und einmal
# komplett beim sortieren -> O(n)
def sort_two_values(data: list) -> None:
    def switch(a, b):
        data[a], data[b] = data[b], data[a]

    # finden von max/min:
    val1 = val2 = data[0]
    i = 0
    while val1 is val2:
        if val2 is not data[i]:
            val2 = data[i]
        i += 1
    if val1 > val2:
        val1, val2 = val2, val1
    # setzt einen index i beim ersten grossen wert. beim nächsten kleinen wert: tauscht mit platz i und setzt i -> i+1
    nub = -1
    i = 0
    while i < len(data):
        if data[i] is val2 and nub is -1:
            nub = i
        if data[i] is val1 and nub is not -1:
            switch(nub, i)
            nub += 1
        i += 1


def test_sort_two() -> None:
    d = [1, 0, 0, 1, 0, 1, 1, 0, 0, 0, 1, 0, 1, 1, 0]
    sort_two_values(d)
    print(d)
    d = ["Bob", "Alice", "Alice", "Bob", "Alice"]
    sort_two_values(d)
    print(d)
    d = [3.5, 2.3, 2.3, 3.5]
    sort_two_values(d)
    print(d)


test_sort_two()

# ------------
# Aufgabe 4
# ------------

import operator
import random

d = [random.randint(0, 10) for i in range(10)]
print(d)
d.sort()
print(d)
r = [random.randint(0, 10) for j in range(10)]
print(r)
r.sort(reverse=True)
print(r)

cities = ["Vienna", "Amsterdam", "Rome", "Dublin", "Helsinki", "Bratislava"]

cs = sorted(cities)
print(cs)
cls = sorted(cities, key=lambda x: len(x)) # key=len <- funkt
print(cls)
clr = sorted(cities, key=lambda x: len(x), reverse=True)
print(clr)

cities_2 = {"Vienna": 1888776, "Amsterdam": 872680, "Rome": 2860009, "Dublin": 554554, "Helsinki": 650058,
            "Bratislava": 432864}
sorted_cities = dict(sorted(cities_2.items(), key=operator.itemgetter(0)))
""" list.items() gibt ein dict_items objekt mit (stadt, EW-zahl) tupeln zurück. sorted() sortiert nach dem key (in 
diesem  Fall dem 0ten element der tupel -> Stadtnamen) und gibt eine liste von tupeln zurück. dict() macht wieder ein
 dictionary daraus."""
print(sorted_cities)
sorted_cities_ew = dict(sorted(cities_2.items(), key=operator.itemgetter(1)))
print(sorted_cities_ew)


# ------------
# Aufgabe 5
# ------------

class Student:
    def __init__(self, name: str, first_test: int, second_test: int):
        self.name = name
        self.ft = first_test
        self.st = second_test

    def __lt__(self, other) -> bool:
        if self.ft < other.ft:
            return True
        elif self.ft > other.ft:
            return False
        else:
            return True if self.st < other.st else False

    def __str__(self) -> str:
        return self.name + ":" + str(self.ft) + "/" + str(self.st)


def test_students() -> None:
    import random
    names = ["Alice", "Bob", "Claire", "Donald", "Eric", "Jessica", "Leo", "Robyn", "William", "Zoe"]
    students = [Student(name, random.randint(90, 100), random.randint(50, 100)) for name in names]

    print("Student results:")
    print("\n".join(str(i) for i in students))
    students.sort()
    print("\nSorted results:")
    print("\n".join(str(i) for i in students))


test_students()
