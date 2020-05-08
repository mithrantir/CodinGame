n = int(input())
program = []
for i in range(n):
    program.append([c for c in input()])

x, y, exit_p, stack, con_out, dr, string_mode = 0, 0, False, [], "", 0, False
d = [[0, 1], [1, 0], [0, -1], [-1, 0]]

while not exit_p:
    c = program[x][y]
    if c == '"':
        string_mode = not string_mode
    elif string_mode:
        stack.append(ord(c))
    elif c == ' ':
        pass
    elif c == 'E':
        exit_p = True
    elif c == '>':
        dr = 0
    elif c == '<':
        dr = 2
    elif c == '^':
        dr = 3
    elif c == 'v':
        dr = 1
    elif c == 'S':
        x, y = x + d[dr][0], y + d[dr][1]
    elif c.isdigit():
        stack.append(int(c))
    elif c == '+':
        b, a = stack.pop(), stack.pop()
        stack.append(a + b)
    elif c == '-':
        b, a = stack.pop(), stack.pop()
        stack.append(a - b)
    elif c == '*':
        b, a = stack.pop(), stack.pop()
        stack.append(a * b)
    elif c == 'P':
        stack.pop()
    elif c == 'X':
        b = stack.pop()
        a = stack.pop()
        stack.append(b)
        stack.append(a)
    elif c == 'D':
        stack.append(stack[-1])
    elif c == '_':
        if stack.pop() == 0:
            dr = 0
        else:
            dr = 2
    elif c == '|':
        if stack.pop() == 0:
            dr = 1
        else:
            dr = 3
    elif c == 'I':
        con_out += str(stack.pop())
    elif c == 'C':
        con_out += str(chr(stack.pop()))

    x, y = x + d[dr][0], y + d[dr][1]

print(con_out)
