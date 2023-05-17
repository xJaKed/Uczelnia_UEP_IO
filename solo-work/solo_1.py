# zadanie 1.1

hello = "Hello"
student = "Kuba"

print("{} {}".format(hello, student))

# zadanie 1.2

student = input("Wpisz swoje imie")

print("Hello {}".format(student))

# zadanie 1.3

studenci = ["Ania", "Kuba", "Piotr", "Jan"]

liczba_studentow = len(studenci)
print("Liczba studentow wynosi: {}".format(liczba_studentow))

# zadanie 1.4

studenci = ["Ania", "Kasia", "Piotr", "Tomek"]

for i in studenci:
    print("Hello {}".format(i))

# zadanie 1.5

liczba = 3
potega = 4

wynik = liczba**potega

print("Wynik wynosi: {}".format(wynik))

# zadanie 1.6

ciag_znakow = "edbw(hdakqas(skqskahb))adwndwb(wgwidn()dsqwhjdw)"
liczba_nawiasow_otwierajacych = ciag_znakow.count("(")

print("Liczba nawiasow otwierajacych wynosi: " + str(liczba_nawiasow_otwierajacych))

# zadanie 1.7

studenci = ["Anna Szczesny", "Tomasz Nijaki", "Barbara Kowalska", "Jan Niezbedny"]
studenci.sort()

print("Alfabetyczna lista studentow wynosi: ")
for student in studenci:
    print(student)

# zadanie 1.8

studenci = ["Anna Szczesny", "Tomasz Nijaki", "Barbara Kowalska", "Jan Niezbedny"]
studenci_1=sorted(studenci, key = lambda name:name.split(' ')[1])

print("Alfabetyczna lista studentow wynosi: ")
for student in studenci_1:
    print(student)

# zadanie 1.9
studenci = ["Anna Szczesny", "Tomasz Nijaki", "Barbara Kowalska", "Jan Niezbedny"]

liczba_n = 0
for student in studenci:
    if student.split()[1][0].upper() == "N":
        liczba_n += 1
print("Liczba studentow na N wynosi: {}".format(liczba_n))

# zadanie 1.10

wykres_1 = [[2, 4], [4, 4], [6, 4]]
wykres_2 = [[2, 3], [4, 4], [6, 5]]
wykres_3 = [[2, 3], [4, 3], [5, 4]]

def sprawdzenie(wykres):
        x1=wykres[0][0]
        x2=wykres[1][0]
        x3=wykres[2][0]
        y1=wykres[0][1]
        y2=wykres[1][1]
        y3=wykres[2][1]
        a = (y1-y2)/(x1-x2)
        if (y3-y1)/(x3-x1)==a:
            return True
        else:
            return False

wykres_1_funkcja_liniowa = sprawdzenie(wykres_1)
wykres_2_funkcja_liniowa = sprawdzenie(wykres_2)
wykres_3_funkcja_liniowa = sprawdzenie(wykres_3)

if wykres_1_funkcja_liniowa==True:
    print("Dla punktow w wykres_1 mozna wyznaczyc funkcje liniowa.")
else:
    print("Dla punktow w wykres_1 nie mozna wyznaczyc funkcji liniowej.")

if wykres_2_funkcja_liniowa==True:
    print("Dla punktow w wykres_2 mozna wyznaczyc funkcje liniowa.")
else:
    print("Dla punktow w wykres_2 nie mozna wyznaczyc funkcji liniowej.")

if wykres_3_funkcja_liniowa==True:
    print("Dla punktow w wykres_3 mozna wyznaczyc funkcje liniowa.")
else:
    print("Dla punktow w wykres_3 nie mozna wyznaczyc funkcji liniowej.")