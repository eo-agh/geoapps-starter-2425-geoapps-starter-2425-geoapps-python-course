import datetime
import random


def zmierz_czas(unit="seconds"):
    def dekorator(funkcja):
        def wrapper(*args, **kwargs):
            start = datetime.datetime.now()
            wynik = funkcja(*args, **kwargs)
            end = datetime.datetime.now()
            czas_dzialania = (end - start).total_seconds()
            if unit == "seconds":
                print(f"Funkcja {funkcja.__name__} wykonala sie w {czas_dzialania} s")
            elif unit == "microseconds":
                print(
                    f"Funkcja {funkcja.__name__} wykonala sie w {czas_dzialania * 1000000} us"
                )
            return wynik

        return wrapper

    return dekorator


@zmierz_czas("seconds")
def znajdz_liczbe_w_s():
    """
    Funkcja losuje liczbe z przedzialu od 1 do 100.
    Poczatkowo nie przyjmuje zadnych argumentow.
    Funkcja konczy dzialanie, kiedy uzytkownik znajdzie wylosowana liczbe.
    """
    szukana = random.randint(1, 100)
    proby = 1
    print("Zostala wylosowana liczba od 1 do 100. Znajdz ja!")
    liczba = int(input("Wpisz liczbe: "))

    while liczba != szukana:
        if liczba > szukana:
            print("\nPodana liczba jest wieksza niz wylosowana. \nSprobuj jeszcze raz")
        elif liczba < szukana:
            print("\nPodana liczba jest mniejsza niz wylosowana. \nSprobuj jeszcze raz")
        liczba = int(input("Podaj liczbe: "))
        proby += 1

    if proby == 1:
        print(
            f"\n Wygrales!!!\nOdgadnieta liczba to: {szukana}, by ja odnalezc potrzebowalxs {proby} proby"
        )
    else:
        print(
            f"\n Wygrales!!!\nOdgadnieta liczba to: {szukana}, by ja odnalezc potrzebowalxs {proby} prob"
        )


@zmierz_czas("microseconds")
def znajdz_liczbe_w_us():
    """
    Funkcja losuje liczbe z przedzialu od 1 do 100.
    Poczatkowo nie przyjmuje zadnych argumentow.
    Funkcja konczy dzialanie, kiedy uzytkownik znajdzie wylosowana liczbe.
    """
    szukana = random.randint(1, 100)
    proby = 1
    print("Zostala wylosowana liczba od 1 do 100. Znajdz ja!")
    liczba = int(input("Wpisz liczbe: "))

    while liczba != szukana:
        if liczba > szukana:
            print("\nPodana liczba jest wieksza niz wylosowana. Sprobuj ponownie.")
        elif liczba < szukana:
            print("\nPodana liczba jest mniejsza niz wylosowana. Sprobuj ponownie.")
        liczba = int(input("Wpisz liczbe: "))
        proby += 1

    if proby == 1:
        print(
            f"\n Wygrales!!!\nOdgadnieta liczba to: {szukana}, by ja odnalezc potrzebowalxs {proby} proby"
        )
    else:
        print(
            f"\n Wygrales!!!\nOdgadnieta liczba to: {szukana}, by ja odnalezc potrzebowalxs {proby} prob"
        )


@zmierz_czas("seconds")
def wypelnienie_listy_100_w_s():
    lista = []
    for a in range(100):
        lista.append(a)
    lista.clear()


@zmierz_czas("microseconds")
def wypelnienie_listy_100_w_us():
    lista = []
    for a in range(100):
        lista.append(a)
    lista.clear()


if __name__ == "__main__":
    # znajdz_liczbe_w_s()
    # znajdz_liczbe_w_us()
    wypelnienie_listy_100_w_s()
    wypelnienie_listy_100_w_us()
