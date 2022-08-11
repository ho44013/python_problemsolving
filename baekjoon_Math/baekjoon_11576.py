import sys

A, B = map(int, input().split())
length = int(input())
ans = []
A_list = list(map(int, sys.stdin.readline().split()))[::-1]
num_10 = 0

for i in range(length):
    num_10 += A_list[i] * (A ** i)


while num_10 >= B:
    ans.append(str(num_10%B))
    num_10 = num_10//B
ans.append(str(num_10))

print(*ans[::-1], sep=' ')


'''
처음 이 문제를 풀 때는 ans 변수의 type을 str로 한 후 같은 알고리즘을 진행했다.
그때는 틀린 답이 나왔었는데, 그 이유로 자릿수에 대해 오류가 있었던 것 같다.
원하던 답은 16 2 였다면, 1 6 2 와 같은 방식으로 출력이 되는 것 같았다.
그래서 list로 바꾼 뒤 같은 알고리즘을 진행했더니 맞았다.
'''