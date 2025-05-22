class SalaKinowaException(Exception):
    """Bazowy wyjatek dla systemu kina."""

    pass


class BrakMiejscException(SalaKinowaException):
    """Wyjatek zglaszany, gdy nie ma juz wolnych miejsc."""

    pass


class MiejsceZajeteException(SalaKinowaException):
    """Wyjatek zglaszany, gdy miejsce jest juz zarezerwowane."""

    pass


class UzytkownikJuzZarezerwowalException(SalaKinowaException):
    """Wyjatek zglaszany, gdy uzytkownik probowal zarezerwowac wiecej niz jedno miejsce."""

    pass


class NieprawidlowaAnulacjaException(SalaKinowaException):
    """Wyjatek zglaszany przy probie anulacji nieprawidlowej rezerwacji."""

    pass


class SalaKinowa:
    """
    Klasa tworzaca sale kinowa.

    Atrybuty:
        rzedy (int): Liczba rzedow w sali. Domysla wartosc jest rowna 2.
        miejsca_na_rzad (int): Liczba miejsc w rzedzie. Domysla wartosc jest rowna 5.

    Metody:
        zarezerwuj(miejsce, imie_nazwisko): Rezerwuje dane miejsce w sali dla uzytkownika.
        anuluj_rezerwacje(miejsce, imie_nazwisko): Anuluje rezerwacje wybranego miejsca przez uzytkownika.
        pokaz_miejsca(): Wypisuje aktualny stan miejsc - "'miejsce': 'status' ('uzytkownik')".
    """

    def __init__(self, rzedy: int = 2, miejsca_na_rzad: int = 5):
        self.miejsca = {}  # np. {'A1': {'status': 'wolne', 'uzytkownik': None}}
        self.rezerwacje_uzytkownikow = {}  # np. {'Jan Kowalski': 'A1'}
        for r in range(rzedy):
            rzad = chr(65 + r)  # lub chr(ord('A') + r)
            for m in range(1, miejsca_na_rzad + 1):
                self.miejsca[f"{rzad}{m}"] = {"status": "wolne", "uzytkownik": None}

    def zarezerwuj(self, miejsce, imie_nazwisko):
        if all(info["status"] == "zajete" for info in self.miejsca.values()):
            raise BrakMiejscException("Brak wolnych miejsc na sali!")

        if miejsce not in self.miejsca:
            raise ValueError(f"Miejsce {miejsce} nie istnieje.")

        if self.miejsca[miejsce]["status"] == "zajete":
            raise MiejsceZajeteException(f"Miejsce {miejsce} jest juz zajete.")

        if imie_nazwisko in self.rezerwacje_uzytkownikow:
            # raise UzytkownikJuzZarezerwowalException("Ten uzytkownik juz zarezerwował miejsce.")
            raise UzytkownikJuzZarezerwowalException(
                f"Uzytkownik {imie_nazwisko} ma juz zarezerwowane miejsce {self.rezerwacje_uzytkownikow[imie_nazwisko]}."
            )

        self.miejsca[miejsce]["status"] = "zajete"
        self.miejsca[miejsce]["uzytkownik"] = imie_nazwisko
        self.rezerwacje_uzytkownikow[imie_nazwisko] = miejsce
        print(f"Zarezerwowano miejsce {miejsce} dla {imie_nazwisko}.")

    def anuluj_rezerwacje(self, miejsce, imie_nazwisko):
        if miejsce not in self.miejsca:
            raise ValueError(f"Miejsce {miejsce} nie istnieje.")

        if self.miejsca[miejsce]["uzytkownik"] != imie_nazwisko:
            # raise NieprawidlowaAnulacjaException("Nie mozna anulowac tej rezerwacji – dane nieprawidlowe.")
            raise NieprawidlowaAnulacjaException(
                f"Rezerwacja na miejscu {miejsce} nie nalezy do uzytkownika {imie_nazwisko}."
            )

        self.miejsca[miejsce]["status"] = "wolne"
        self.miejsca[miejsce]["uzytkownik"] = None
        del self.rezerwacje_uzytkownikow[imie_nazwisko]
        print(f"Anulowano rezerwacje miejsca {miejsce} dla {imie_nazwisko}.")

    def pokaz_miejsca(self):
        print("Stan miejsc:")
        for miejsce, info in self.miejsca.items():
            print(f"{miejsce}: {info['status']} ({info['uzytkownik'] or 'brak'})")


if __name__ == "__main__":
    sala = SalaKinowa()

    try:
        sala.zarezerwuj("A1", "Jan Kowalski")
        sala.zarezerwuj("A2", "Anna Nowak")
        sala.zarezerwuj("A3", "Jan Kowalski")
    except SalaKinowaException as e:
        print(f"\nBłąd: {e}")

    sala.pokaz_miejsca()
    print()
    try:
        sala.anuluj_rezerwacje("A1", "Jan Kowalski")
        sala.anuluj_rezerwacje("A2", "Jan Kowalski")
    except SalaKinowaException as e:
        print(f"\nBłąd: {e}")

    sala.pokaz_miejsca()
    print()
    sala1 = SalaKinowa()

    try:
        sala1.zarezerwuj("A1", "Jan Was")
        sala1.zarezerwuj("A2", "Jan Lis")
        sala1.zarezerwuj("A3", "Jan Noc")
        sala1.zarezerwuj("A4", "Jan Koc")
        sala1.zarezerwuj("A5", "Jan Sas")
        sala1.zarezerwuj("B1", "Jan Rak")
        sala1.zarezerwuj("B2", "Jan Osa")
        sala1.zarezerwuj("B3", "Jan Rok")
        sala1.zarezerwuj("B4", "Jan Wok")
        sala1.zarezerwuj("B5", "Jan Jak")
        sala1.zarezerwuj("A1", "Jan Wan")
    except SalaKinowaException as e:
        print(f"\nBłąd: {e}")

    sala1.pokaz_miejsca()
