def zaj01_skrypt3():
    imiona = ["Jan", "Maria", "Piotr"]

    for ix, el in enumerate(imiona):
        print(f"Nr indeksu: {ix} - wartosc: {el}")

    print("\nProgram sprawdzajacy, czy dana liczba jest parzysta i dodatnia")
    x = float(input("Podaj liczbe: "))
    if x > 0 and x % 2 == 0:
        print(f"Liczba {x} jest dodatnia i parzysta")
    else:
        print(f"Liczba {x} nie jest dodatnia i/lub nie jest parzysta")

    print(
        "\nProgram sprawdzajacy, czy wprowadzona przez użytkownika liczba nie jest równa zero"
    )
    y = float(input("Podaj liczbe: "))
    if not (y == 0):  # if y != 0:
        print(f"Liczba {y} jest rozna od zera")
    else:
        print(f"Liczba {y} to zero")

    print("\nProgram sprawdzajacy, czy wybrany przez użytkownika owoc jest na liscie")
    owoc = input("Podaj owoc: ")
    owoce = ["kiwi", "banan", "mandarynka", "liczi"]
    print(f"Lista owocow: {owoce}")
    if owoc in owoce:
        print("Owoc jest dostępny")
    else:
        print("Owoc nie wystepuje w rejestrze")

    print("\nPetla konczaca sie przy przekroczeniu wartosci rownej 100")
    suma = 0
    while suma < 100:
        liczba = float(input("Podaj liczbe: "))
        suma += liczba
    print(f"Suma wprowadzonych liczb: {suma}")


if __name__ == "__main__":
    zaj01_skrypt3()
