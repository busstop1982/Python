# -*- coding: utf-8 -*-

# ------------
# Aufgabe 1	
# ------------

# Aufgabe: Ausgabe aller geraden Zahlen im Intervall [0, 20] in einer Zeile
# Implementierung:
#	* for-Schleife für das Iterieren über das Intervall
# 	* In der Verzweigung wird mit Modulo-Berechnung festgestellt, ob der aktuelle Wert von i eine gerade Zahl ist
# 	* Bei print wird das Schlüsselwortargument end auf " " gesetzt und daher wird nicht in die nächste Zeile gesprungen

for i in range(0, 21):
    if i % 2 == 0:
        print(i, end=" ")
print()

# Aufgabe: Ausgabe aller Zahlen im Intervall [0, 100] die durch 4 aber nicht durch 10 teilbar sind
# Implementierung:
#   * while-Schleife für das Intervall
#   * Verzweigung mit 2 if-Bedingungen - Feststellen ob a durch 4 und nicht durch 10 teilbar ist
#   * Ausgabe mit underscore statt newline

a = 0
while (a < 100):
    if (a % 4 == 0) and (a % 10 != 0):
        print(a, end="_")
    a += 1
print()

# Aufgabe: Eingabetext wird auf Zeichen in [a-z] reduziert und wieder ausgegeben
# Implementierung:
#   * Einlesen eines Strings -> Groß- zu Kleinbuchstaben
#   * In der Schleife wird für jedes Zeichen überprüft ob es ein Buchstabe aus [a-z] ist; falls ja hinzufügen zu new_text.
#   * Ausgabe von new_text

text = input("Please enter some text: ")
text = text.lower()
new_text = ""
for c in text:
    if c in "abcdefghijklmnopqrstuvwxyz":
        new_text += c
print(new_text)

# Aufgabe: Primfaktorenzerlegung
# Implementierung:
#   * Einlesen einer Zahl N
#   * Setze Faktor D = 2
#   * Erste while-Schleife: Abbruchbedingung: D^2 > N
#      * Zweite while-Schleife: falls N D mit Null Rest teilt: teile N durch D, gib D aus
#   * erhöhe D um 1
#   * falls ein Rest groesser Eins bleibt, diesen ausgeben

n = int(input("Please enter an integer > 0: "))

factor = 2
while factor * factor <= n:
    while n % factor == 0:
        n //= factor
        print(factor, end=" ")
    factor += 1
if n > 1:
    print(n)

# ------------
# Aufgabe 2
# ------------

# Aufgabe 2.1
output=0
for i in range (0,101):
    output+=i
print(output)

# Aufgabe 2.2
n=1
while 2**n <= 1024:
    print(2**n,end=" ")
    n += 1

# Aufgabe 2.3
stuff=input("i can haz string now? ")
the_as=0
for l in stuff:
    if l == "a":
        the_as += 1
print(the_as)

# Aufgabe 2.4
stuff = input("give us the string!")
i = 0
not_found = True

while not_found and i < len(stuff):
    if stuff[i] == "u":
        not_found = False
    i += 1

if not_found:
    i = 0

print(i-1)

# ------------
# Aufgabe 3
# ------------
message = "* Welcome to the GPA calculator! *"
print("*"*len(message)+"\n"+message+"\n"+"*"*len(message))

options = ["add two numbers","multiply two numbers","calculate square root","quit"]
chosen = 0

while chosen != 4:
    print("Please make your choice:")
    for i in range(4):
        print(i+1,"...",options[i])
    chosen = int(input("Your input: "))

    if chosen == 1:
        n1 = float(input("First number: "))
        n2 = float(input("Second number: "))
        print("Result:",n1+n2)
    elif chosen == 2:
        n1 = float(input("First number: "))
        n2 = float(input("Second number: "))
        print("Result:",n1*n2)
    elif chosen == 3:
        number = float(input("Your number: "))
        epsilon = 0.001
        guess = number / 2
        guesses = 0
        while abs(guess**2 - number) > epsilon and guesses < 100:
            guess = guess - (guess**2 - number)/(2*guess)
            guesses += 1
        print("Square root of",number,"is about",guess)
    elif chosen == 4:
        print("Good bye! See you soon!")
    else:
        print("Please choose a valid option!")

