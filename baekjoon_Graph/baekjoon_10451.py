import sys

sys.setrecursionlimit(2000)

def dfs(s):
    cycle.append(s)
    visited.append(s)
    if graph[s] not in visited:
        dfs(graph[s])

for _ in range(int(input())):
    points = int(input())
    cnt = 0
    graph = [0] + list(map(int, sys.stdin.readline().split()))
    visited = []
    for i in graph[1:]:
        if i not in visited:
            cycle = []
            dfs(i)
            cnt += 1
    print(cnt)   


'''
순열 싸이클에 관한 문제. 개념을 몰라서 풀기 힘들었지만 dfs로 풀었다.
다른 정점의 목적지가 같은 정점이 나올수도 있다는 생각에 어떻게 해야하나 고민이었지만 그럴 일은 없다고...
시간은 3000ms 가량 나왔다. 재귀의 횟수 제한도 늘려주어야 했다. 다음에 볼때 최적화할 수 있는 방법이 있나 검토해볼것.
'''
