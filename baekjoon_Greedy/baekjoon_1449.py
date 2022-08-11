'''
좌우 0.5만큼 추가로 막아야 하므로 길이가 2인 테이프로 2와 4를 동시에 막을 수 없음.
길이가 n이면 i부터 시작할 때 i + n - 1 까지만 막을 수 있다
== 마지막으로 커버되는 곳이 i + n - 0.5 다.

위치가 가까운 순서로 정렬하고 차례대로 테이프를 붙혀간다.
이때 앞에서 붙혔던 걸로 새로운 구멍을 막을 수 있다면 넘어간다.
'''

import sys

amt, length = map(int, input().split())
holes = sorted(list(map(int, sys.stdin.readline().split())))

covered = 0
ans = 0
for i in holes:
    if i < covered:
        continue
    else:
        ans += 1
        covered = i + length - 0.5

print(ans)
