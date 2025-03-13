wartosc = 100
print("Wartosc: " + str(wartosc))
print("Typ zmiennej wartosc: " + str(type(wartosc)))

dodawanie = wartosc + 123.15
print("Dodawanie: " + str(dodawanie))
print("Typ zmiennej dodawanie: " + str(type(dodawanie)))

#potega = dodawanie ** 12345 --> blad; liczba poza skala
potega = dodawanie ** 12
print("Potega: " + str(potega))
print("Typ zmiennej potega: " + str(type(potega)))

tekst = str(potega)
print("Tekst: " + str(tekst))
print("Typ zmiennej tekst: " + str(type(tekst)))

from math import pi
wartosc_pi = pi
print("Wartosc_pi: " + str(wartosc_pi))
print("Typ zmiennej wartosc_pi: " + str(type(wartosc_pi)))

li = [1,2,3,4,5]

from random import randint
los = randint(0, 4)
losowa = li[los]
print("Lista: " + str(li))
print("Wylosowana liczba z listy: " + str(losowa))
print("Typ zmiennej losowa: " + str(type(losowa)))

tekst = f"Wartosc: {tekst}"
print("Dlugosc zmiennej tekst po nadpisaniu: " + str(len(tekst)))
print("Typ zmiennej tekst po nadpisaniu: " + str(type(tekst)))
print("wybrany fragment ze zmiennej tekst po nadpisaniu: " + tekst[1:4])
print(dir(tekst))
tekst = tekst.upper()
print("Kolejne nadpisanie zmiennej tekst: " + tekst)

#tekst[1] = "p" --> blad
print("Zamiana drugiej pozycji zmiennej tekst na p: " + tekst.replace("A","p"))

lista = list(tekst)
print("Zawartosc zmiennej lista: " + str(lista))
print("Typ zmiennej lista: " + str(type(lista)))

lista = lista[0:8]
print("Zawartosc zmiennej lista po obcieciu: " + str(lista))
print("Typ zmiennej lista po obcieciu: " + str(type(lista)))

lista = lista + li
print("Zawartosc zmiennej lista po dodaniu innej listy: " + str(lista))
print("Typ zmiennej lista po dodaniu innej listy: " + str(type(lista)))

lista.remove(":")
print("Zawartosc zmiennej lista po usunieciu dwukropka: " + str(lista))
print("Typ zmiennej lista po usunieciu dwukropka: " + str(type(lista)))

lista2 = [1,2,3,"banan",100]

lista3 = [x ** 2 for x in lista2 if x != "banan"]

lista4 = [x for x in range(2, 17) if x % 2 == 0]

print("Lista2: " + str(lista2))
print("Lista3: " + str(lista3))
print("Lista4: " + str(lista4))
print("Typ zmiennej lista2: " + str(type(lista2)))
print("Typ zmiennej lista3: " + str(type(lista3)))
print("Typ zmiennej lista4: " + str(type(lista4)))

ja = {}
print("Typ zmiennej ja: " + str(type(ja)))

ja = {
    "imie":"Martyna", 
    "nazwisko":"Sala", 
    "wiek":21, 
    "moje_hobby":[{"nazwa":"origami", "dlaczego:":"lubie skladac papier w rozne ksztalty, bardzo mnie to relaksuje"},
                  {"nazwa":"ukladanie puzzli", "dlaczego:":"dzieki temu nie musze myslec o niczym innym"},
                  {"nazwa":"szydelkowanie","dlaczego:":"odprezajace dla mnie zajecie po stresujacym dniu"},
                  {"nazwa":"czytanie ksiazek","dlaczego:":"oderwanie od rzeczywistosci"}]
}
print("Typ zmiennej ja: " + str(type(ja)))

print("Wartosc klucza moje_hobby:" + str(ja["moje_hobby"]))

print("Kulucze w slowniku ja:" + str(ja.keys()))

czy = False
if "adres" in ja.keys():
    czy = True

print("W zmiennej ja znajduje sie klucz adres: " + str(czy))
print("Typ zmiennej odpowiedzialnej zasprawdzenie prawdziwosci wczesniejszego zdania: " + str(type(czy)))

krotka1 = (1,2,"3",4,2,5)
print("Zawartosc zmiennej krotka1: " + str(krotka1))
print("Typ zmiennej krotka1: " + str(type(krotka1)))

print("Dlugosc zmiennej krotka1: " + str(len(krotka1)) + ". Pierwszy wyraz zmiennej krotka1: " + str(krotka1[0]))

il2 = 0
for el in krotka1:
    if el == 2:
        il2 += 1
print("Ilosc występowania wartosci 2 w zmiennej krotka1: " + str(il2))

#zmiana elementu zmiennej typu tuple (krotka) na dwa sposoby:
#krotka1[0] = 2 --> blad, jesli typ zmiennej to tuple
#by wykonac ta linijke kodu najpierw trzeba zmienic typ zmiennej na liste
krotka1 = list(krotka1)
krotka1[0] = 2
#i wracamy do typu tuple
krotka1 = tuple(krotka1)

#lub poczaczyc krotki
# krotka1 = (2,) + krotka1[1:]
print("Wartości nadpisananej zmiennej krotka1 (zmiana wartosci dla pierwszego elementu): " + str(krotka1))
print("Typ zmiennej krotka1 po nadpisaniu: " + str(type(krotka1)))

X = set("kalarepa")
Y = set("lepy")

print("Zmienna X: ", + str(X))
print("Typ zmiennej X: " + str(type(X)))
print("Zmienna Y: " + str(Y))
print("Typ zmiennej Y: " + str(type(X)))

print(f"Czesc wspolna zmiennych X i Y: ", X & Y)