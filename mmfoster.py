from hurry.filesize import size
import os, sys

def mmfile(filename, dump, size):
    """
    Create a file of certain size
    """
    f = open(filename, 'w')
    rd = open(dump, 'r')
    dump = rd.read()
    filesize = 0
    while(filesize < size):
        f.write(dump)
        filesize = os.path.getsize(filename)
    return filesize

if __name__ == '__main__':
    if len(sys.argv) != 4:
        print("Usage: mmfoster <dumpdatafile> <outfile> <size>")
        exit(-1)
    dumpfile = sys.argv[1]
    filename = sys.argv[2]
    filesize = int(sys.argv[3])
    dumpdata = "Hi hello bye 123 xyz"
    size = mmfile(filename, dumpfile, filesize)
    print("Created file of size", size)
