#!/usr/bin/python
import sys
import getopt
opts, args = getopt.getopt(sys.argv[1:],'n:', ["nb="] )

for opt,arg in opts:
    if opt in ["--nb"]:
        execution_time=int(arg)
        for i in range (0,execution_time):
             exec(open("validation.py").read())

    

        
        

