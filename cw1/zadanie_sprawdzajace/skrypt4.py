import json
path_j = "./cw1/zadanie_sprawdzajace/teksty.json"
# path_j = "teksty.json"
with open(path_j) as json_data:
    teksty = json.load(json_data)
    json_data.close()

print(f"Zawartosc slownika: {teksty}")
print(f"Typ zmiennej: {type(teksty)}")

print()

for ix, el in enumerate(teksty['teksty']):
    for k, v in el.items():
        teksty['teksty'][ix][k] = v.lower()
print("Cala zawartosc zmiennej jako male litery:")
print(teksty)
print("Typ zmiennej po zmianach: " + str(type(teksty)))

for ix, el in enumerate(teksty['teksty']):
    for k, v in el.items():
        teksty['teksty'][ix][k] = list(v.split())   
print("Cala zawartosc zmiennej podzielona na wyrazy:")
print(teksty)
print("Typ zmiennej po zmianach: " + str(type(teksty)))

for ix, el in enumerate(teksty['teksty']):
    for k, v in el.items():
        for ixx, ell in enumerate(v):
            ell = ell.replace('.', '')
            teksty['teksty'][ix][k][ixx] = ell.replace(',', '')
print("Cala zawartosc zmiennej bez znakow interpunkcyjnych:")
print(teksty)
print("Typ zmiennej po zmianach: " + str(type(teksty)))

for ix, el in enumerate(teksty['teksty']):
    for k, v in el.items():
        for ixx, ell in enumerate(v):
            teksty['teksty'][ix][k][ixx] = str(ell[:-1] + ell[-1].upper())
print("Cala zawartosc zmiennej po zmodyfikowaniu tak by w każdym wyrazie ostatni znak był w formacie dużej litery:")
print(teksty)
print("Typ zmiennej po zmianach: " + str(type(teksty)))
print()

for ix, el in enumerate(teksty['teksty']):
    for k, v in el.items():
        #1 sposob
        teksty['teksty'][ix][k] = [x for x in v if 'a' not in x.lower()]
        #2 sposob
        # for ixx, ell in enumerate(v):
        #     if 'a' in ell.lower():
        #         teksty['teksty'][ix][k][ixx] = 0
        # while 0 in teksty['teksty'][ix][k]:
        #     teksty['teksty'][ix][k].remove(0)
print("Cala zawartosc zmiennej po usunieciu wyrazow, zawierajacych a:")
print(teksty)  

pom_list = list()           
for ix, el in enumerate(teksty['teksty']):
    for k, v in el.items():
        pom = [x for x in v if v.count(x) < 2]
        pom_list += pom

unikat = [x for x in pom_list if pom_list.count(x) < 2]
unikalne_slowa = {"unikalne_slowa":unikat}
print("Unikalne wartosci ze wszystkich tekstow: ")
print(unikalne_slowa)

il_poszczegolnych_slow_os_tx = {"teksty": [1,1,1,1,1]}
for ix, el in enumerate(teksty['teksty']):
    for k, v in el.items():
        il_poszczegolnych_slow_os_tx['teksty'][ix] = {k+"_slowa":[]}
        slowa = set(v)
        pom_dict = dict()
        for slowo in slowa:
            one_word = {slowo:v.count(slowo)}
            pom_dict = dict(pom_dict.items() | one_word.items())
        il_poszczegolnych_slow_os_tx['teksty'][ix][k+"_slowa"] = pom_dict
print("Zmienna, ktora przetrzymuje ilosc wystapien dla kazdego ze slow wystepujacych w odpowiednim tescie: ")
print(il_poszczegolnych_slow_os_tx)

pom_slowa = list()
for ix, el in enumerate(teksty['teksty']):
    for k, v in el.items():
        pom_slowa += v

slowa = set(pom_slowa)
il_poszczegolnych_slow_calosc = {"teksty":pom_slowa, "slowa":[]}
pom_dict2 = dict()
for slowo in slowa:
    one_word = {slowo:pom_slowa.count(slowo)}
    pom_dict2 = dict(pom_dict2.items() | one_word.items())
il_poszczegolnych_slow_calosc['slowa'] = pom_dict2

print("Zmienna, ktora przetrzymuje ilosc wystapien dla kazdego ze slow wystepujacych w tekstach: ")
print(il_poszczegolnych_slow_calosc)

with open("./cw1/zadanie_sprawdzajace/zadanie_spr.json", "w", encoding="utf-8") as plik:
    json.dump(unikalne_slowa, plik, ensure_ascii=False, indent=4)
    
with open("./cw1/zadanie_sprawdzajace/zadanie_spr.json", "a", encoding="utf-8") as plik:
    json.dump(il_poszczegolnych_slow_os_tx, plik, ensure_ascii=False, indent=4)
    
with open("./cw1/zadanie_sprawdzajace/zadanie_spr.json", "a", encoding="utf-8") as plik:
    json.dump(il_poszczegolnych_slow_calosc, plik, ensure_ascii=False, indent=4)
