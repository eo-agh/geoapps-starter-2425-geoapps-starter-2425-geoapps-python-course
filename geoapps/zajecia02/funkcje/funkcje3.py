def stworz_raport(*args, **kwargs):
    for id in args:
        info = dict()
        for key, value in kwargs.items():
            key_r = key.replace("_", " ")
            key_rs = key_r.split()
            if int(key_rs[1]) == id:
                info.update({key_rs[0]: value})
        print(f"Raport produktu o nr ID: {id}\n{info}")
        del info


def zaj02_funkcje3():
    stworz_raport(
        101,
        102,
        nazwa_101="Kubek termiczny",
        cena_101="45.99 zł",
        nazwa_102="Długopis",
        cena_102="4.99 zł",
    )


if __name__ == "__main__":
    zaj02_funkcje3()
