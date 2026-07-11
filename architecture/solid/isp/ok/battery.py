from power_source import PowerSource

class Battery(PowerSource):
    def consume(self, distance: float) -> float:

        energy_consumed = distance / 5;
        if self._level - energy_consumed < 0:
            raise ValueError("해당 거리를 주행할 만큼의 충전량이 부족")
        
        self._level -= energy_consumed
        return energy_consumed
    
