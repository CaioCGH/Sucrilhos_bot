#!/usr/bin/python
from subprocess import Popen
import sys
from datetime import datetime


filename = sys.argv[1]
while True:
    print(str(datetime.now()) + " Starting " + filename )
    p = Popen("python3 " + filename, shell=True)
    p.wait()