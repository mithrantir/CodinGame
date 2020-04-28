import sys
import math


# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

def evaluate(exp):
    br = []
    for c in exp:
        if c == '[' or c == '(' or c == '{':
            br.append(c)
        elif c == '}':
            if len(br) > 0 and br[-1] == '{':
                br.pop()
            else:
                return False
        elif c == ']':
            if len(br) > 0 and br[-1] == '[':
                br.pop()
            else:
                return False
        elif c == ')':
            if len(br) > 0 and br[-1] == '(':
                br.pop()
            else:
                return False

    if len(br) == 0:
        return True
    else:
        return False


expression = input()

# Write an answer using print
# To debug: print("Debug messages...", file=sys.stderr)

if evaluate(expression):
    print("true")
else:
    print("false")
