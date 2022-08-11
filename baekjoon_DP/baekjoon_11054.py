import sys

N = int(input())
DP = [1 for i in range(N)]
DP_reverse = [1 for i in range(N)]

nums = list(map(int, sys.stdin.readline().split()))
nums_reverse = nums[::-1]

# 정방향에서 보는 증가하는 수열
for i in range(1, N):
    values = [1]
    for j in range(0, i):
        if nums[i] > nums[j]:
            values.append(DP[j]+1)
    DP[i] = max(values)

# 역방향에서 보는 증가하는 수열, 이는 다시 정방향으로 돌려줘서 감소하는 수열로 만들어주기 위함
for i in range(1, N):
    values = [1]
    for j in range(0, i):
        if nums_reverse[i] > nums_reverse[j]:
            values.append(DP_reverse[j]+1)
    DP_reverse[i] = max(values)

DP_reverse = DP_reverse[::-1]

print(max(map(sum, zip(DP, DP_reverse))) -1)