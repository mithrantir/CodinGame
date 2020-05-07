
b = {"1": "@", "0": "."}
rules_id = ["@@@", "@@.", "@.@", "@..", ".@@", ".@.", "..@", "..."]


def next(pattern):
    pattern_exp, new_pattern = [pattern[-1]] + [c for c in pattern] + [pattern[0]], []
    for i in range(1, len(pattern)+1):
        local = pattern_exp[i-1] + pattern_exp[i] + pattern_exp[i+1]
        new_pattern.append(rule[rules_id.index(local)])
    return "".join(c for c in new_pattern)


r = str(bin(int(input())))[2:]
while len(r) < 8:
    r = "0" + r
rule = [b[c] for c in r]

n = int(input())
pattern = input()
for i in range(n):
    print(pattern)
    pattern = next(pattern)
