
r, minn, maxn, cheat = int(input()), 1, 100, -1
for i in range(1, r+1):
    line = input().split()
    num = int(line[0])
    if line[2] == 'low':
        if num >= maxn:
            cheat = i
            break
        minn = max(minn, num + 1)
    elif line[2] == 'high':
        if num <= minn:
            cheat = i
            break
        maxn = min(maxn, num - 1)
    else:
        if minn <= num <= maxn:
            minn, maxn = num, num
        else:
            cheat = i
            break
    if minn > maxn:
        cheat = i
        break

if cheat < 0:
    print("No evidence of cheating")
else:
    print("Alice cheated in round {}".format(cheat))
