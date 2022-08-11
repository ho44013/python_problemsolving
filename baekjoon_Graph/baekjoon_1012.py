import sys

sys.setrecursionlimit(10**6)

def dfs(pos_x, pos_y):
    if pos_x < 0 or pos_x >= row or pos_y < 0 or pos_y >= column:
        return
    if field[pos_y][pos_x] == 1:
        field[pos_y][pos_x] = 0
        dfs(pos_x+1, pos_y)
        dfs(pos_x-1, pos_y)
        dfs(pos_x, pos_y+1)
        dfs(pos_x, pos_y-1)
        
    
for _ in range(int(input())):
    row, column, amount = map(int, input().split())
    field = [[0 for i in range(row)] for j in range(column)]
    for ba in range(amount):
        ba_x, ba_y = map(int, sys.stdin.readline().split())
        field[ba_y][ba_x] = 1
    cnt = 0
    for i in range(column):
        for j in range(row):
            if field[i][j] == 1:
                dfs(j, i)
                cnt += 1
    print(cnt)


'''
필드에 깔린 땅의 개수 세는 문제
'''