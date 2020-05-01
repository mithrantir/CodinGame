import sys
import math

m = int(input())
n60_meas, n08_meas = [], []
pr = 0
for i in range(m):
    line = input().split()
    meas = [int(c) for c in line]
    n60_meas.append(10+(sum(meas)-40)/7)
    if i%2 == 0:
        for j in range(0,13,2):
            n08_meas.append(meas[j]+meas[j+1]+5)
        pr = meas[14]
    else:
        n08_meas.append(pr+meas[0]+5)
        for j in range(1,15,2):
            n08_meas.append(meas[j]+meas[j+1]+5)
        pr = 0

temp = sum(n60_meas)/len(n60_meas)
print("{:0.1f}".format(temp))
if 5 <= temp <= 30:
    print("{:0.1f}".format(sum(n08_meas)/len(n08_meas)))
