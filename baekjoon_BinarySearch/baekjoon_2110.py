import sys

N, C = map(int, input().split())
house = []

for _ in range(N):
    house.append(int(sys.stdin.readline().strip()))

house.sort()

minL = 1
maxL = house[-1] - house[0]

while minL <= maxL:
    cnt = 1
    gap = (minL + maxL) // 2
    start = house[0]
    for i in range(1, len(house)):
        if start + gap <= house[i]:
            cnt += 1
            start = house[i]
    if cnt < C:
        maxL = gap - 1
    else:
        minL = gap + 1
        
print(maxL)

'''
문제 이해가 어려웠다! 뭔 소린지 모르겠고 그림을 그려봐도 어떻게 짤지 막막했다
그래도 이런 문제류의 알고리즘의 흐름 자체는 슬슬 이해할 수 있을 것 같다.
우선 조건을 만족하게 하는 코드를 짜고, 그 조건을 만족하는 수의 범위를 찾아야 한다.
그 후 이진탐색을 진행하여 최적의 값, 즉 마지노선을 찾는 게 목표다!
'''