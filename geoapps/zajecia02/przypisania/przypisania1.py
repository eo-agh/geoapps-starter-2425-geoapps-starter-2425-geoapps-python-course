def zaj02_przypisania1():
    #zad1
    dane = (2024, 'Python', 3.8)

    rok, jezyk, wersja = dane

    print(f"Rok: {rok}")
    print(f"Jezyk: {jezyk}")
    print(f"Wersja: {wersja}")

    #zad2
    oceny = [4, 3, 5, 2, 5, 4]

    pierwsza, *srodek, ostatnia = oceny

    print(f"Pierwsza ocena: {pierwsza}")
    print(f"Ostatnia ocena: {ostatnia}")
    print(f"Reszta ocen: {srodek}\n")

    #zad3
    info = ('Jan', 'Kowalski', 30, 'Polska', 'programista')

    imie, nazwisko, *_,zawod = info

    print(f"Imie: {imie}")
    print(f"Nazwisko: {nazwisko}")
    print(f"Zawod: {zawod}\n")

    #zad4
    dane = (2024, ['Python', 3.8, ('Stabilna', 'Wersja')])
    rok, [jezyk, wersja, opis] = dane


    print(f"Rok: {rok}")
    print(f"Jezyk: {jezyk}")
    print(f"Wersja: {wersja}")
    print(f"Opis: {opis}\n")
    
if __name__ == "__main__":
    zaj02_przypisania1()