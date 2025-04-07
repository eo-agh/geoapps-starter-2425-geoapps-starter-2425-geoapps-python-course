# from geoapps.zajecia03.fleet.ambulance import Ambulance
# from geoapps.zajecia03.operations import *
# from geoapps.zajecia03.personnel import *
# import geoapps
import geoapps.zajecia03 as zaj03

def run_application():
    # Zdefiniowanie naszych zasobów
    ambulance1 = zaj03.fleet.Ambulance(1, "Type A", "available", (50.095340, 18.920282), ["Defibrillator", "Oxygen tank"])
    ambulance2 = zaj03.fleet.Ambulance(2, "Type B", "on mission", (50.095340, 19.920282), ["Stretcher", "First Aid Kit"])
    
    employee1 = zaj03.personnel.Employee("John", "Doe", 123, 12000.0)
    employee2 = zaj03.personnelEmployee("Jane", "Smith", 124, 8000.0)

    driver1 = zaj03.personnel.Driver("Mike", "Johnson", 125, 10000.0, "DL12345", ["BLS"])
    driver2 = zaj03.personnel.Driver("Anna", "Brown", 126, 11500.0, "DL12346", ["ALS", "PHTLS"])

    # Sprawdzenie czy to czasem nie są te same karetki
    if ambulance1 == ambulance2:
        raise ValueError("To są te same karetki!")
    # Sprawdzenie ile mamy karetek
    print(zaj03.fleet.Ambulance.get_instances_count())

    # Stworzenie kolejki
    queue = zaj03.operations.IncidentQueue()

    # Zaraportowanie 2 zgłoszeń
    incident1 = zaj03.operations.Incident(1, "Power outage in sector 4")
    incident2 = zaj03.operations.Incident(2, "Fire alarm in building 21")
    queue += incident1
    queue += incident2

    # Wypisz wszystkie zgłoszenia
    print("Aktualne zgłoszenia:")
    print(queue)

    # Daj kierowcy podwyżkę za super zasługi
    print(f"Przed podwyżką: {driver1.display_info()}")
    driver1.update_salary(5000.12)
    print(f"Po podwyżce: {driver1.display_info()}")


if __name__ == "__main__":
    run_application()