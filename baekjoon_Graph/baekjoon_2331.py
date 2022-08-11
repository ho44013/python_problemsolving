def next_num(curr_num, p):
    ans = 0
    for i in curr_num:
        ans += int(i)**int(p)
    return str(ans)

def dfs(s, p):
    if s in visited:
        global cycle_num
        cycle_num = s       
        return
    else:
        visited.append(s)
        dfs(next_num(s,p), p)

A, times = map(str, input().split())
cycle_num = 0
visited = []
dfs(A, times)

print(visited.index(cycle_num))

'''
알고리즘 자체는 쉬운 편이었음. 이게 왜 dfs 문제인지 모르겠지만...
'''