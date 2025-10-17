from dataclasses import dataclass


class NotFoundExaception(Exception):
    pass


@dataclass
class Item:
    id: int
    name: str

    def is_name_valid(self) -> bool:
        return "@" in self.name


class ShoppingCart:
    def __init__(self, items: list[Item]):
        self.items: list[Item] = items

    def get_items(self) -> list[Item] | None:
        return self.items

    def get_item(self, id: int) -> Item:
        try:
            item = next((item for item in self.items if item.id == id), None)

            if not item:
                raise NotFoundExaception(f"Id {id} not found in the list")

            return item
        except NotFoundExaception as error:
            print(error)  # or raise error

    def search(self, name: str) -> list[Item]:
        return [
            item for item in self.items if item.name.lower().startswith(name.lower())
        ]

    def get_items_name(self) -> list[str]:
        return [item.name for item in self.items]

    def remove_item(self, id: int):
        # for index, item in enumerate(self.items):
        #     if item.id == id:
        #         self.items.pop(index)
        self.items = [item for item in self.items if item.id != id]
        return self.items


basket: list[Item] = [Item(1, "Shampoo"), Item(2, "Amaciante"), Item(3, "Sabão")]
my_cart: ShoppingCart = ShoppingCart(basket)

print("all items:")
print(my_cart.get_items())

print("item:")
item = my_cart.get_item(1)
print(item)

print("search_result:")
search_result = my_cart.search("S")
print(search_result)

print("names:")
print(my_cart.get_items_name())

print("delete:")
print(my_cart.items)
print(my_cart.remove_item(1))
# exception
# item = my_cart.get_item(99)
