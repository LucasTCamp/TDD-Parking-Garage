from garage import enter_garage
import pytest

def test_enter_garage():
    garageDict = {
    "capacity": 10,   # total number of spots
    "cars": {}         # car_id -> entry_hour (int)
    }
    enter_garage(garageDict, "Bugatti7", 13)
    assert "Bugatti7" in garageDict["cars"].keys()


def test_enter_garage_valueError_if_full():
    with pytest.raises(ValueError):
        garageDict = {
        "capacity": 1,   # total number of spots
        "cars": {"Rat67": 15}         # car_id -> entry_hour (int)
        }
        enter_garage(garageDict, "Bugatti7", 13)

def test_enter_garage_valueError_if_carID_already_exists():
    with pytest.raises(ValueError):
        garageDict = {
        "capacity": 3,   # total number of spots
        "cars": {"Rat67": 15}         # car_id -> entry_hour (int)
        }
        enter_garage(garageDict, "Rat67", 18)