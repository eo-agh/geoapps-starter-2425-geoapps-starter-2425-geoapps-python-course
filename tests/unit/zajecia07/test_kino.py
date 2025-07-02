from geoapps.zajecia05.wyjatki.wyjatki import (
    BrakMiejscException,
    MiejsceZajeteException,
    NieprawidlowaAnulacjaException,
    SalaKinowa,
    UzytkownikJuzZarezerwowalException,
)
import pytest


def test_rezerwacja_i_anulacja():
    sala1 = SalaKinowa(1, 2)
    sala1.zarezerwuj("A1", "Jan Kowalski")
    assert sala1.miejsca["A1"]["status"] == "zajete"

    sala1.anuluj_rezerwacje("A1", "Jan Kowalski")
    assert sala1.miejsca["A1"]["status"] == "wolne"


def test_zajete_miejsce_exception():
    sala2 = SalaKinowa(1, 2)
    sala2.zarezerwuj("A1", "Anna Nowak")
    with pytest.raises(MiejsceZajeteException):
        sala2.zarezerwuj("A1", "Jan Kowalski")


def test_uzytkownik_juz_ma_rezerwacje():
    sala3 = SalaKinowa(1, 2)
    sala3.zarezerwuj("A2", "Jakub Nowak")
    with pytest.raises(UzytkownikJuzZarezerwowalException):
        sala3.zarezerwuj("A1", "Jakub Nowak")


def test_anulacja_nieprawidlowa():
    sala4 = SalaKinowa(1, 1)
    sala4.zarezerwuj("A1", "Anna Nowak")
    with pytest.raises(NieprawidlowaAnulacjaException):
        sala4.anuluj_rezerwacje("A1", "Jan Kowalski")


def test_brak_miejsc_exception():
    sala5 = SalaKinowa(1, 1)
    sala5.zarezerwuj("A1", "User 1")
    with pytest.raises(BrakMiejscException):
        sala5.zarezerwuj("A2", "User 2")
