layer = {'D': 1, 'U': 1, 'L': 1, 'R': 1}

order = input()
side = input()

for c in order:
    if c == 'D':
        layer['U'], layer['D'] = layer['U'] + layer['D'], 1
        layer['L'], layer['R'] = 2 * layer['L'], 2 * layer['R']
    elif c == 'U':
        layer['D'], layer['U'] = layer['D'] + layer['U'], 1
        layer['L'], layer['R'] = 2 * layer['L'], 2 * layer['R']
    elif c == 'L':
        layer['R'], layer['L'] = layer['R'] + layer['L'], 1
        layer['U'], layer['D'] = 2 * layer['U'], 2 * layer['D']
    elif c == 'R':
        layer['L'], layer['R'] = layer['R'] + layer['L'], 1
        layer['U'], layer['D'] = 2 * layer['U'], 2 * layer['D']

print(layer[side])
