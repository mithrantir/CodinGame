match_op = {'(': ')', '{': '}', '[': ']', '<': '>'}
match_cl = {')': '(', '}': '{', ']': '[', '>': '<'}

n = int(input())
for i in range(n):
    expression = input()
    stack, valid = [], True
    for c in expression:
        if c in match_op:
            if len(stack) > 0 and stack[-1] == c:
                stack.pop()
            else:
                stack.append(c)
        elif c in match_cl:
            if len(stack) > 0 and match_cl[c] == stack[-1]:
                stack.pop()
            else:
                stack.append(match_cl[c])
    valid = len(stack) == 0

    print(str(valid).lower())
