
def dfs_visit(node):
    if node not in influenced_by:
        return
    global distance, answer
    for n in influenced_by[node]:
        if n not in distance:
            distance[n] = distance[node]+1
            if distance[n] > answer:
                answer = distance[n]
            dfs_visit(n)
        elif distance[n] <= distance[node]:
            distance[n] = distance[node]+1
            if distance[n] > answer:
                answer = distance[n]
    return


ancestors = set()
siblings = set()

n = int(input())  # the number of relationships of influence
influenced_by = {}
for i in range(n):
    # x: a relationship of influence between two people (x influences y)
    x, y = [int(j) for j in input().split()]
    if x in influenced_by:
        influenced_by[x].append(y)
    else:
        influenced_by[x] = [y]
    ancestors.add(x)
    siblings.add(y)

start_set = ancestors - siblings

answer = 0
for s in start_set:
    distance = {s: 1}
    dfs_visit(s)

# The number of people involved in the longest succession of influences
print(answer)
