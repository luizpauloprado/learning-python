# data classes
from dataclasses import dataclass
from typing import Any


@dataclass
class Product:
    name: str
    description: str
    count: int = 0
    price: float = 0.0
    etc: Any | None = None

    def description_is_valid(self) -> bool:
        return "@" in self.description


item1: Product = Product(name="Item 1", description="@ example")
print(item1)
print("description_is_valid:")
print(item1.description_is_valid())
