class CustomDict(dict):
    def __setitem__(self, key, value):
        if not all(char == '_' or char.isdigit() or char.islower() for char in key):
            raise TypeError(f'Name {key} must only be lowercase with numbers or underscore')
        super().__setitem__(key, value)


class NoCamelHumpMeta(type):
    @classmethod
    def __prepare__(cls, name, bases):
        return CustomDict()


class C(metaclass=NoCamelHumpMeta):
    def _came(self): pass
