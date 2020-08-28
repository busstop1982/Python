# -*- coding: utf-8 -*-

# ------------
# Aufgabe 1
# ------------

# 2 1 0 3 5 4
# 2 3 5 4 0 1 -> kann nicht 0 vor 1 ausgeben wenn 1 schon auf dem stack liegt
# 3 2 1 4 0 5
# 0 3 1 2 5 4 -> eins liegt unter zwei (weil drei schon am stack war) -> kann eins nicht vor zwei ausgeben

# ------------
# Aufgabe 2
# ------------

# 5 4 3 2 1 0 
# 5 4 0 1 2 3 
# 2 1 0 3 4 5 
# 0 1 2 3 5 4 
# das geht alles nicht, weil die reihenfolge (0,1,2,3,4,5) nicht verändert werden kann und 0 als erstes ausgegeben wird.
# ------------
# Aufgabe 3
# ------------


from stack import Stack
from collections import deque
from my_queue import Queue
import random


# Komplexität: worst case: für jede Zahl wird newstack auf original zurückgeschoben -> n(n+1)/2 operationen -> in O(n^2)
def sort_stack(original) -> Stack:
    new_stack = Stack()
    while not original.is_empty():
        curr = original.pop()
        while not new_stack.is_empty() and curr <= new_stack.top():
            original.push(new_stack.pop())
        new_stack.push(curr)
    return new_stack


def test_sort():
    data = Stack()
    values = [4, 1, 5, 6, 8, 7, 3, 2]
    for i in values:
        data.push(i)
    result = sort_stack(data)
    values.clear()
    while not result.is_empty():
        values.append(result.pop())
    print(values)


test_sort()


# ------------
# Aufgabe 4
# ------------

# Komplexität: 2k push&pop + n-k requeue -> amortisiert in O(n)
def reverse_first_k_entries(k, queue):
    if len(queue) < k < 2:
        return
    buffer = Stack()
    for i in range(k):
        buffer.push(queue.dequeue())
    while not buffer.is_empty():
        queue.enqueue(buffer.pop())
    for i in range(len(queue) - k):
        queue.enqueue(queue.dequeue())


def test_reverse():
    data = Queue()
    values = [10, 20, 30, 40, 50, 60, 70, 80, 90]
    for i in values:
        data.enqueue(i)
    reverse_first_k_entries(4, data)
    values.clear()
    while not data.is_empty():
        values.append(data.dequeue())
    print(values)


test_reverse()


# ------------
# Aufgabe 5
# ------------

# Fragen:
# Neue Knoten werden am Anfang der Liste eingefügt -> neues Element wird head
# nach flip zeigt ein knoten n auf n-1 statt auf n+1, wobei auch head und None platz tauschen.
# head -> 1 ... n -> None => None <- 1 ... n <- head
# ein schleifendurchlauf:
# vom aktuellen knoten n wird der verknüpfte (n._next) als iterator weitergegeben.
# der knoten selbst wird zwischengespeichert (als first für die nächste iteration).
# die verknüpfung wird vom nächsten auf den vorhergehende knoten geändert.


class SpecialList:
    class _Node:
        def __init__(self, element, next_elem):
            self._element = element
            self._next = next_elem

    def __init__(self):
        self._head = None

    def add(self, e):
        self._head = self._Node(e, self._head)

    def __str__(self):
        result = []
        walk = self._head
        while walk is not None:
            result.append(walk._element)
            walk = walk._next
        return str(result)

    def flip(self):
        first = None
        walk = self._head
        while walk is not None:
            second = walk._next
            walk._next = first
            first = walk
            walk = second
        self._head = first


def test_special_list():
    data = SpecialList()
    print(data)
    data.add(1)
    print(data)
    data.add(2)
    data.add(3)
    print(data)
    data.flip()
    print(data)


test_special_list()


# ------------
# Aufgabe 6
# ------------

# Fragen:
# Knoten sind ihrem Nachfolger verknüpft. Beim Initialisieren einer Liste werden head und # tail (Anfang und Ende der Liste) erstellt.
# neue elemente werden als vorletztes eingefügt (also for tail).

class TangledList:
    class _Node:
        def __init__(self, element, next_elem):
            self._element = element
            self._next = next_elem

    def __init__(self):
        self._head = self._Node(0, None)
        self._tail = self._Node(0, None)
        self._head._next = self._tail._next = self._tail

    def add(self, element):
        newest = self._Node(element, None)
        walk = self._head
        while not walk._next == walk._next._next:  # True bis self._tail (tail.next = tail) -> walk = vorletztes
            walk = walk._next
        newest._next = walk._next  # newest._next = tail
        walk._next = newest  # vorletztes._next = newest

    def __str__(self):
        result = []
        walk = self._head
        while not walk._next == walk._next._next:
            walk = walk._next
            result.append(walk._element)
        return str(result)


def test_tangled_list():
    data = TangledList()
    print(data)
    data.add(1)
    print(data)
    data.add(2)
    data.add(3)
    print(data)


test_tangled_list()


# ------------
# Aufgabe 7
# ------------


class Song:
    def __init__(self, title: str, artists: str):
        self.title = title
        self.artists = artists
        self.play_count = 0

    def play(self) -> None:
        if self.play_count < 5:
            self.play_count += 1
        print("Playing", u"\U0001F3B5", self.title, u"\U0001F3B5", "by", self.artists)

    def __str__(self) -> str:
        return "\"" + self.title + "\"" + " by " + self.artists + " (played " + str(self.play_count) +\
               " {times})".format(times="time" if self.play_count is 1 else "times")


class Player:
    def __init__(self, songs: list) -> None:
        self.songs = deque(songs)

    def __str__(self) -> str:
        out = "Playlist:\n"+"\n".join(str(i) for i in self.songs)
        return out

    def play_first_song(self) -> None:
        current = self.songs.popleft()
        print("First song:")
        current.play()
        self.songs.append(current)

    def play_last_song(self) -> None:
        current = self.songs.pop()
        print("Last Song:")
        current.play()
        self.songs.appendleft(current)

    def wurlitzer(self, loops: int) -> None:
        for i in range(loops):
            self.songs.rotate(random.randint(1, len(self.songs)))
            self.play_first_song()


def test_song():
    favs = [Song("Pöpi", "Eleäkeläiset"),
            Song("Hooked on a Feeling", "David Hasselhoff"),
            Song("It's Raining Men", "The Weather Girls"),
            Song("Never Gonna Give You Up", "Rick Astley"),
            Song("Holding out for a Hero", "Bonnie Tyler"),
            Song("Bohemian Rhapsody", "Queen"),
            Song("You Spin Me Round", "Dead or Alive"),
            Song("Life is a Highway", "Tom Cochrane"),
            Song("I Was Made for Lovin' You", "KISS")]
    playlist = Player(favs)
    print(playlist, "\n")
    playlist.wurlitzer(6)
    for i in range(3):
        playlist.play_first_song()
        playlist.play_last_song()
    print("\n", playlist)


test_song()
