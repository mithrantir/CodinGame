
def add_link(a, b):
    if a not in linksOf:
        linksOf[a] = [b]
    elif b in linksOf[a]:
        return
    else:
        linksOf[a].append(b)
    add_link(b, a)
    return


# n: the total number of nodes in the level, including the gateways
# l: the number of links
# e: the number of exit gateways
n, l, e = [int(i) for i in input().split()]
linksOf = {}
for i in range(l):
    # n1: N1 and N2 defines a link between these nodes
    n1, n2 = [int(j) for j in input().split()]
    add_link(n1, n2)

gateway = {}
for i in range(e):
    ei = int(input())  # the index of a gateway node
    gateway[ei] = -1

# game loop
while True:
    si = int(input())  # The index of the node on which the Skynet agent is positioned this turn

    # bfs search
    x,  y, found = -1, -1, False
    dist_from_agent, bfs_queue = {si:0}, [si]
    while len(bfs_queue) > 0:
        node = bfs_queue.pop(0)
        for n in linksOf[node]:
            if n in gateway:
                x, y, found = n, node, True
                linksOf[x].pop(linksOf[x].index(y))
                linksOf[y].pop(linksOf[y].index(x))
                break
            elif n not in dist_from_agent:
                dist_from_agent[n] = dist_from_agent[node]+1
                bfs_queue.append(n)

        if found:
            break

    # Example: 0 1 are the indices of the nodes you wish to sever the link between
    print("{} {}".format(x,y))
