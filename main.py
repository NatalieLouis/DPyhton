from collections import OrderedDict


class OrderedClass(type):
    @classmethod
    def __prepare__(cls, name, bases):
        return OrderedDict()

    def __new__(cls, name, bases, attrs):
        attrs['__ordered__'] = attrs.copy()
        return super().__new__(cls, name, bases, attrs)


class C(metaclass=OrderedClass):
    z = 1
    a = 2
    def method(self): pass


for attr in C.__ordered__:
    if not attr.endswith('__'):
        print(attr, end=' ')
