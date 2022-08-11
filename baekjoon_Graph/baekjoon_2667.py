import sys

def dfs(x, y):
    if x >= size or x < 0 or y >= size or y < 0:
        return
    if grid[x][y] == '1':
        global cnt
        cnt += 1
        grid[x][y] = '0'
        dfs(x-1, y)
        dfs(x+1, y)
        dfs(x, y-1)
        dfs(x, y+1)
    return

size = int(input())
grid = []
cnt = 0
cnts = []
total = 0
for _ in range(size):
    grid.append(list(sys.stdin.readline().strip()))
    
for i in range(size):
    for j in range(size):
        if grid[i][j] == '1':
            dfs(i, j)
            total += 1
            cnts.append(cnt)
            cnt = 0

print(total)
print(*sorted(cnts), sep='\n')



'''
책에서 봤던 문제긴 한데 직접 구현해보려니깐 그렇게 쉽지는 않았다. 
dfs함수의 백트래킹 조건에서 grid[x][y] 가 0인 경우를 같이 넣지 않은 이유는 만약 땅이 아니라면 indexerror가 나지 않을까 해서였다.
dfs 문제를 다룰때는 항상 백트래킹 조건을 잘 생각하면서 다루자.
'''