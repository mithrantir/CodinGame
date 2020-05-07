import re


def print_tree():
    tree_str = tree[0]
    for i in range(1, len(tree)):
        tree_str += " > " + tree[i]
    print(tree_str)


count = int(input())
tree, prdots = [], 1
for i in range(count):
    name, dots = re.subn(r'[.]', "", input())
    if dots <= prdots:
        if len(tree) > 0:
            print_tree()
        tree = tree[:dots]
    tree.append(name)
    prdots = dots

print_tree()
