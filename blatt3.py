# -*- coding: utf-8 -*-

# ------------
# Aufgabe 1	
# ------------
def print_pattern(n):
    stars = "*"*n
    new_n = (n+1)//2
    return stars[new_n:]+" :-) "+stars[:new_n]

def mysum(low,high,sum=0):
    if low+1 == high:
        return sum+low+high
    else:
        return mysum(low+1,high,sum+low)

def powers_of_two(low, high, i=1):
    out = ""
    for j in range(low,high+1,i):
        out += str(2**j)+" "
    return out

# ------------
# Aufgabe 2
# ------------
def check_length(s,t):
    if len(s)<len(t):
        return t
    elif len(s)>len(t):
        return s
    else:
        return s+t

#einmal hübsch
def cat_strings(*texts):
    def addem(first, second):
        if first == "":
            return second
        else:
            return first + "-" + second

    output = ""
    for text in texts:
        output = addem(output, text)
    return output

#einmal kurz
def cat_strings_1(*args):
    out = ""
    for arg in args:
        out += arg+"-"
    return out[:len(out)-1]

# ------------
# Aufgabe 3
# ------------
def is_prime(n):
    still_prime = True
    i = 2
    while still_prime and i<n:
         if n % i == 0:
            still_prime = False
         i += 1
    return still_prime

def user_input():
    print("Welcome to the primerator!")
    return int(input("Please choose upper bound: "))

def generate(upper_bound):
    out = ""
    for i in range (2,upper_bound+1):
        if is_prime(i):
           out += str(i)+"\n"
    return out

def main():
    print(generate(user_input()))
# ------------
# Aufgabe 4
# ------------

# Aufgabe: Gibt die einzelnen Ziffern einer Zahl nach aufsteigender 10er Potenz sortiert aus
# Basisfall: n < 10 -> print n
# Rekursionsschritt: print n modulo 10 (die 10^0 Stelle) -> n//10 an das Programm zurück

def magic_print(n):
    if n < 10:
        print(n)
    else:
        print(n % 10)
        magic_print(n // 10)
		
# Aufgabe: Testet ob eine Zahl gerade ist
# Basisfall: 2 Fälle: n = 0 -> wahr; n = 1 -> falsch
# Rekursionsschritt: 2 von der Zahl abziehen -> überprüfen

def magic_test(n):
    if n == 0:
        return True
    elif n == 1:
        return False
    else:
        return magic_test(n - 2)	

# Aufgabe: Gibt die Eingabe verkehrt herum aus
# Basisfall: leerer String rein, leerer String raus (Abbruchbedingung)
# Rekursionsschritt: magic_string vom text ab index 1 + 0ter index vom text

def magic_string(text):
    if text == "":
        return ""
    else:
        return magic_string(text[1:]) + text[0]

# Aufgabe: Vergleiche ob zwei strings ident sind
# Basisfall: Strings nicht gleich lang -> falsch
#            ODER: leerer String -> wahr
#            ODER: die ersten Zeichen sind ungleich -> falsch
# Rekursionsschritt: magic_strings von 2 - um je ein zeichen verkürzte - strings

def magic_strings(text_1, text_2):
    if len(text_1) != len(text_2):
        return False
    elif text_1 == "":
        return True
    elif text_1[0] != text_2[0]:
        return False
    else:
        return magic_strings(text_1[1:], text_2[1:])		
