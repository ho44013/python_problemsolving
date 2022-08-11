import sys

info = []
for _ in range(int(input())):
    info.append(list(map(str, sys.stdin.readline().split())))

info = sorted(info, key=lambda x: int(x[0]))

for i in info:
    print(f'{i[0]} {i[1]}')


# sort 를 사용했지만, sort를 사용하지 않는 경우 불안정 정렬 (퀵 정렬 등) 을 사용해서는 안됨
# 불안정 정렬을 시행할 경우 가입한 순서를 섞어버릴 수 있음!