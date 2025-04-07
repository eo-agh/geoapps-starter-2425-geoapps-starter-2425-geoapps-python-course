from geoapps.zajecia03.fleet import *
from geoapps.zajecia03.operations import *
from geoapps.zajecia03.personnel import *
from geoapps.zajecia03.management import *
from time import sleep

def run_application():
    # Zdefiniowanie naszych zasobów
    ambulance1 = Ambulance("Type A", "available", (50.095340, 18.920282), ["Defibrillator", "Oxygen tank"])
    ambulance2 = Ambulance("Type B", "available", (50.095340, 19.920282), ["Stretcher", "First Aid Kit"])

    employee1 = Employee("John", "Doe", 12000.0)
    employee2 = Employee("Jane", "Smith", 8000.0)

    driver1 = Driver("Mike", "Johnson", 10000.0, "DL12345", ["BLS"])
    driver2 = Driver("Anna", "Brown", 11500.0, "DL12346", ["ALS", "PHTLS"])

    # Sprawdzenie czy to czasem nie są te same karetki
    if ambulance1 == ambulance2:
        raise ValueError("To są te same karetki!")
    # Sprawdzenie ile mamy karetek
    print(Ambulance.get_instances_count())

    # Stworzenie kolejki
    queue = IncidentQueue()

    # Zaraportowanie 2 zgłoszeń
    incident1 = Incident("Power outage in sector 4", "low", (50.9148, 18.3847), "John Smith")
    sleep(10)
    incident2 = Incident("Fire alarm in building 21", "high", (50.1478, 19.901487), "Linda Umer")
    queue += incident1
    queue += incident2

    # Wypisz wszystkie zgłoszenia
    print("Aktualne zgłoszenia:")
    print(queue)

    # Daj kierowcy podwyżkę za super zasługi
    print(f"Przed podwyżką: {driver1.display_info()}")
    driver1.update_salary(15000.12)
    print(f"Po podwyżce: {driver1.display_info()}")

    station1 = Station(location=(50.095340, 19.920282), ambulance=ambulance1, driver="John Doe", staff_member="Jane Smith")
    
    print(station1)
    print("Czy karetka jest na stacji?", station1.is_ambulance_at_station())

    ambulance1.update_location((50.095340, 19.920282))
    print("Czy karetka jest na stacji? (Po aktualizacji lokalizacji)", station1.is_ambulance_at_station())

    sleep(20)
    incident3 = Incident("Power outage in sector 4", "low", (50.923145, 18.917486), "Amy King")
    sleep(15)
    incident5 = Incident("Fire alarm in building 21", "high", (50.923145, 19.017486), "Phill Poe")
    sleep(20)
    incident4 = Incident("Fire alarm in building 129", "medium", (50.023145, 18.907486), "Mindy Lote")
    queue += incident3
    queue += incident5
    queue = queue + incident4

    print(f"---------- wyświetlanie za pomocą __str__ ----------")
    print(queue)
    print()
    print(f"---------- Sortowanie ----------")
    print(queue.sort_incidents())

    ambulances = [ambulance1, ambulance2]
    management = Management(queue.sort_incidents(), ambulances)    
    
    print()
    print(management.assign_ambulances())


if __name__ == "__main__":
    run_application()