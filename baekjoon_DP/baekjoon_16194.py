import sys

total = int(input())
price_list = [0] + list(map(int, sys.stdin.readline().split()))
DP = [0 for i in range(total+1)]

DP[1] = price_list[1]

for i in range(2, total+1):
    DP[i] = min([DP[k]+DP[i-k] for k in range(1, i)])
    DP[i] = min(DP[i], price_list[i])

print(DP[-1])