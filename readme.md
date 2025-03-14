# dataclass 
## 字段定义
- 如果 Person 是不可变的，可以用 frozen=True，这样 Python 会自动生成 __hash__
- 如果你想让 Person 仍然是可变的，但又能用作字典键，可以用 unsafe_hash=True
如果你手动定义了 __eq__，Python 默认会禁用 __hash__，你可以用 unsafe_hash=True 让 __hash__ 仍然可用。
因为 dataclass 继承自 object，而 object.__hash__() 返回的是默认的对象 ID，而不是基于 name 和 age 计算的哈希值。
在 Python 中，默认的 object.__hash__() 返回的是对象的内存地址，类似于 id(self)
默认情况下，如果 eq=True，而 frozen=False，Python 不会自动生成 __hash__，因为对象是可变的，哈希值不稳定。
unsafe_hash=True强制 生成 __hash__，即使类是可变的，但这样做可能导致哈希问题（对象变了但 __hash__ 不变）。

# 单例模式
```python
class Singleton(type):
    _instances = {}
    _lock = threading.Lock()

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            with cls._lock:
                if cls not in cls._instances:  # Double-checked locking
                    cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]

class Config(metaclass=Singleton):
    def __init__(self, value):
        self.value = value
```