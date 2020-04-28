import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.
from typing import List

f = open("00000test.txt", 'r').read(-1).split('\n')
lon_str, lat_str = f[0].split(','), f[1].split(',')
# lon_str , lat_str = input().split(','), input().split(',')

lon = int(lon_str[0]) + int(lon_str[1])*10**-len(lon_str[1])
lat = int(lat_str[0]) + int(lat_str[1])*10**-len(lat_str[1])
lon, lat = lon * math.acos(-1) / 180, lat * math.acos(-1) / 180

n = int(f[2])
# n = int(input())

bestDist , answer = 999999999999.9, ""
for i in range(n):
    defib  = f[i+3].split(';')
    # defib = input().split(';')

    lonx_str, laty_str = defib[-2].split(','), defib[-1].split(',')
    lonx = int(lonx_str[0]) + int(lonx_str[1])*10**-len(lonx_str[1])
    laty = int(laty_str[0]) + int(laty_str[1])*10**-len(laty_str[1])
    lonx, laty = lonx * math.acos(-1) / 180, laty * math.acos(-1) / 180

    x = (lon - lonx) * math.cos((lon + lonx) / 2.)
    y = lat-laty
    dist = math.sqrt(x * x + y * y) * 6371.0
    if dist < bestDist:
        bestDist, answer = dist, defib[1]

# Write an answer using print
# To debug: print("Debug messages...", file=sys.stderr)

print(answer)
