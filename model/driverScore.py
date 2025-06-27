from dataclasses import dataclass


@dataclass
class DriverScore:
    driverId: int
    position: int
    circuitId: int

    def __hash__(self):
        return hash((self.driverId, self.position, self.points, self.time))

    def __eq__(self, other):
        return (self.driverId == other.driverId
                and self.position == other.position
                and self.circuitId == other.circuitId)