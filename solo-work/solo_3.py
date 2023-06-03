# pip install numpy
import numpy as np
import datetime

class Student:
    def __init__(self, imie, nazwisko, nr_indeksu):
        self.imie = imie
        self.nazwisko = nazwisko
        self.nr_indeksu = nr_indeksu
        self.indeks = []
        self.srednia_ocen
    
    def __str__(self):
          return self.imie+" "+self.nazwisko+" "+str(self.nr_indeksu)
    
    def dodaj_ocene(self, ocena):
        self.indeks.append(ocena)
    
    def srednia_ocen(self):
        if len(self.indeks)==0:
            return 0
        else:
            return sum(self.indeks)/len(self.indeks)
        
    pass

student_kuba = Student("Jakub", "Kędzierski", 120057)
student_kuba.dodaj_ocene(5.0)
student_kuba.dodaj_ocene(4.0)
student_kuba.dodaj_ocene(3.0)
student_kuba.dodaj_ocene(2.0)
print(student_kuba)
print(student_kuba.indeks)
print(student_kuba.srednia_ocen())

#Zadanie Domowe

class Samochod:
    def __init__(self, marka, model, silnik, kolor, przebieg, cena, rocznik, rodzaj_paliwa):
        self.marka=marka
        self.model=model
        self.silnik=silnik
        self.kolor=kolor
        self.przebieg=przebieg
        self.cena=cena
        self.rocznik=rocznik
        self.rodzaj_paliwa=rodzaj_paliwa
        self.wlasciciele=[]

    def __str__(self):
        return self.marka+" "+self.model+" "+str(self.silnik)+" litrów "+self.kolor+" "+str(self.przebieg)+"km "+str(self.cena)+"zł "+ str(self.rocznik)+"r. "+self.rodzaj_paliwa
        
    def oblicz_przebieg_na_rok(self):
        return self.przebieg/(datetime.datetime.now().year-int(self.rocznik))
    
    def dodaj_wlasciciela(self,wlasciciel):
        self.wlasciciele.append(wlasciciel)

    pass

samochod_1 = Samochod('Volkswagen', 'Passat', 1.9, 'czarny', 200000, 13000, 2006, 'Diesel')
samochod_2 = Samochod('Ford', 'Focus', 1.6, 'czerwony', 150000, 10000, 2010, 'Benzyna')
samochod_3 = Samochod('BMW', 'X5', 3.0, 'biały', 80000, 50000, 2015, 'Diesel')
samochod_4 = Samochod('Audi', 'A4', 2.0, 'srebrny', 120000, 20000, 2012, 'Benzyna')
print(samochod_1)
print(samochod_2)
print(samochod_3)
print(samochod_4)

print(samochod_1.oblicz_przebieg_na_rok())
print(samochod_2.oblicz_przebieg_na_rok())
print(samochod_3.oblicz_przebieg_na_rok())
print(samochod_4.oblicz_przebieg_na_rok())

samochod_1.dodaj_wlasciciela("Jan Kowalski")
samochod_2.dodaj_wlasciciela("Adam Nowak")
samochod_3.dodaj_wlasciciela("Katarzyna Miła")
samochod_4.dodaj_wlasciciela("Tomasz Mądry")

print(samochod_1.wlasciciele)
print(samochod_2.wlasciciele)
print(samochod_3.wlasciciele)
print(samochod_4.wlasciciele)