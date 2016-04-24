# python3

import sys

n, m = map(int, sys.stdin.readline().split())
lines = list(map(int, sys.stdin.readline().split()))
rank = [1] * n
parent = list(range(0, n))
ans = max(lines)

def getParent(table):
    # find parent and compress path
    if table != parent[table]:
      parent[table] = getParent(parent[table])
    return parent[table]

def merge(destination, source):
    realDestination, realSource = getParent(destination), getParent(source)

    if realDestination == realSource:
      return(max(lines))

    # merge two components
    # use union by rank heuristic
    # update ans with the new maximum table size
    if rank[realDestination] > rank[realSource]:
      parent[realSource] = realDestination
      lines[realDestination] += lines[realSource]
    else:
      parent[realDestination] = realSource
      if rank[realDestination] == rank[realSource]:
        rank[realSource] += 1
      lines[realSource] += lines[realDestination]
    return(max(lines))

    return True

for i in range(m):
    destination, source = map(int, sys.stdin.readline().split())
    print(merge(destination - 1, source - 1))
    # print(ans)

