#1 sposob
def dni_tygodnia():
    dni_tyg = ["poniedzialek", "wtorek", "sroda", "czwartek", "piatek", "sobota", "niedziela"]
    for dzien in dni_tyg:
        yield dzien   

def zaj02_generatory():
    print("\n1 sposob")
    dni_tygodnia1 = dni_tygodnia()

    print("\nPierwsze trzy dni tygodnia:")    
    for x in range(3):
        print(next(dni_tygodnia1))
    print("\nReszta dni:")
    for x in dni_tygodnia1:
        print(x)

    #2 sposob
    print("\n\n2 sposob")
    dni_tyg = ["poniedzialek", "wtorek", "sroda", "czwartek", "piatek", "sobota", "niedziela"]
    dni_tygodnia2 = (x for x in dni_tyg)

    print("\nPierwsze trzy dni tygodnia:")    
    for x in range(3):
        print(next(dni_tygodnia2))
    print("\nReszta dni:")  
    for x in dni_tygodnia2:
        print(x)

if __name__ == "__main__":
    zaj02_generatory()