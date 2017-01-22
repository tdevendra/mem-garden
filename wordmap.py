from __future__ import print_function

import re
import sys
from operator import add
from pyspark.sql import SparkSession

def wordcount(line):
    line = line.strip()
    word = line.split()[0]
    return (word, 1)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: wordmap <file>", file=sys.stderr)
        exit(-1)

    spark = SparkSession\
        .builder\
        .appName("WordMapping")\
        .getOrCreate()

    lines = spark.read.text(sys.argv[1]).rdd.map(lambda r: r[0])

    #print(lines.collect())
    #lines = lines[1:]
    result = lines.map(lambda line: wordcount(line)).reduceByKey(add)
    #print("Result")
    print(result.collect())
    spark.stop()
