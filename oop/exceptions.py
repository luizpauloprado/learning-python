class MyException(Exception):
    pass


class User:
    def __init__(self, name: str):
        self.name: str = name
        self.complements: list[str] = []

    def get_name(self) -> str:
        return self.name

    def add_complement(self, complement: str):
        try:
            if "@" in complement:
                raise MyException("@ not allowed in complements")
            if complement in self.complements:
                raise ValueError("Complement alrady in complements list")

            self.complements.append(complement.lower())
        except (ValueError, TypeError) as error:
            print(error)
        except MyException as my_error:
            print(my_error)
        finally:
            print("Execution finished")


benji: User = User("Benji")
print(benji.get_name())

benji.add_complement("cute")
benji.add_complement("loveable")
print("complements list:")
print(benji.complements)

benji.add_complement("cute")
benji.add_complement("@cute")
