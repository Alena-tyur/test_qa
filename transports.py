from vehicle import Vehicle

class Car(Vehicle):
    def __init__(self, liters: int):
        self.fuel_consumption_per_100km = liters
        self._current_fuel = 0
      
    def fill_up(self, liters: int):
        self._current_fuel += liters

    def drive(self, distance: float):
        fuel_consumption_for_distance = distance / 100 * self.fuel_consumption_per_100km
        if fuel_consumption_for_distance > self._current_fuel:
            raise ValueError("Недостаточно топлива")
        self._current_fuel -= fuel_consumption_for_distance

    def remaining_fuel(self) -> float:
        return self._current_fuel
  
  
class Track(Vehicle):
    def __init__(self, liters: int, trailers: int = 1):
        self.fuel_consumption_per_100km = liters
        self.trailers = trailers
        self._current_fuel = 0
      
    def fill_up(self, liters: int):
        self._current_fuel += liters

    def drive(self, distance: float):
        fuel_consumption_for_distance = distance / 100 * self.fuel_consumption_per_100km * self.trailers
        if fuel_consumption_for_distance > self._current_fuel:
            raise ValueError("Недостаточно топлива")
        self._current_fuel -= fuel_consumption_for_distance

    def remaining_fuel(self) -> float:
        return self._current_fuel