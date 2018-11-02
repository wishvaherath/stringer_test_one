#!/usr/bin/env python
import sys
x = 0
for line in open(sys.argv[1].strip()):
    x = x + int(line.strip())


f = open(sys.argv[2].strip(),"w")
f.write(str(x) + "\n")

f.close()
