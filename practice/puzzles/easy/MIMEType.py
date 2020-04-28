import sys
import math

associate = {}

n = int(input())  # Number of elements which make up the association table.
q = int(input())  # Number Q of file names to be analyzed.
for i in range(n):
    # ext: file extension
    # mt: MIME type.
    ext, mt = input().split()
    ext = ext.lower()
    associate[ext] = mt

for i in range(q):
    fname = input()  # One file name per line.
    extension = ""
    for i in range(len(fname)):
        if fname[i] == '.':
            extension = fname[i + 1:]
    extension = extension.lower()
    if extension in associate:
        print(associate[extension])
    else:
        print("UNKNOWN")
