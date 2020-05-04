
def add_keys(k1, k2):
    k = ""
    for i in range(4):
        if k1[i] == k2[i] == '0':
            k += '0'
        else:
            k += 'X'
    return k


l = int(input())
n = int(input())
map_of = ["0000" for i in range(l+1)]
for i in range(n):
    pattern, tempo = input().split()
    tempo = int(tempo)
    for j in range(0,l+1,tempo):
        map_of[j] = add_keys(map_of[j], pattern)

for k in range(l,0,-1):
    print(map_of[k])
