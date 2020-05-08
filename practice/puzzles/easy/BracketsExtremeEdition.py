open_brackets = {'(', '{', '['}
match = {'}': '{', ']': '[', ')': '('}

expression = input()
stack, valid = [], True
for c in expression:
    if c in open_brackets:
        stack.append(c)
    elif c in match and (len(stack) == 0 or match[c] != stack.pop()):
        valid = False
        break
if valid:
    valid = len(stack) == 0

print(str(valid).lower())
