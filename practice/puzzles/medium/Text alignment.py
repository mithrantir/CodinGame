import math

def allign(i, text):
    switcher={
        "LEFT": left,
        "RIGHT": right,
        "CENTER": center,
        "JUSTIFY": justify
        }
    func=switcher.get(i,lambda :'invalid command')
    return func(text)

def left(text):
    print_text(text)
    return

def right(text):
    rtext = []
    for line in text:
        rtext.append("".join(' ' for c in range(maxlen-len(line)))+line)
    print_text(rtext)
    return

def center(text):
    ctext = []
    for line in text:
        ctext.append("".join(' ' for c in range((maxlen-len(line)+1)//2))+line)
    print_text(ctext)
    return

def justify(text):
    jtext = []
    for line in text:
        words = line.split()
        if len(words) == 1:
            jtext.append(line)
        else:
            jline = words[0]
            blanks = maxlen - len(line) + len(words) - 1
            postions = len(words) - 1
            for i in range(1,len(words)):
                nspaces = int(math.floor(i*blanks/postions)-math.floor((i-1)*blanks/postions))
                jline += "".join(' ' for j in range(nspaces)) + words[i]
            jtext.append(jline)
    print_text(jtext)
    return

def print_text(text):
    for line in text:
        print(line)
    return

alignment = input()
n = int(input())
text, maxlen = [], 0
for i in range(n):
    text.append(input())
    maxlen = max(maxlen, len(text[i]))

allign(alignment, text)
