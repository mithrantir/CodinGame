
def from_str_to_time(s):
    times = [int(c) for c in s.split(':')]
    return times[0] * 3600 + times[1] * 60 + times[2]


n = int(input())
min_time, answer = 3600*25, ""
for i in range(n):
    t = input()
    t_int = from_str_to_time(t)
    if t_int < min_time:
        min_time, answer = t_int, t

print(answer)
