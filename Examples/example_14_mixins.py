"""
Scratch file for testing concepts
"""
class AsDictMixin:
    def as_dict(self):
        dict_ = {}
        vars_ = vars(self)
        for name, value in vars_.items():
            if not name.startswith('_'):
                dict_[name] = value
        return dict_


class Bike(AsDictMixin):
    def __init__(self):
        self.a = 1
        self.b = 2
        self._c = 3


class User(AsDictMixin):
    def __init__(self):
        self.d = 1
        self.e = 2
        self._f = 3


b = Bike()
print(b.as_dict())

u = User()
print(u.as_dict())