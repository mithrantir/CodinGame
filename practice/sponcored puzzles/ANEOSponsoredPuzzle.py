import sys
import math

speed = int(input())
light_count = int(input())
lights = []
for i in range(light_count):
    distance, duration = [int(j) for j in input().split()]
    lights.append([distance,duration])

ans = 0
for sp in range(speed, 0, -1):
    isPossible = True
    for d, p in lights:
        k = math.ceil((18*d-5*p*sp)/(10*p*sp)+0.0001)
        if k*5*p*sp > 9*d:
            isPossible = False
            break
    if isPossible:
        ans = sp
        break

print(ans)
