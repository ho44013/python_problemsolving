import sys

num = int(input())

lengths = []
for _ in range(num):
    lengths.append(int(sys.stdin.readline()))
lengths.sort(reverse=True)

for i in range(num-2):
    if lengths[i] >= lengths[i+1] + lengths[i+2]:
        continue
    else:
        print(sum(lengths[i:i+3]))
        exit(0)

print(-1)


'''
길이를 기준으로 하여 내림차순 정렬 후, 바로 다음과 다다음의 길이로 삼각형을 만들 수 있는지 판별.
어차피 i와 i+1, i+2로 삼각형을 만들 수 있다면 다른 인덱스를 비교할 필요가 없고
만약 다른 인덱스로 만들어진다고 해도 저것보다 길이가 길 수가 없다
'''