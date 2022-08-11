from collections import deque

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

def bfs():
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            if 0 <= nx < n and 0 <= ny < m and grid[nx][ny] == 0:
                grid[nx][ny] = grid[x][y] + 1
                queue.append([nx, ny])

        
m, n = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]
queue = deque([])
ans = 0

for i in range(n):
    for j in range(m):
        if grid[i][j] == 1:
            queue.append([i, j])

bfs()

for i in grid:
    for j in i:
        if j == 0:
            print(-1)
            exit(0)
    ans = max(ans, max(i))

print(ans-1)

'''
bfs로 푸는거였다!! 무지성으로 dfs로 풀려고 시도했는데 잘 안 풀려서 찾아보니 알고리즘 분류에 dfs가 읎더라...
문제 키워드 중 최소일수, 주변의 토마토를 익힘이란 키워드를 보고 깊게 들어가지 않아도 된다고 판단해 BFS로 시도했다는데.. 그건 아직 잘 모르겠다.
여하튼 BFS를 직접 짜본건 또 처음이라 익숙치 않았다. 얘도 연습 좀 해보자
'''