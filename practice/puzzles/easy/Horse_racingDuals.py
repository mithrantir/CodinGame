import sys
import math

n = int(input())
pi = []
for i in range(n):
    pi.append(int(input()))

spi = sorted(pi)
diff = [abs(spi[i] - spi[i + 1]) for i in range(n - 1)]

# Write an answer using print
# To debug: print("Debug messages...", file=sys.stderr)

print(min(diff))