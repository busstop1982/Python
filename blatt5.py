 # -*- coding: utf-8 -*-

# ------------
# Aufgabe 1	
# ------------

# Jede Stadt in einer eigenen Zeile ausgeben:
# Beijing
# Tokyo
# Moscow
# Mexico City
capitals = {"China": "Beijing", "Japan": "Tokyo", "Russia": "Moscow", "Mexico": "Mexico City"}
for i in capitals:
    print(capitals[i])

# Alle Berge als Liste in einer Zeile ausgeben, in der Zeile darunter die entsprechenden Höhen als Liste ausgeben:
# ['Everest', 'K2', 'Kangchenjunga', 'Lhotse', 'Makalu']
# [8848, 8614, 8586, 8516, 8485]
mountains = {"Everest": 8848, "K2": 8614, "Kangchenjunga": 8586, "Lhotse": 8516, "Makalu": 8485}
print([m for m in mountains])
print([mountains[m] for m in mountains])

# Eine Liste von Namen erstellen, bei denen mehr als 2 Ergebnisse in der Punkteliste (Wert im Dictionary) stehen und diese ausgeben:
# ['Alice', 'Bob', 'Erik']
# Ein neues Dictionary erstellen, bei dem zu jedem Namen nur mehr die maximale Punkteanzahl gespeichert wird und dieses ausgeben:
# {'Alice': 98, 'Bob': 86, 'Claire': 86, 'Donald': 55, 'Erik': 76}
students = {"Alice": [98, 85, 92], "Bob": [86, 79, 78], "Claire": [75, 86], "Donald": [55], "Erik": [65, 54, 76]}
print([s for s in students if len(students[s]) > 2])
print({i: max(students[i]) for i in students})

# Ein Dictionary erstellen, bei dem nur jene Städte mit ihrem Temperaturwert vorhanden sind, bei denen die Temperatur über 18 Grad liegt und dieses ausgeben:
# {'Graz': 19, 'Klagenfurt': 19}
# Eine Python-Menge von Windgeschwindigkeiten erstellen, die bei Städten mit einer Temperatur > 15 auftreten und diese ausgeben:
# {25, 10, 20, 15}

weather = {"Vienna": {"wind": 10, "temperature": 18},
           "St.Pölten": {"wind": 10, "temperature": 18},
           "Linz": {"wind": 20, "temperature": 16},
           "Salzburg": {"wind": 15, "temperature": 16},
           "Innsbruck": {"wind": 5, "temperature": 14},
           "Bregenz": {"wind": 12, "temperature": 15},
           "Eisenstadt": {"wind": 25, "temperature": 17},
           "Graz": {"wind": 15, "temperature": 19},
           "Klagenfurt": {"wind": 15, "temperature": 19},
           }
print({i: weather[i]["temperature"] for i in weather if weather[i]["temperature"] > 18})
print({weather[i]["wind"] for i in weather if weather[i]["temperature"] > 15})


# ------------
# Aufgabe 2
# ------------

def find_root(x, power, epsilon):
    for i in [x, power, epsilon]:
        if type(i) not in [int, float]:
            raise TypeError("Arguments should be of type int or float")
    if x < 0 and power % 2 == 0:
        raise ValueError("Negative number has no even-powered roots")
    if power < 1:
        raise ValueError("Power should be >= 1")
    if epsilon <= 0:
        raise ValueError("Epsilon should be > 0")
    low = min(-1.0, x)
    high = max(1.0, x)
    ans = (high + low) / 2.0
    while abs(ans ** power - x) >= epsilon:
        if ans ** power < x:
            low = ans
        else:
            high = ans
        ans = (high + low) / 2.0
    return ans


def print_vals():
    vals = [(0.5, 2, 0.001), (-8, 3, 0.0001)]
    for i in vals:
        print(find_root(*i))


print_vals()


def print_evil_vals():
    evil_vals = [(-8, 2, 0.0001), (0.5, 0, 0.001), (0.5, 2, 0), (-0.5, "a", 0.001), ("a", 2, 0.001), (2, 2, "a"),
                 (1, 2),
                 (1, 2, 0.001, 0.1)]
    for i in evil_vals:
        try:
            print(find_root(*i))
        except ValueError as msg:
            print(msg)
        except TypeError as msg:
            print(msg)


# Hier find_root mit allen Werten aus evil_vals testen - das Programm sollte nur Ausgaben erzeugen und nicht abstürzen
print_evil_vals()
"""""
Der Aufruf mit *args übergibt nicht ein Tupel von Werten, sondern die Werte selbst. Die nicht von der 
Erweiterung erzeugten Ausnahmen stammen daher, dass die Anzahl der übergebenen Werte nicht mit der Anzahl 
übereinstimmt, die die Funktion erwartet. 
"""


# ------------
# Aufgabe 3
# ------------
def mark(board, player, i, j):
    if not (0 <= i <= 2 and 0 <= j <= 2):
        raise ValueError('Invalid board position')
    if board[i][j] != ' ':
        raise ValueError('Board position occupied')
    board[i][j] = player


def is_win(board, mark):
    def is_mark(m,n):
        return board[m][n] == mark

    def check_lin(i,trans):
        return not False in [is_mark(j,i) if trans else is_mark(i,j) for j in range(3)]

    def str_win():
        return True in [check_lin(i,False) or check_lin(i,True) for i in range(3)]

    def dia_win():
        return is_mark(0,0) and is_mark(2,2) or is_mark(0,2) and is_mark(2,0) if is_mark(1,1) else False

    return str_win() or dia_win()


def print_board(board):
    rows = ['|'.join(board[r]) for r in range(3)]
    print('\n-----\n'.join(rows))


def run_game():
    board = [[' '] * 3 for j in range(3)]
    pieces = ["X", "O"]
    player = pieces[0]
    win = is_win(board, player)
    moves = 0
    while not win and moves < 9:
        try:
            print("Player", player, "choose your field: ")
            x = int(input("row number: "))
            y = int(input("column number: "))
            mark(board, player, x, y)
            print_board(board)
            win = is_win(board, player)
            if player == pieces[0]:
                player = pieces[1]
            else:
                player = pieces[0]
            moves += 1
        except ValueError as msg:
            print(msg)

    if is_win(board, pieces[0]):
        print(pieces[0], 'wins')
    elif is_win(board, pieces[1]):
        print(pieces[1], 'wins')
    else:
        print("Tie")

run_game()

# ------------
# Aufgabe 4
# ------------
def create_telbook():
    try:
        with open("tel.txt", "r") as file:
            book = {}
            for line in file:
                entry = line.split()
                book[entry[0]] = entry[1]
            return book
    except FileNotFoundError:
        return {}


def search(numbers):
    name = input("Name: ")
    try:
        print(name+"s number is: "+numbers[name])
    except KeyError:
        print("No such entry.")


def new_number(numbers):
    new_name = input("Name: ")
    new_num = input("Number: ")
    numbers[new_name] = new_num
    print("New number has been added!")


def print_numbers(numbers):
    print("All your entries:")
    print("Name   Number")
    print("----------")
    for name in numbers:
        print(name+":", numbers[name])


def print_goodbye(numbers):
    file = open("tel.txt", "w")
    for entry in numbers:
        file.write(entry + " " + numbers[entry] + "\n")
    file.close()
    print("Goodbye and thanks for all the fish!")


def menu(numbers):
    print("Welcome to this little phone book!")
    options = {"s": "(S)earch for a number", "n": "(N)ew number", "a": "(A)ll numbers", "e": "(E)nd"}
    functions = {"s": search, "n": new_number, "a": print_numbers, "e": print_goodbye}
    choice = ""
    while choice.lower() != "e":
        print("----------")
        try:
            for opt in options:
                print(options[opt])
            choice = input("Your choice: ")
            functions[choice.lower()](numbers)
        except KeyError:
            print("Please choose again")


# main program

book = create_telbook()
menu(book)
