K = [1, 2]
L = K
# konkatenacja
K = K + [3, 4]
M = [1, 2]
N = M
# przypisanie rozszerzone
M += [3, 4]

print(f"Konkatencja\nK: {K}; L: {L}")
print(f"Przypisanie rozszerzone\nM: {M}; N: {N}")

#kontrachencja laczy ciagi znakow, sekwencje lub struktury danych w jeden nowy dluzszy ciag/strukture, 
# a przypisania rozszerzone modyfikują wartość zmiennej i przypisują wynik (zachowuje referencje --> wspoldzielona referencja)