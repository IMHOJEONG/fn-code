# 잘못된 코드
class Vehicle:
    def __init__(self, fuel_capacity: float):
        self._fuel_capacity = fuel_capacity;
        self._fuel_level = fuel_capacity;

    def fuel_level(self) -> float:
        return self._fuel_level
    
    def consume_fuel(self, distance: float) -> None:

        fuel_consumed = distance / 10

        if self._fuel_level - fuel_consumed < 0:
            raise ValueError("거리를 이동하기에 충분한 연료가 없음");

        self._fuel_level -= fuel_consumed

class ElectricCar(Vehicle):
    def __init__(self, battery_capacity: float):
        super().__init__(battery_capacity)

    def consume_fuel(self, distance: float) -> None:
        energy_consumed = distance / 5
        if self._fuel_level - energy_consumed < 0:
            raise ValueError("해당 거리를 주행할 만큼의 전력이 부족함")
    
        self._fuel_level -= energy_consumed

# 예시
def drive_vehicle(vehicle: Vehicle, distance: float) -> None:
    initial_fuel = vehicle.fuel_level()
    vehicle.consume_fuel(distance)
    fuel_consumed = initial_fuel - vehicle.fuel_level()
    print(f"연료 소모량: {fuel_consumed:.2f} 리터")

# 호출부
car = Vehicle(50)
drive_vehicle(car, 100)

# 호출 에러 케이스 
electric_car = ElectricCar(50)
drive_vehicle(electric_car, 100)