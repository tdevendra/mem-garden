import gc
from guppy import hpy

f = open('filenew.txt', 'r')

d = {}
h = hpy()
#h.setref()
for line in f:
   line = line.strip()
   word = line.split()[0]
   #h.setref()
   if word in d:
       d[word] = d[word] + 1
   else:
       d[word] = 0
   #print(d)
   #print h.heap()

h.setref()
z = {}
import sys
print(sys.getsizeof(d))
print d
z = list(d)
print z
print(sys.getsizeof(z))
#h.setref()
#gc.collect()
print h.heap()
