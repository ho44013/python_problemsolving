N, M, K = map(int, input().split())

for _ in range(K):
    if N ==0 or M ==0:
        print(0)
        exit(0)
    elif N//2 < M:
        M -= 1
    else:
        N -= 1

print(min(N//2, M))

'''
그리디 시작.
기본적으로 사람을 뺄 때 여자에서 빼되, 남자에서 빼는게 더 이득인 경우 즉, 남자가 모든여자랑 팀을 이루고도 남는 경우에만 남자를 빼면 된다.
'''