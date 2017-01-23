from hurry.filesize import size
import os, sys

def mmfile(filename, dump, size):
    """
    Create a file of certain size
    """
    f = open(filename, 'w')
    filesize = 0
    while(filesize < size):
        f.write(dump)
        filesize = os.path.getsize(filename)
    return filesize

if __name__ == '__main__':
    if len(sys.argv) != 3:
        print("Usage: foster <file> <size>")
        exit(-1)
    filename = sys.argv[1]
    filesize = int(sys.argv[2])
    dumpdata = "Hi hello bye 123 xyz"
    size = mmfile(filename, dumpdata, filesize)
    print("Created file of size", size)
