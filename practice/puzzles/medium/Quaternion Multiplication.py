import re


def multiplicate(q1, q2):
    res = [0, 0, 0, 0]
    res[0] = q1[1] * q2[2] - q1[2] * q2[1] + q1[0] * q2[3] + q1[3] * q2[0]
    res[1] = q1[2] * q2[0] - q1[0] * q2[2] + q1[1] * q2[3] + q1[3] * q2[1]
    res[2] = q1[0] * q2[1] - q1[1] * q2[0] + q1[2] * q2[3] + q1[3] * q2[2]
    res[3] = -q1[0] * q2[0] - q1[1] * q2[1] - q1[2] * q2[2] + q1[3] * q2[3]
    return res


def read_quartenion(q):
    if 'i' not in q:
        q = "0i" + q
    if 'j' not in q:
        ind = q.index('i')
        q = q[:ind+1] + "0j" + q[ind+1:]
    if 'k' not in q:
        ind = q.index('j')
        q = q[:ind+1] + "0k" + q[ind+1:]

    coef_list = list(re.findall(r'(.*)[i](.*)[j](.*)[k](.*)', q)[0])
    coefficient = []
    for i in range(3):
        if len(coef_list[i]) == 0:
            coefficient.append(1)
        elif len(coef_list[i]) == 1 and coef_list[i] == '+':
            coefficient.append(1)
        elif len(coef_list[i]) == 1 and coef_list[i] == '-':
            coefficient.append(-1)
        else:
            coefficient.append(int(coef_list[i]))
    if len(coef_list[3]) == 0:
        coefficient.append(0)
    else:
        coefficient.append(int(coef_list[3]))
    return coefficient


def print_version(q):
    s = "+" + str(q[0]) + "i+" + str(q[1]) + "j+" + str(q[2]) + "k+" + str(q[3])
    s = re.sub(r'\+0i', "", s)
    s = re.sub(r'\+0j', "", s)
    s = re.sub(r'\+0k', "", s)
    s = re.sub(r'\+0', "", s)
    s = re.sub(r'\+1i', "+i", s)
    s = re.sub(r'\+1j', "+j", s)
    s = re.sub(r'\+1k', "+k", s)
    s = re.sub(r'-1i', "-i", s)
    s = re.sub(r'-1j', "-j", s)
    s = re.sub(r'-1k', "-k", s)
    s = re.sub(r'\+\-', "-", s)
    if len(s) == 0:
        s = "0"
    if s[0] == '+':
        s = s[1:]
    return s


expr = input()
product = re.findall(r'\(([+-0123456789ijk]+)\)', expr)
result = [0, 0, 0, 1]
for q in product:
    result = multiplicate(result, read_quartenion(q))
print(print_version(result))
