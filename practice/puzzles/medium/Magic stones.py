
stone = [0 for c in range(100)]
n = int(input())
for i in input().split():
    stone[int(i)] += 1

for i in range(99):
    stone[i+1] += stone[i] // 2
    stone[i] = stone[i] % 2

print(sum(stone))
