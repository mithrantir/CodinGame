
def reverse_possible(s):
    if len(s) % 2 == 1:
        return False
    for i in range(1, len(s)-2, 2):
        if s[i] == s[i+2]:
            return False
    return True


def step_back(s):
    sn = ""
    while len(s) > 0:
        sn += int(s[0]) * s[1]
        s = s[2:]
    return sn


s = input()
while reverse_possible(s):
    sn = step_back(s)
    if sn == s:
        break
    else:
        s = sn
print(s)
