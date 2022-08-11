import sys

sys.setrecursionlimit(111111)

def dfs(s, curr_team):
    visited_stud[s] = True
    curr_team.append(s)
    if visited_stud[graph[s]]:
        if graph[s] in curr_team:
            return curr_team.index(graph[s])
        else:
            return len(curr_team)
    else:
        return dfs(graph[s], curr_team)

for _ in range(int(input())):
    students = int(input())
    graph = [0] + list(map(int, sys.stdin.readline().split()))
    ans = 0
    visited_stud = [False] * (students + 1)
    for i in range(1, students+1):
        if not visited_stud[i]:
            ans += dfs(i, [])
    print(ans)


'''
학생의 범위가 100000명 까지라서 재귀의 범위를 100000 이상으로 해주었다.
모든 학생이 다 싸이클로 연결되어 있는 케이스도 있을 수 있기 때문에...
처음에는 재귀의 범위를 2000까지 했다가 오류가 발생했다.
재귀를 사용해야 할 때, 사용해야 할 재귀의 횟수를 예상하고 설정하는 것이 좋다는 것을 알았다.
'''