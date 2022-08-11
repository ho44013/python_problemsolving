import sys

sys.setrecursionlimit(5000)

def dfs(s):
    visited[s] = True
    for i in graph[s]:
        if not visited[i]:
            dfs(i)

point, lines = map(int, input().split())
graph = [[] for _ in range(point+1)]

for i in range(lines):
    start, end = map(int, sys.stdin.readline().split())
    graph[start].append(end)
    graph[end].append(start)

visited = [False] * (point+1)
cnt = 0

for i in range(1, point+1):
    if not visited[i]:
        if not graph[i]:
            cnt += 1
            visited[i] = True
        else:
            dfs(i)
            cnt += 1

print(cnt)