from dataclasses import dataclass


@dataclass(eq=True, unsafe_hash=True)  # ✅ 强制生成 __hash__
class Person:
    name: str
    age: int


p1 = Person("John", 30)
p2 = Person("John", 30)

print("hash", hash(p1))  # ✅ 现在可以计算哈希值
print("hash", hash(p2))
print("eq", p1 == p2)

d = {p1: "p1", p2: "p2"}  # ✅ 但如果修改 p1.name 可能导致哈希问题
# p2.name = "Tom"
print("change", d[p2])
print(d)
