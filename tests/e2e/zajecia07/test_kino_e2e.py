# from geoapps.zajecia05.wyjatki.wyjatki import *

from geoapps.zajecia05.wyjatki.wyjatki import SalaKinowa, SalaKinowaException


def test_e2e_kino_workflow():
    sala = SalaKinowa(2, 3)

    try:
        sala.zarezerwuj("A1", "Jan Kowalski")
        sala.zarezerwuj("A2", "Anna Nowak")
    except SalaKinowaException:
        assert False, "Rezerwacja nie powinna się nie powieść"

    try:
        sala.zarezerwuj("A1", "Adam Nowak")
        assert False, "Powinien zostać rzucony wyjątek"
    except SalaKinowaException:
        pass

    try:
        sala.anuluj_rezerwacje("A1", "Jan Kowalski")
        sala.anuluj_rezerwacje("A2", "Anna Nowak")
    except SalaKinowaException:
        assert False, "Anulacja nie powinna się nie powieść"

    for m in ["A1", "A2"]:
        assert sala.miejsca[m]["status"] == "wolne"
