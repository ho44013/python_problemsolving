import sys

num = int(input())
ropes = []

for _ in range(num):
    ropes.append(int(sys.stdin.readline()))

ropes.sort(reverse=True)

ans = 0
for i in range(1, num+1):
    weight = ropes[i-1] * i
    if ans < weight:
        ans = weight

print(ans)

'''
개수와 사용하는 로프의 최솟값에 따라 들 수 있는 무게가 달라지므로,
내림차순으로 정렬 후 개수를 늘려가며 비교했다.
'''