def zmien_wartosc(arg):
    if isinstance(arg, int):
        arg = 65482652
    elif isinstance(arg, list):
        arg[0] = 'kalafior'
        
x = 10
y = [1, 3, 'z']
print(f"Liczba: {x}; Lista: {y}")

zmien_wartosc(x)
zmien_wartosc(y)

print("Po uzyciu funkcji")
print(f"Liczba: {x}; Lista: {y}")