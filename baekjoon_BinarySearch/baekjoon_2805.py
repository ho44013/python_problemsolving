import sys

def check(fivot):
    cnt = 0
    for i in trees:
        if i >= fivot:
            cnt += i - fivot
    return cnt >= M

N, M = map(int, input().split())
trees = list(map(int, sys.stdin.readline().split()))

start = 0
end = max(trees)

while start <= end:
    mid = (start+end)//2
    if check(mid):
        start = mid + 1
    else:
        end = mid - 1

print(end)

'''
체크 코드를 짜는 것에서, 처음 나는 모든 i에 대해 cnt += max(0, i-fivot)으로 짰는데
타임아웃이 발생했다.
왜 발생한지는 모르겠는데...
'''