from math import *
from typing import Any

class Graphic:
    def __init__(self):
        print("father init")
        self.is_graphic = True
    def up():
        print("up")

class Cone(Graphic):
    __val = 3 

    def __str__(self) -> str:
        return "fuck you "
    def __init__(self,m):
        # super().__init__()
        super().__init__()
        self.__val = m
        print("init")
    def __call__(self, *args: Any, **kwds: Any) -> Any:
        print("call function is executed")
    def __eq__(self, __value: object) -> bool:
        return self.__val == __value 
    @staticmethod
    def get_name():
        print("this is a cone class ")
    def up(self):
        print("up son")
    
c:Cone= Cone(3)
c.up()
# print(Cone.get_name())
# print(Cone.up())
# print(c == 3)
# print(c == 2)
