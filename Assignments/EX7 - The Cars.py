class Vehicle():
    def __init__(self,
                manufacturer : str,
                pcapacity : int,
                max_speed : int,
                mileage : int = 0 ) -> None:
        self.manufacturer = manufacturer
        self.pcapacity = pcapacity
        self.max_speed = max_speed
        self.mileage = mileage

    def state(self) -> str:
        if self.mileage :
            return f"The car mileage is {self.mileage}"
        return "The car is new"

    def mileageset(self, new_mileage : int):
        """set a new mileage for vehicle"""
        self.mileage = new_mileage


class SUV(Vehicle):
    def __init__(self, manufacturer: str, pcapacity: int, max_speed: int, mileage: int = 0, wheeldrive : str = "AWD" ) -> None:
        """ wheeldrive should be one of the `2WD`, `4WD`, `AWD`"""
        super().__init__(manufacturer, pcapacity, max_speed, mileage)
        self.wheeldrive = wheeldrive
    def wdcount(self):
        wheels = {
            "AWD" : 4,
            "4WD" : 4,
            "2WD" : 2,
        }
        return f"{wheels[self.wheeldrive]} wheels"


class Truck(Vehicle):

    def __init__(self, manufacturer: str, pcapacity: int, max_speed: int, loadcapacity : int = 0, mileage: int = 0, ) -> None:
        super().__init__(manufacturer, pcapacity, max_speed, mileage)
        self.loadcapacity = loadcapacity

    def capacity(self) -> int:
        return f"capacity is: {self.loadcapacity}"
    

if __name__ == "__main__":

    Tiba2 = Vehicle("Saipa", 4, 190)
    print(Tiba2.state())
    Tiba2.mileageset(130)
    print(Tiba2.state())

    Terrain = SUV("GMC", 5, 180)
    print(Terrain.state())
    print(Terrain.wdcount())

    Sierra = Truck("GMC", 5, 200, 0, 3)
    print(Sierra.state())
    print(Sierra.capacity())
