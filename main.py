from dataclasses import dataclass


@dataclass()
class Person:
    name: str
    age: int


p1 = Person("John", 30)
p2 = Person("John", 30)

print("hash", hash(p1))
print("hash", hash(p2))
print("eq", p1 == p2)
d = {p1: "p1", p2: "p2"}
print(d)
