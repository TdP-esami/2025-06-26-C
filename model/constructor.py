from dataclasses import dataclass


@dataclass
class Constructor:
    constructorId: int
    constructorRef: str
    name: str
    nationality: str
    url: str
    results: map

    def __hash__(self):
        return self.constructorId

    def __eq__(self, other):
        return self.constructorId == other.constructorId

    def __str__(self):
        return self.name