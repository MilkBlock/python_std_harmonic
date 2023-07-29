import subprocess
import sys
# print(subprocess.check_output(['cd','..']))
# result= subprocess.check_output(['ls'],cwd="/usr",text=True)
result= subprocess.run(['env'],cwd="/usr/bin",env={"LANG":"zh_CN.utf8"},text=True,shell=True,capture_output=True)
# result= subprocess.run(['&& env'],text=True,shell=True,capture_output=True)
print(result)
# print(subprocess.check_output(['readlink .']))