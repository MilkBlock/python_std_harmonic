import sys,os
sys.path.append("./taichi_harmonic/")
print(__file__)
import taichi_harmonic.path_test_child as ptc

ptc.c.put("a")
print(ptc.c.get())

