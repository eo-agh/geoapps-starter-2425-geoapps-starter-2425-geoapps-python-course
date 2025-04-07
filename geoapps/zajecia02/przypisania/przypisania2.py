def zaj02_przypisania2():
    #zad1
    a = b = [1, 2, 3]

    b[0] = 'zmieniono'
    print(f"Lista a: {a}; lista b: {b}")
    #wspoldzielenie referencji -> obydwie zmienne odnosza sie do tego samego obiektu w pamieci
    #lista jest obiektem mutowalnym, czyli jego elementy/zawartosc moze ulec zmianie po utworzeniu, inne przyklady:zbior, slownik
    #a[0] = 1 -> zmieni pierwszy element listy na 1

    #zad2
    c = list(a) #a[:]
    c[0] = 'nowa wartosc'
    print(f"Lista a: {a}; lista b: {b}; lista c: {c}")
    #kopiowanie zapobieglo wspoldzieleniu referencji, poniewaz lista c (jest nowa instacja obiektu i --> gleboka kopia) nie odnosi sie juz do obiektu kopiowanego (brak refenercji do tego obiektu) 

    #zad3
    x = y = 10
    y += 1
    print(f"zmienna x: {x}; zmienna y: {y}")
    #intigery sa obiektami niemutowalnymi, podobnie jak obiekty typu nt , float , bool , str , tuple oraz Unicode 

if __name__ == "__main__":
    zaj02_przypisania2()