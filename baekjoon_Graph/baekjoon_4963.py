import sys

sys.setrecursionlimit(3000)

dx = [0, 1, 1, 1, 0, -1, -1, -1]
dy = [1, 1, 0, -1, -1, -1, 0, 1]

def dfs(x, y):
    if x >= h or x < 0 or y >= w or y < 0:
        return
    if grid[x][y] == '1':
        grid[x][y] = '0'
        for i in range(len(dx)):
            ax = x + dx[i]
            ay = y + dy[i]
            dfs(ax, ay)
    return


while True:
    w, h = map(int, input().split())
    if not (w and h):
        break
    grid = []
    cnt = 0
    for _ in range(h):
        grid.append(list(map(str, sys.stdin.readline().split())))
    for i in range(h):
        for j in range(w):
            if grid[i][j] == '1':
                dfs(i, j)
                cnt += 1
    print(cnt)


'''
dfs에서 x와 y의 백트래킹 조건을 헷갈려서 되게 전에 풀었던 문제랑 같은 유형임에도 불구하고 오래 걸렸다. 변수명 잘 짓기...
알고리즘 자체는 2667번과 비슷했음!
'''