import sys
import re
import gc
from guppy import hpy
import pdb

h = hpy()
#h.setref()

def updatecount(word, line):
    """
    Update word count in stored values string
    """
    if re.search(word, line) is not None:
        m = re.search(word + "\=(\d+)\;", line)
        oldval = m.group(1)
        newval = int(oldval) + 1
        wordbefore = word + '=' + oldval
        wordafter = word + '=' + str(newval)
        line = re.sub(wordbefore, wordafter, line)
    else:
        line = line + word + '=1;'
    return line

def wordcount(filename):
    """
    Count and map word occurence
    """
    f = open(filename, 'r')

    d = {}
    for line in f.readlines():
        line = line.strip()
        word = line.split()[0]
        letter = word[0]
        if letter in d:
            countline = d[letter]
            newcountline = updatecount(word, countline)
            d[letter] = newcountline 
        else:
            d[letter] = word + '=1;'
    return d

if len(sys.argv) != 2:
    print("Usage: python wordgroup.py <file>")
    exit(-1)

res = wordcount(sys.argv[1])
print sys.getsizeof(res)
for l in res:
    print res[l].split(';')
print h.heap()
