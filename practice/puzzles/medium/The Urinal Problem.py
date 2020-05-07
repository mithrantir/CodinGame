
n = int(input())
b = input()
urinal_pos = []
for i in range(n):
    if b[i] == '!':
        urinal_pos.append(i)

maxdist, index = urinal_pos[0], 0
for i in range(1, len(urinal_pos)):
    dist = (urinal_pos[i] - urinal_pos[i-1])//2
    if dist > maxdist:
        maxdist, index = dist, urinal_pos[i-1] + dist
if n - urinal_pos[-1] > maxdist:
    index = n-1

print(index)
