import re
from guppy import hpy

d = {}
def read_in_chunks(f, size=1024):
    while True:
        chunk = f.read(size * 10)
        if not chunk:
            break
        yield chunk
    print("Out of while loop")

def calc_words(word):
    word = word.lower()
    if re.search("[A-Za-z0-9]+", word):
        pass
    else:
        return

    if word in d:
        d[word] = d[word] + 1
    else:
        d[word] = 1

def process_chunk(data):
    print("In process chunk")
    lines = data.split("\n")
    for line in lines:
        words = line.split()
        words = map(lambda y: y.strip(), words)        
        words = map(calc_words, words)

h = hpy()
h.setref()
with open('testin.txt') as f:
    for chunk in read_in_chunks(f):
        process_chunk(chunk)

for k, v in sorted(d.iteritems(), key=lambda (k, v): (v, k), reverse=True):
    print "Word: " + str(k) + " Count: " + str(v)

print h.heap()
