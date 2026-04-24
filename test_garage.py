from garage import enter_garage, exit_garage, get_available_spots, calculate_fee
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

def test_enter_garage_typeError_if_entryHour_notInt():
    with pytest.raises(TypeError):
        garageDict = {
        "capacity": 10,   # total number of spots
        "cars": {}         # car_id -> entry_hour (int)
        }
        enter_garage(garageDict, "Rat67", "18.0")

def test_exit_garage_works():
    garageDict = {
        "capacity": 3,   # total number of spots
        "cars": {"Rat67": 15}         # car_id -> entry_hour (int)
        }
    exit_garage(garageDict, "Rat67")
    assert "Rat67" not in garageDict["cars"].keys()

def test_exit_garage_keyError_if_carId_not_in_garage():
    with pytest.raises(KeyError):
        garageDict = {
        "capacity": 10,   # total number of spots
        "cars": {"Rat67": 15}         # car_id -> entry_hour (int)
        }
        exit_garage(garageDict, "Rat")

def test_get_available_spots_works():
    garageDict = {
        "capacity": 10,   # total number of spots
        "cars": {"Rat67": 15}         # car_id -> entry_hour (int)
        }
    assert get_available_spots(garageDict) == 9

def test_get_available_spots_is_full():
    garageDict = {
        "capacity": 1,   # total number of spots
        "cars": {"Rat67": 15}         # car_id -> entry_hour (int)
        }
    assert get_available_spots(garageDict) == 0

# def test_calculate_fee_works():
#     assert calculate_fee(3, 2) == 6.00

@pytest.mark.parametrize("hours, rate, expected", [(3, 2, 6.00), (8, 2.5, 20.00), (5.5, 2, 11.00)])
def test_calculate_fee_works(hours, rate, expected):
    assert calculate_fee(hours, rate) == expected

@pytest.mark.parametrize("hours, rate", [(-3, 2), (4, -2)])
def test_calcuate_fee_valueError_if_negative_input():
    with pytest.raises(ValueError):
        calculate_fee(hours, rate)

