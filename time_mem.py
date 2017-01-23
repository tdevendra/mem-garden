import timeit

t = timeit.Timer(stmt="wordcount('10MFile.txt')", setup="from wordgroup import wordcount")
print t.timeit(1)
