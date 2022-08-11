import sys

# 분할된 부분 안에 있는 것들이 전부 같은 숫자면 True
def check(x, y, size):
    fivot = nums[x][y]
    for i in range(x, x+size):
        for j in range(y, y+size):
            if fivot != nums[i][j]:
                return False
    print(str(fivot), end='')
    return True


# 분할
def devide(x, y, size):
    if check(x, y, size):
        return
    else:
        new_size = size//2
        print('(', end='')
        for i in range(2):
            for j in range(2):
                devide(x+i*new_size, y+j*new_size, new_size)
        print(')', end='')


length = int(input())
nums = []
for _ in range(length):
    nums.append(list(map(int, list(sys.stdin.readline().strip()))))

devide(0, 0, length)


'''
색종이 접기랑 비슷했던 문제, 다만 색종이접기는 메인 영역에 있던 변수에 저장했다면 여기는 바로바로 출력했다는 것의 차이...?
'''