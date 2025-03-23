ksiazki = [
    {"tytul": "Władca Pierścieni", "autor": "J.R.R. Tolkien", "rok_wydania": 1954},
    {"tytul": "Harry Potter i Kamień Filozoficzny", "autor": "J.K. Rowling", "rok_wydania": 1997},
    {"tytul": "Duma i uprzedzenie", "autor": "Jane Austen", "rok_wydania": 1813},
    {"tytul": "Rok 1984", "autor": "George Orwell", "rok_wydania": 1949},
    {"tytul": "Zbrodnia i kara", "autor": "Fiodor Dostojewski", "rok_wydania": 1866},
    {"tytul": "Mistrz i Małgorzata", "autor": "Michaił Bułhakow", "rok_wydania": 1967},
    {"tytul": "Hobbit", "autor": "J.R.R. Tolkien", "rok_wydania": 1937},
    {"tytul": "Sto lat samotności", "autor": "Gabriel García Márquez", "rok_wydania": 1967},
    {"tytul": "Imię róży", "autor": "Umberto Eco", "rok_wydania": 1980},
    {"tytul": "Solaris", "autor": "Stanisław Lem", "rok_wydania": 1961},
]

print(f"Lista ksiazek: {ksiazki}\n")
print(f"Posortowane ksiazki wg roku wydania: {sorted(ksiazki, key=lambda i: i['rok_wydania'])}\n")

ksiazki_po_2000 = list(filter(lambda i: i['rok_wydania'] > 2000, ksiazki))
print(f"Ksiazki wydane po 2000 roku: {ksiazki_po_2000}\n")

print(f"Tytuly ksiazek: {list(map(lambda x: x["tytul"], ksiazki))}")