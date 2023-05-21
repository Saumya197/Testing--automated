from subprocess import Popen
from os import listdir
from time import perf_counter as pcr
file=listdir(".")[0]
st=pcr()
Popen(["python",f"payload/{file}"])
print(pcr()-st)
