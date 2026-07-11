from power_source import PowerSource

class FuelTank(PowerSource):
    def consume(self, distance: float) -> float:
        fuel_consumed = distance / 10
        if self._level - fuel_consumed < 0:
            raise ValueError("해당 거리를 주행할 만큼의 연료가 부족함")
        self._level -= fuel_consumed
        return fuel_consumed
    
