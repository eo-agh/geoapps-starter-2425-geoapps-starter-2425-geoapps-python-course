def stworz_funkcje_potegujaca(wykladnik):
    def poteguj(podstawa):
        return podstawa ** wykladnik
    return poteguj

potega_2 = stworz_funkcje_potegujaca(2)  # Tworzy funkcję potęgującą do kwadratu
print(potega_2(4))

potega_3 = stworz_funkcje_potegujaca(3)
print(potega_3(2)) 