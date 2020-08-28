# -*- coding: utf-8 -*-

# ------------
# Aufgabe 1	
# ------------
2 ** 3  # potenzieren, 8, integer(int)
5.0 * .5  # multiplikation, 12.5, float
"One" + "Two"  # concatenation von strings, 'OneTwo', str(string)
2 * (5 / 2)  # division -> multiplikation, 5.0, float
22 // 5 % 2  # division ohne nachkomma -> modulo, 0, int
int("10") + float(5 // 2)  # division -> addition, 12.0, float
"Hello World"[6:] + "Hello World"[:5]  # slice strings -> concatenate, 'WorldHello', string
"step on no pets"[::-1]  # string rückwärts ausgeben, 'step on no pets', string
2 < 3 and 4 < 5  # zwei booleans mit und verknüpft, True, bool(boolean)
bool("") or False  # zwei booleans mit oder verknüpft, False, boolean
# ------------
# Aufgabe 2
# ------------

# Teilaufgabe 2.1
current_year = int(input('Current year: '))
year = int(input('Year to check: '))
preamble = ""

if (year % 400 == 0) or ((year % 4 == 0) and (year % 100 != 0)):
    analysis = "a leapyear"
else:
    analysis = "not a leapyear"

if year < current_year:
    preamble = "Long time ago -"
elif year > current_year:
    preamble = "The future is always beginning now -"
else:
    analysis = analysis.capitalize()

print("Current year:", current_year)
print("Year to analyze:", year)
print(str(year)+":", preamble, analysis)

# Teilaufgabe 2.2
a = int(input("First number: "))
b = int(input("Second number: "))
c = int(input("Third number: "))
if b < a:  # wenn b kleiner a, tausche b mit a
    t = b
    b = a
    a = t
if c < b:  # wenn c kleiner b, tausche b mit c
    t = c
    c = b
    b = t
if b < a:  # siehe erstes if
    t = b
    b = a
    a = t
print(a, b, c)

# Alternative Form für Teilaufgabe 2.2
a = int(input("First number: "))
b = int(input("Second number: "))
c = int(input("Third number: "))
if b < a:
    a, b = b, a
if c < b:
    b, c = c, b
if b < a:
    a, b = b, a
print(a, b, c)
# ------------
# Aufgabe 3
# ------------

# Teilaufgabe 3.1. Version nur mit if (ohne elif und else)
weight = float(input("Gewicht: "))
output = "Falsche Eingabe! Gewicht muss > 0 sein!"
if weight > 0:
    output = "Gewicht --> Extra leicht"
    if weight >= 5:
        output = "Gewicht --> Leicht"
        if weight >= 10:
            output = "Gewicht --> Mittelschwer"
            if weight >= 25:
                output = "Gewicht --> Schwer"
                if weight >= 50:
                    output = "Gewicht --> Extra Schwer"

print(output)

# Teilaufgabe 3.2. Version mit elif
weight = float(input("Gewicht: "))

if weight <= 0:
    output = "Falsche Eingabe! Gewicht muss > 0 sein!"
elif weight < 5:
    output = "Gewicht --> Extra leicht"
elif weight < 10:
    output = " Gewicht -->Leicht"
elif weight < 25:
    output = "Gewicht --> Mittelwert"
elif weight < 50:
    output = "Gewicht --> Schwer"
else:
    output = "Gewicht --> Extra Schwer"

print(output)
