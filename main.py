from dataclasses import dataclass


@dataclass(frozen=True, eq=False)
class Person:
    name: str
    age: int

    def __hash__(self):
        return 1


p1 = Person("John", 30)
p2 = Person("John", 30)

print("hash", hash(p1))
print("hash", hash(p2))
print("eq", p1 == p2)
d = {p1: "p1", p2: "p2"}
print(d)
