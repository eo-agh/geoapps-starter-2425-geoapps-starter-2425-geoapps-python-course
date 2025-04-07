from .ambulance import Ambulance

class Station:
    __max_id = 0


    def __init__(self, location, ambulance, driver, staff_member):
        Station.__max_id += 1
        self.id = Station.__max_id
        self.location = location
        self.ambulance = ambulance
        self.driver = driver
        self.staff_member = staff_member

    def is_ambulance_at_station(self):
        return self.location == self.ambulance.location

    def __str__(self):
        return f"Station ID: {self.id}, Location: {self.location}, Ambulance ID: {self.ambulance.id}, Driver: {self.driver}, Staff Member: {self.staff_member}\n"


if __name__ == "__main__":
    ambulance1 = Ambulance(
        vehicle_type="AZ124",
        status="Available",
        location=(50.095340, 19.920282),
        medical_equipment=["defibrillator", "stretcher"]
    )

    station1 = Station(
        location=(50.095340, 19.920282),
        ambulance=ambulance1,
        driver="John Doe",
        staff="Jane Smith"
    )

    print(station1)
    print("Is ambulance at station?", station1.is_ambulance_at_station())

    ambulance1.update_location((50.100000, 19.920000))
    print("Is ambulance at station?", station1.is_ambulance_at_station())
