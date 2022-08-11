import sys

'''
손님들이 주려고 했던 팁을 오름차순 (사실 내림차순이었음!) 으로 정렬 후, 각각의 인덱스를 빼주기.
음수면 0 더하기

내림차순이었던 이유는, 어차피 팁-인덱스가 음수면 0으로 바뀌기에 인덱스가 높은 곳에 낮은 수를 배치하면
어차피 0이고, 그만큼 낮은 인덱스에 높은 값을 배치할 수 있었기 때문이다.
'''

people = int(input())
tips = []

for _ in range(people):
    tips.append(int(sys.stdin.readline()))

tips.sort(reverse=True)

ans = 0
for diff, tip in enumerate(tips):
    if diff < tip:
        ans += (tip-diff)
print(ans)