'''
자신의 예상 등수가 낮은 순서대로 정렬, 이후 각 인덱스와 예상한 순위의 차를 구해서 더한다
'''

import sys

people = int(input())

ranks = []
for _ in range(people):
    ranks.append(int(sys.stdin.readline()))
ranks.sort()

ans = 0
for index, rank in enumerate(ranks):
    ans += abs(index-rank+1)

print(ans)