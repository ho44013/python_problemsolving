'''
낱개 = r, 6개 세트 = s
if min(r)*6 <= s: r로 다사기,
elif min(r)*(needs%6) > min(s): 인 경우 그냥 min(s)로 다 사기
else: min(s)*(needs//6) + min(r)*(needs%6)
'''

import sys

needs, brand = map(int, input().split())

lines = []
for _ in range(brand):
    lines.append(list(map(int, sys.stdin.readline().split())))

rest = min(list(zip(*lines))[1])
package = min(list(zip(*lines))[0])
div, mod = needs//6, needs%6

if rest*6 <= package:
    print(rest*needs)
elif rest*mod > package:
    print(package*(div+1))
else:
    print(package*(div) + rest*(mod))