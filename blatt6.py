# -*- coding: utf-8 -*-

# ------------
# Aufgabe 1
# ------------

class Fraction:
    # Beschreibung:
    # Initiiert ein Objekt der Klasse Fraction mit zwei übergebenen Zahlen, ruft gcd auf, kürzt den Bruch durch
    # den größten gemeinsamen Teiler und speichert die Zahlen als numerator und denominator ab.
    def __init__(self, numerator: int, denominator: int) -> None:
        if denominator is 0:
            raise ValueError("Denominator can't be zero.")
        g = gcd(numerator, denominator)
        self.numerator = numerator // g
        self.denominator = denominator // g

    def __str__(self) -> str:
        return str(self.numerator) + "/" + str(self.denominator)

    def __add__(self, other):
        new_den = lcm(self.denominator, other.denominator)
        new_num = self.numerator * new_den // self.denominator + other.numerator * new_den // other.denominator
        return Fraction(new_num, new_den)

    def inverse(self):
        return Fraction(self.denominator, self.numerator)


def gcd(a: int, b: int) -> int:
    while b != 0:
        a, b = b, a % b
    return a


def lcm(a: int, b: int) -> int:
    """kleinstes gemeinsames vielfaches"""
    return abs(a * b) // gcd(a, b)


def test() -> None:
    f1 = Fraction(6, 24)
    print(f1)
    f2 = Fraction(3, 7)
    print(f2)
    f3 = f1 + f2
    print(f3)
    f4 = f2.inverse()
    print(f4)
    print((f1 + f1).inverse().inverse())
    # Warum funktioniert dieser Aufruf und wie läuft die Ausführung ab?
    # 6/24 wird als 1/4 initiiert, zu sich selbst addiert (-> 2/4 __init__ auf 1/2), zwei mal invertiert und
    # geprintet. Bezüglich warum: weil wir für die Klasse Fraction den + Operator überschrieben und die Methode
    # .inverse() definiert haben.


test()


# ------------
# Aufgabe 2
# ------------

# Funktion 2n + 3
# Obere Schranke: O(n)
# Erklärung: Korrekt. 2n + 3 <= 5n für c = 5 und n0 = 1 und daher in O(n)


# Funktion a) log(n) + 5
# Obere Schranke: O(n)
# Erklärung: ansich korrekt, allerdings ist O(log(n)) eine kleinere obere Schranke [log(n)+5 <= 6log(n) für n0 = 2].


# Funktion b) n^2*n + 3
# Obere Schranke: O(n^2)
# Erklärung: Falsch. n^3+3 </= c*n^2; mit c = 4, n0 = 1 in O(n^3)


# Funktion c) n^3 + n×n + 4
# Obere Schranke: O(n^4)
# Erklärung: wie bei a): Korrekt, aber da n^3 + n^2 + 4 <= 6n^3 für n0=1 ist O(n^3) eine größere Einschränkung


# Funktion d) n^2 + 2^10*n
# Obere Schranke: O(n^2)
# Erklärung: Korrekt, n^2 + 2^10*n  <= c*n^2 für n0 = 1, c = 1025, daher in O(n^2)


# Funktion e) 3^n
# Obere Schranke: O(2^n)
# Erklärung: Falsch. 3^n > 2^n für alle n > 0 (-> O(3^n))

# ------------
# Aufgabe 3
# ------------


# Beschreibung: Berechnet n*n
# Komplexität: Zwei verschachtelte Schleifen, Obergrenzen von n abhängig -> O(n^2)

def func_example(n: int) -> int:
    count = 0
    for i in range(n):
        for j in range(n):
            count += 1
    return count


# Beschreibung: Berechnet die Summe von 0 bis n
# Komplexität: Schleife in Schleife; kleiner gauß -> n(n+1)/2 -> O(n^2)

def func_1(n: int) -> int:
    count = 0
    for i in range(n):
        for j in range(i, n):
            count += 1
    return count


# Beschreibung: Berechnet n*((n+1)//2) bzw: n^2/2 für gerade n, n*(n+1)/2 für ungerade n
# Komplexität: 2 verschachtelte Schleifen, ca. n*n/2 -> O(n^2)

def func_2(n: int) -> int:
    count = 0
    for i in range(n):
        for j in range(0, n, 2):
            count += 1
    return count


# Beschreibung: Berechnet 10*n
# Komplexität: zwei verschachtelte Schleifen, aber äussere immer nur bis 10 -> O(n)

def func_3(n: int) -> int:
    count = 0
    for i in range(10):
        for j in range(n):
            count += 1
    return count


# Beschreibung: Berechnet um wieviel n größer als 100 ist
# Komplexität: eine Schleife -> O(n)
def func_4(n: int) -> int:
    count = 0
    for i in range(100, n):
        count += 1
    return count


# Beschreibung: Berechnet n*ceil(log_2(n+1)) [log basis 2]
# Komplexität: äußere Schleife n, innere Schleife log2(n) Durchläufe -> O(n log(n))
def func_5(n: int) -> int:
    count = 0
    for i in range(n):
        b = n
        while b > 0:
            count += 1
            b //= 2
    return count


# ------------
# Aufgabe 4
# ------------

# Beschreibung: Macht eine neue Liste: [a,b,c,d]->[a,a+b,a+b+c,a+b+c+d]. äussere schleife
# iteriert durch die gesamte liste und setzt den startpunkt für die innere schleife.
# Innere schleife geht vom startpunkt (i) bis zum ende der liste und zieht von der aktuellen position das (i-1)te
# element ab (ausser beim ersten durchgang); dh man bekommt zb beim zweiten durchlauf b,b+c,b+c+d. so iteriert man
# durch alle möglichen summen von zahlen und vergleicht mit einem wert "maximum" der am anfang gleich null gesetzt wird.
# Komplexität: drei Schleifen, zwei davon verschachtelt, n-1 + n*n <= 2n^2 (n0=1) -> O(n^2)
# Speicheranforderung: vergleichbar mit max_sum_2, aber erstellt eine neue Liste mit n Einträgen.
# Aufruf mit einelementiger Liste: erste Schleife wird nicht durchlaufen (range(1,1)) -> part_sum=data; einziger Wert
# wird das Maximum
# Aufruf mit leerer Liste: keine Schleife wird durchlaufen, Maximum wird 0 gesetzt und ausgegeben

def max_sum_alt(data: list) -> int:
    part_sum = data[:]
    for pos in range(1, len(part_sum)):
        part_sum[pos] = part_sum[pos - 1] + part_sum[pos]
    maximum = 0
    for left in range(len(part_sum)):
        for right in range(left, len(part_sum)):
            temp_sum = part_sum[right]
            if left > 0:
                temp_sum -= part_sum[left - 1]
            if temp_sum > maximum:
                maximum = temp_sum
    return maximum


# ------------
# Aufgabe 5
# ------------

# my_unique
# Komplexität: sort in O(n log(n)) + eine schleife in O(n) -> insgesamt in O(n log(n))
def my_unique(data):
    data.sort()
    for i in range(1, len(data)):
        if data[i - 1] is data[i]:
            return False
    return True


# my_disjoint
# Komplexität: zwei verschachtelte Schleifen: n*2n <= 3n^2 for n0=1 -> O(n^2)
def my_disjoint(l1, l2, l3):
    for i in l1:
        if i in l2 and i in l3:
            return False
    return True
