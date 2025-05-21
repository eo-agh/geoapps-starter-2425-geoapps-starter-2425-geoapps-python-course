from geoapps.zajecia03.fleet.ambulance import *

def test_e2e_ambulance_workflow():
    a1 = Ambulance("AZ124", "available", (50.1, 19.9), ["defibrillator"])
    a2 = Ambulance("AZ125", "on_mission", (50.2, 19.8), [])

    assert a1.status == "available"
    a1.update_location((51.0, 20.0))
    assert a1.location == (51.0, 20.0)
    assert a1 != a2
    assert Ambulance.validate_id(a1.id)