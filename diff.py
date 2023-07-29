import subprocess as sp
r1 = sp.run('env',shell=True,text=True,capture_output=True)
r2 = sp.run('env',shell=False,text=True,capture_output=True)
import difflib
m=[]
m.append(r1.stdout.splitlines(keepends=True))
m.append(r2.stdout.splitlines(keepends=True))
diff= difflib.ndiff(*m)
print(''.join(diff))

