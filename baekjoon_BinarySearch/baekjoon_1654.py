import sys

def check(fivot):
    cnt = 0
    for i in length:
        cnt += i//fivot
    return cnt >= N

K, N = map(int, input().split())
length = []
end = 0

for _ in range(K):
    u = int(sys.stdin.readline().strip())
    if end < u:
        end = u
    length.append(u)

start = 1

while start <= end:
    mid = (start+end)//2
    if check(mid):
        start = mid+1
    else:
        end = mid-1

print(end)

'''
탐색 알고리즘의 시작, 이진탐색으로 시작한다.
이진 탐색에 대해서는 어느정도 잘 알고 있었지만, 체크 한 이후 start와 end를 바꿔주는게 익숙치 않았다..
'''