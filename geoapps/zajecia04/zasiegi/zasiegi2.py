def licznik_nonlocal():
    licznik_stanu_nonlocal = 0

    def zwieksz():
        nonlocal licznik_stanu_nonlocal
        licznik_stanu_nonlocal += 1
        return licznik_stanu_nonlocal

    return zwieksz


licznik_stanu_global = 0


def licznik_global():
    global licznik_stanu_global
    licznik_stanu_global += 1
    return licznik_stanu_global


class Licznik_class:
    def __init__(self):
        self.licznik_stanu_class = 0

    def __call__(self):
        self.licznik_stanu_class += 1
        return self.licznik_stanu_class


def licznik_funkcyjny():
    licznik_funkcyjny.licznik_f += 1
    return licznik_funkcyjny.licznik_f


def zaj04_zasiegi2():
    li_pr1 = licznik_nonlocal()
    print("Licznik nonlocal:")
    print(li_pr1())
    print(li_pr1())

    print("Licznik globalny:")
    print(licznik_global())
    print(licznik_global())

    li_pr2 = Licznik_class()
    print("Licznik klasy:")
    print(li_pr2())
    print(li_pr2())

    licznik_funkcyjny.licznik_f = 0
    print("Licznik funkcyjny:")
    print(licznik_funkcyjny())
    print(licznik_funkcyjny())


if __name__ == "__main__":
    zaj04_zasiegi2()
