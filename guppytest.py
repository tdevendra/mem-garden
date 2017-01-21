import gc
from guppy import hpy

def wordcount():
    f = open('filenew.txt', 'r')

    d = {}
    for line in f:
        line = line.strip()
        word = line.split()[0]
        if word in d:
            d[word] = d[word] + 1
        else:
            d[word] = 0
    return d

wordcount()
gc.collect()
h = hpy()
print h.heap()
