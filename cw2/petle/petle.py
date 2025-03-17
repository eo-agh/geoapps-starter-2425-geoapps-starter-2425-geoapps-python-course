#zad1
imiona = ['Anna', 'Jan', 'Ewa', 'Karol']
oceny = [5, 4, 3]

for imie, ocena in zip(imiona, oceny):
    print(f"{imie} ma {ocena}")
    
#jesli listy maja rozne dlugosci to przestaje iterowac/nie sa wyswietlane dane, ktore nie maja pary\
    
#zad2
liczby = [1, 2, 3, 4, 5]

def kwadrat(x):
    return x ** 2

kwadraty = list(map(kwadrat, liczby))
print(f"Liczby: {liczby}")
print(f"Liczby do kwadratu: {kwadraty}")