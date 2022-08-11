import sys

def bisearch(start, end, fivot):
    while start <= end:
        mid = (start+end) // 2
        if card[mid] == fivot:
            return 1
        elif card[mid] > fivot:
            end = mid-1
        else:
            start = mid+1
    return 0

N = int(input())
card = list(map(int, sys.stdin.readline().split()))
card.sort()

M = int(input())
target = list(map(int, sys.stdin.readline().split()))

for i in target:
    print(bisearch(0, len(card)-1, i), end=' ')


'''
이진 탐색을 했는데 시간이 오래걸렸고,
in을 사용했는데 빨리 끝나는 아이러니한 문제.
아마도 in을 사용하는 경우는 sort를 따로 해야 하므로 추가적인 시간이 걸린 것으로 예상이 된다.
'''