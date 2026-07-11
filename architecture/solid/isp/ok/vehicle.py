from power_source import PowerSource
from fuel_tank import FuelTank
from battery import Battery

class Vehicle:

    def __init__(self, power_source: PowerSource):
        self._power_source = power_source

    def power_level(self) -> float:
        return self._power_source.level()
    
    def drive(self, distance: float) -> float:
        return self._power_source.consume(distance)
    
def drive_vehicle(vehicle: Vehicle, distance: float) -> None:
    try:
        energy_consumed = vehicle.drive(distance)
        print(f"소비된 에너지: {energy_consumed:.2f} 단위")

    except ValueError as e:
        print(f"여행 완료 불가: {e}")

fuel_car = Vehicle(FuelTank(50))
drive_vehicle(fuel_car, 100)

electric_car = Vehicle(Battery(50))
drive_vehicle(electric_car, 100)
