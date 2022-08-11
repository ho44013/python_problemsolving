import sys

times = []

for _ in range(int(input())):
    times.append(list(map(int, sys.stdin.readline().split())))

times = sorted(times, key = lambda x: (x[0], x[1]-x[0]))

cnt = 1
last = times[0]

for i in times[1:]:
    if last[0] <= i[0] and last[1] > i[1]:
        last = i
    elif i[0] >= last[1]:
        cnt += 1
        last = i

print(cnt)

'''
사실 이게 왜 그리디인지 모르겠긴 했는데...
'''