import sys

nums = [0 for _ in range(10001)]

for _ in range(int(input())):
    nums[int(sys.stdin.readline())] += 1

for i in range(1, len(nums)):
    for j in range(nums[i]):
        print(i)

'''
기존 sort를 사용하지 않은 이유:
하나씩 입력받아 리스트에 append하고 sort 한 결과 메모리 초과가 발생했다.
리스트의 각 원소마다 10000이라는 숫자가 들어가면,
10000000개의 원소에 10000이라는 숫자를 할당해야 하는데, 이는 메모리 초과가 나기 충분하다
'''