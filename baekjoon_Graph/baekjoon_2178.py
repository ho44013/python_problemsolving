import sys
from collections import deque

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

m, n = map(int, input().split())
grid = [list(sys.stdin.readline().strip()) for _ in range(m)]
visited = [[False for i in range(n)] for j in range(m)]
path = deque([(1, 0, 0)])

def bfs():
    while path:
        cnt, x, y = path.popleft()
        if (x, y) == (m-1, n-1):
            print(cnt)
            return
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if not (0 <= nx < m and 0 <= ny < n):
                continue
            if visited[nx][ny] or grid[nx][ny] == '0':
                continue
            path.append((cnt+1, nx, ny))
            visited[nx][ny] = True

bfs()

'''
방문했던 경로인지 아닌지를 판단하는 건 이차원 배열의 TRUE FALSE로 두자. in 특성상 시간복잡도가 폭발할수도...
'''