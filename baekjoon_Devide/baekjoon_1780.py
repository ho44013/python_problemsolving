import sys

# 종이 안의 숫자가 모두 같은 숫자인지 체크
def check(x, y, size):
    global paper
    fivot = paper[x][y]
    for i in range(size):
        for j in range(size):
            if fivot != paper[x+i][y+j]:
                return False
    return True

# 종이 분할. 체크가 True면 ans에 값을 더해주고 아니면 나누기
def devide(x, y, size):
    global ans
    global paper
    if check(x, y, size):
        ans[paper[x][y]+1] += 1
    else:
        new_size = size//3
        for i in range(3):
            for j in range(3):
                devide(x+new_size*i, y+new_size*j, new_size)

length = int(input())
paper = []
ans = [0, 0, 0]

for _ in range(length):
    paper.append(list(map(int, sys.stdin.readline().split())))

devide(0, 0, length)
print(*ans, sep='\n')



'''
솔직히 말해서 문제 보자마자 바로 해설 보러갔다.
분할 진짜 책 볼때마다 그냥 넘겼던 부분인데 이번 기회에 확실하게 잡고 가야될 것 같다.
기본적으로 분할 문제의 순서는 최소 문제로 분할하고, 그 최소 문제일때의 푸는 방법을 알아야 할 것 같았다.
'''