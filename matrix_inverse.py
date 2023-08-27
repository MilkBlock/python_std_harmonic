# import sympy as sy
# from sympy.abc import *
# ma =sy.Matrix([
#     [2,1,-1,1],
#     [0,3,1,0],
#     [45,3,2,1],
#     [6,6,1,3],
# ])
# eq1 = sy.Eq(3*x+2*x+5**2*x**2,y)
# eq2 = sy.Eq(y,30)
# sol = sy.solve((eq1,eq2))
# print(sol[0][x])

# a = "abcdef"
# print
# import re
# print(re.sub("[ab|de]","",a))
# import re
# with open("data.txt","r",encoding="utf-8") as f :
#     s =  f.read()
#     # print(s)
#     print(re.sub("([。，\n])",lambda a: str(a.group())+"sdfjosdf",s))
# a = re.match("s","sss")
# print(a.groups())
# print(a.group(0))
# print(a.group(1))
# print(a.group(2))
# print(a.group(3))
# print(a.groupdict())
# import re
# def func(match:re.Match):
#     print(match.groupdict())
#     print(match.groups())
#     print(match.group())
#     return match.group()

# with open("data.txt","r",encoding="utf-8") as f :
#     s =  f.read()
#     # print(s)
#     print(re.sub("([。，\n])",func,s))
# a = re.match("s","sss")



from sympy import Matrix
from sympy.abc import *
from sympy import *
t : Matrix  = Matrix([theta,phi,r])
s : Matrix  = Matrix([r*sin(theta)*cos(phi),r*sin(theta)*sin(phi),r*cos(theta)])
print(s.jacobian(t).det().simplify())