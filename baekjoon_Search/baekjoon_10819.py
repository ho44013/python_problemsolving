import itertools

def total(nums):
    ans = 0
    for i in range(0, len(nums)-1):
        ans += abs(nums[i]-nums[i+1])
    return ans

u = int(input())
num_list = list(map(int, input().split()))

maxNum = 0
for i in itertools.permutations(num_list):
    cnt = total(i)
    if maxNum <= cnt:
        maxNum = cnt

print(maxNum)

'''
다른 사람이 푼 걸 보니깐 이걸 아예 일반화를 해버려서 빠른 시간 내에 풀어버린 사람들이 있는데,
이 문제는 N의 최댓값이 8이라서 별 차이가 나지 않았던 것 같다.
N이 되게 컸다면 그렇게 하는게 맞지 않았을까?
'''