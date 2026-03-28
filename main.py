import subprocess as sub
import os
import time
i=1
sub.run(["mkdir","tmp/c"] shell=True)
while True:
  print(i)
  i=i+1
