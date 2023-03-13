from dataclasses import dataclass

@dataclass(slots=True)
class Budget:
    amount: int
    category: int
    time: int
    limit: int = 0
    pk: int = 0
