
def next_term(n):
    temp = {'0': 4, '1': 3}
    return sum([temp[c] for c in str(bin(n))[2:]])


orbit = [[] for n in range(300)]
orbit[13].append(13)
orbit[18].append(18)

for n in range(300):
    if len(orbit[n]) > 0:
        continue
    m = n
    while len(orbit[m]) == 0:
        orbit[n].append(m)
        m = next_term(m)
    orbit[n] += orbit[m]

start, term = [int(i) for i in input().split()]
start, term = next_term(start), term - 1

if term >= len(orbit[start]):
    print(orbit[start][-1])
else:
    print(orbit[start][term])
