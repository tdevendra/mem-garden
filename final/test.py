import re
import memory_profiler
import time
import sys

d = {}
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

print("Prof Memory before {} Mb".format(memory_profiler.memory_usage()))
print("Memory before {} Mb".format(sys.getsizeof(d)))
t1 = time.clock()   
with open('testin.txt') as f:
    for chunk in f:
        process_chunk(chunk)

t2 = time.clock()
        
for k, v in d.items():
    print ("Word: " + str(k) + " Count: " + str(v))

print("Memory after {} Mb".format(sys.getsizeof(d)))

print("Prof Memory after {} Mb".format(memory_profiler.memory_usage()))

