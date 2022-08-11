import sys

sys.setrecursionlimit(10**9)

def dfs(s):
    for i in tree[s]:
        if visited[i] == 0:
            visited[i] = s
            dfs(i)

node = int(input())
tree = [[] for _ in range(node+1)]
visited = [0, 1] + [0 for _ in range(node-1)]

for _ in range(node-1):
    a, b = map(int, sys.stdin.readline().split())
    tree[a].append(b)
    tree[b].append(a)

dfs(1)
print(*visited[2:], sep= "\n")

'''
트리 문제지만 알고리즘 분류에 dfs가 있길래 써버렸다.
한가지 신박했던 건 기존 dfs에는 visited에 방문했던 점이나 TF로 만들었었는데, 이건 visited에 그 전의 점을 넣는다는 것에서 조금 신기했다. 
방문했던 경로 자체를 알고 싶으면 이렇게 해도 되는구나였다.
'''