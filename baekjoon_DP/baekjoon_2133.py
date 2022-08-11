N = int(input())
DP = [0 for _ in range(31)]

DP[0] = 1
DP[2] = 3

for i in range(4, 31, 2):
    case = DP[i-2] * 3
    for j in range(4, i, 2):
        case += DP[i-j] * 2
    DP[i] = case + 2

print(DP[N])