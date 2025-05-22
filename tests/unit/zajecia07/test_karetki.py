from geoapps.zajecia03.fleet.ambulance import Ambulance


def test_ambulance_creation():
    a = Ambulance("TypeA", "available", (50.0, 19.0), ["oxygen", "stretcher"])
    assert a.vehicle_type == "TypeA"
    assert a.status == "available"
    assert a.location == (50.0, 19.0)
    assert "oxygen" in a.medical_equipment


def test_update_location():
    a = Ambulance("TypeB", "on_mission", (10.0, 20.0), [])
    a.update_location((30.0, 40.0))
    assert a.location == (30.0, 40.0)


def test_ambulance_equality():
    a1 = Ambulance("TypeC", "available", (0, 0), [])
    a2 = Ambulance("TypeC", "available", (0, 0), [])
    assert a1 != a2


def test_validate_id():
    assert Ambulance.validate_id(10) is True
    assert Ambulance.validate_id(-5) is False
    assert Ambulance.validate_id("abc") is False


def test_get_instances_count():
    count = Ambulance.get_instances_count()
    assert "Number of working ambulances:" in count
