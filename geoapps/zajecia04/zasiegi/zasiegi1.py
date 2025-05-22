def stworz_funkcje_potegujaca(wykladnik):
    def poteguj(podstawa):
        return podstawa**wykladnik

    return poteguj


def zaj04_zasiegi1():
    potega_2 = stworz_funkcje_potegujaca(2)
    print(potega_2(4))

    potega_3 = stworz_funkcje_potegujaca(3)
    print(potega_3(2))


if __name__ == "__main__":
    zaj04_zasiegi1()
