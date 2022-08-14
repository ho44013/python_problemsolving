'''
떨어져 있는 거리를 이동할 수 있는 거리로 나눠서, 가장 빨리 도착하는 몬스터만 신경써주면 됨.
어차피 다른 몬스터는 가장 빨리 도착하는 몬스터보다는 늦게 올 테니 다른 몬스터한테 잡힐 일은 없다.
limit가 1 미만, 즉 다음 단위 시간동안 금화를 줍는다면 몬스터에게 잡히는 경우에는 금화를 줍지 않고,
나머지 시간에는 금화를 줍는다.

+ 처음부터 한번에 올 수 있는 거리가 현재 거리보다 가까운 경우, 그냥 0을 출력한다.
안 주운다고 해서 원래 자리에서 더 이동하는 게 아니라서 어차피 못 줍는건 매한가지다.
'''

import sys

time, gold, monster = map(int, input().split())

mon_list = []
if monster == 0:
    print(time*gold)
    exit(0)
for _ in range(monster):
    mon_list.append(list(map(int, sys.stdin.readline().split())))
mon_list.sort(key = lambda x: x[0]/x[1])

limit = mon_list[0][0]/mon_list[0][1]
if limit <= 1:
    print(0)
    exit(0)
ans = 0

for i in range(time):
    if limit <= 1:
        limit += 1
        continue
    else:
        ans += gold
        limit -= 1

print(ans)