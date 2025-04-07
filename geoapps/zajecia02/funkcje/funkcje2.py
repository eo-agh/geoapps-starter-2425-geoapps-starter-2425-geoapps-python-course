def zamowienie_produktu(nazwa_produktu, *, cena, ilosc = 1):
    wartosc_zamowienia = cena*ilosc
    podsumowanie = f"Podsumowanie:\nProdukt: {nazwa_produktu}.\nLaczna cena: {wartosc_zamowienia}.\nIlosc zamowionego produktu: {ilosc}.\n"
    return podsumowanie, wartosc_zamowienia
    
def zaj02_funkcje2():
    zamowienia = []
    zamowienia.append(zamowienie_produktu("lodowka", cena=3500, ilosc=2))
    zamowienia.append(zamowienie_produktu("pralka", cena=2000, ilosc=1))
    zamowienia.append(zamowienie_produktu("mikser", cena=300, ilosc=3))

    for podsumowanie, _ in zamowienia:
        print(podsumowanie)

    suma_zamowien = sum(zamowienie for _, zamowienie in zamowienia)
    print(f"Łączna wartość wszystkich zamówień: {suma_zamowien:.2f} zł")
    
if __name__ == "__main__":
    zaj02_funkcje2()
