from . import czas
import time
import importlib

def zaj01_skrypt1():
    
    print(czas.aktualny_czas)

    time.sleep(20)
    print(czas.aktualny_czas)

    importlib.reload(czas)
    print(czas.aktualny_czas)
    
if __name__ == "__main__":
    zaj01_skrypt1()