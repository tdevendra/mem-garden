import sys
import re
import gc
from guppy import hpy

# Measure performance using heap from guppy
h = hpy()

def update_word_count(word, line):
    """
    Update word count in stored values string
    """
    if re.search(word + '=', line) is not None:
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
    Count and map word occurence in file
    """
    f = open(filename, 'r')

    d = {}
    for line in f.readlines():
        line = line.strip()
        word = line.split()[0]
        # Get first letter of string and index 
        # dictionary using letter
        letter = word[0]
        if letter in d:
            count_str = d[letter]
            # Update count for word by replacing word=count
            # in stored string format
            newcountline = update_word_count(word, count_str)
            d[letter] = newcountline 
        else:
            d[letter] = word + '=1;'
    return d

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python wordgroup.py <file>")
        exit(-1)

    h.setref()
    res = wordcount(sys.argv[1])
    print "Data Structure res (Size in bytes):"
    print sys.getsizeof(res)
    counts = []
    for l in res:
        wordncounts = res[l].split(';')
        counts.extend(wordncounts)
    print "Data Structure counts (Size in bytes):"
    print sys.getsizeof(counts)
    print ""
    print "Words and their occurence counts"
    for c in counts:
        if c != '':
            print c

    # Print memory usage details
    print ""
    print "Program memory usage details:"
    print h.heap()
