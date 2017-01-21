import timeit

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
    return

t = timeit.Timer(wordcount)
print(t.timeit(number=1))
