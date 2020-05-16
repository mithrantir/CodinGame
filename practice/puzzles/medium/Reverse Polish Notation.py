
n = int(input())
stack, error = [], False
for instruction in input().split():
    if not instruction.isalpha():
        stack.append(int(instruction))
    elif instruction == 'ADD':
        if len(stack) < 2:
            error, stack = True, []
            break
        else:
            a, b = stack.pop(), stack.pop()
            stack.append(a + b)
    elif instruction == 'SUB':
        if len(stack) < 2:
            error, stack = True, []
            break
        else:
            a, b = stack.pop(), stack.pop()
            stack.append(b - a)
    elif instruction == 'MUL':
        if len(stack) < 2:
            error, stack = True, []
            break
        else:
            a, b = stack.pop(), stack.pop()
            stack.append(a * b)
    elif instruction == 'DIV':
        if len(stack) < 2:
            error, stack = True, []
            break
        else:
            a = stack.pop()
            b = stack.pop()
            if a == 0:
                error = True
                break
            stack.append(b // a)
    elif instruction == 'MOD':
        if len(stack) < 2:
            error, stack = True, []
            break
        else:
            a, b = stack.pop(), stack.pop()
            if b == 0:
                error = True
                break
            stack.append(b % a)
    elif instruction == 'SWP':
        if len(stack) < 2:
            error, stack = True, []
            break
        else:
            a, b = stack.pop(), stack.pop()
            stack.append(a)
            stack.append(b)
    elif instruction == 'POP':
        if len(stack) < 1:
            error, stack = True, []
            break
        else:
            a = stack.pop()
    elif instruction == 'DUP':
        if len(stack) < 1:
            error = True
            break
        else:
            stack.append(stack[-1])
    elif instruction == 'ROL':
        if len(stack) < 3:
            error = True
            break
        else:
            pos = stack.pop()
            top = stack.pop(-pos)
            stack.append(top)
    else:
        error = True
        break

ans = ""
while len(stack) > 0:
    ans += str(stack.pop(0)) + " "

if error:
    ans += "ERROR"

print(ans.strip())
