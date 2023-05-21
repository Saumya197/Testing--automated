from subprocess import Popen
from os import listdir,system
from time import perf_counter as pcr
# file=listdir(".")[0]
# print(file)
# st=pcr()
# Popen(["python",f"payload/{file}"])
# print(pcr()-st)
system("python falana.py")