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