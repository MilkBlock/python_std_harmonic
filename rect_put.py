from collections import namedtuple 
Rect = namedtuple("rect",["x","y","w","h","dir"])  # dir 0 1 2 3   其中0代表左下角 然后顺时针
w1 = input("w1")
h1 = input("h1")
w2 = input("w2")
h2 = input("h2")
q = []
def put(x,y,w,h,dir):
    q.append(r:=Rect(x,y,w,h,dir))
    return r
def deput():
    q.pop()

def add_size_to_coord(x,y,r:Rect):
    if dir==0:
        return x+r.w,y+r.h
    if dir==1:
        return x+r.h,y-r.w
    if dir==2:
        return x-r.w,y-r.h
    if dir==3:
        return x-r.h,y+r.w
def solve_edge(x,y,w,h):
    edge_rate =0
    edge_sum =0
    x1,y1=x,y
    x2,y2=x,y
    for i in range(4):
        r1 = put(x1,y1,w1,h1,0)
        x1,y1 = add_size_to_coord(x1,y1,r1)
        deput()

solve_edge(0,0,input("w"),input("h"))