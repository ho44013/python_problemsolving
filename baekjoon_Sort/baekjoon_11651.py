import sys

points = []
for _ in range(int(input())):
    points.append(list(map(int, sys.stdin.readline().split())))

# 조건을 y좌표 기준으로 하되, x좌표도 추가하고 싶으면 키에 이런 식으로 넣자
points = sorted(points, key=lambda x: (x[1], x[0]))

for i in points:
    print(f'{i[0]} {i[1]}')