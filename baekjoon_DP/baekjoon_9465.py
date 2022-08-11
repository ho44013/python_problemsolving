import sys

def DP(sticker):
    price = [[0, 0, 0] for _ in range(len(sticker))]
    price[0][0] = sticker[0][0]
    price[0][1] = sticker[0][1]
    for i in range(1, len(sticker)):
        price[i][0] = max(price[i-1][1]+sticker[i][0], price[i-1][2]+sticker[i][0])
        price[i][1] = max(price[i-1][0]+sticker[i][1], price[i-1][2]+sticker[i][1])
        price[i][2] = max(price[i-1])
    return max(price[-1])

for _ in range(int(input())):
    n = int(input())
    scores = []
    up_scores = list(map(int, sys.stdin.readline().split()))
    down_scores = list(map(int, sys.stdin.readline().split()))
    scores = list(zip(up_scores, down_scores))
    ans = DP(scores)
    print(ans)
        