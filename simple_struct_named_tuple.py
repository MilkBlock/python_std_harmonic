from collections import namedtuple
Point = namedtuple("Point",['x','y'])
p = Point(1,2)
print(p)
print(p.x)
print(p.y)

class DataSet():
    def __init__(self) -> None:
        self._c = 3
    @property
    def c(self):
        print("get c")
        return self._c
    @c.setter
    def c(self,value):
        print("set c")
        self._c = value
    @c.deleter
    def c(self):
        print("delete c")

a =DataSet()
property()
print(a.c)
a.c = 4
print(a.c)
