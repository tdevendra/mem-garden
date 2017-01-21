import timeit

@profile
def wordcount():
    f = open('file.txt', 'r')

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
