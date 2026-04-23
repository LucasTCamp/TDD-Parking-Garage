def enter_garage(garage, car_id, entry_hour):
    if not isinstance(entry_hour, (int)):
        raise TypeError("Time must be an integer")
    if car_id in garage["cars"].keys():
        raise ValueError("Car already in garage")
    if len(garage["cars"]) >= garage["capacity"]:
        raise ValueError("Garage is full")
    garage["cars"][car_id] = entry_hour

def exit_garage(garage, car_id):
    if car_id not in garage["cars"].keys():
        raise KeyError("This car doesn't exist in garage")
    garage["cars"].pop(car_id)


def get_available_spots(garage):
    return garage["capacity"] - len(garage["cars"])

def calculate_fee(hours, rate):
    return 6