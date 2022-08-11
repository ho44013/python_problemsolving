import sys
from collections import defaultdict

def dfs(s):
    discovered_dfs.append(s)
    for i in graph[s]:
        if i not in discovered_dfs:
            dfs(i)


def bfs(s):
    discovered_bfs.append(s)
    queue = [s]
    while queue:
        v = queue.pop(0)
        for i in graph[v]:
            if i not in discovered_bfs:
                discovered_bfs.append(i)
                queue.append(i)


graph = defaultdict(list)
point, line, start_point = map(int, input().split())
discovered_dfs = []
discovered_bfs = []

for _ in range(int(line)):
    start, end = map(int, sys.stdin.readline().split())
    graph[start].append(end)
    graph[end].append(start)
for i in graph:
    graph[i].sort()


dfs(start_point)
bfs(start_point)
print(*discovered_dfs, sep=" ")
print(*discovered_bfs, sep=" ")