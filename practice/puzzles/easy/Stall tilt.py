import sys
import math


def best_speed(radius):
    return int(math.floor((radius*9.81*3**(1/2))**(1/2)))


n = int(input())
v = int(input())
driver_speed = {}
driver = [chr(ord('a')+i) for i in range(n)]
for i in range(n):
    speed = int(input())
    driver_speed[chr(ord('a')+i)] = speed

min_radius = 200
bends = []
for i in range(v):
    bends.append(int(input()))
    if bends[i] < min_radius:
        min_radius = bends[i]

opt_speed = best_speed(min_radius)
print(opt_speed)
print('y')


def value_of_driver(c):
    if driver_speed[c] <= opt_speed:
        return driver_speed[c]
    else:
        value = -v
        for r in bends:
            if driver_speed[c] > best_speed(r):
                return value*100+driver_speed[c]
            else:
                value += 1
    return 0


driver.sort(key=value_of_driver, reverse=True)
for d in driver:
    print(d)
