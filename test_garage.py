from garage import enter garage

def test_enter_garage():
    garageDict = {
    "capacity": 10,   # total number of spots
    "cars": {}         # car_id -> entry_hour (int)
    }
    enter_garage(garageDict, "Bugatti7", 13)
    assert "Bugatti7" in garageDict[cars].keys()