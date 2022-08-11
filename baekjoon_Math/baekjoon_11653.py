num = int(input())

divisor = 2
max_divisor = int(num**0.5)

while num != 1 or divisor <= max_divisor:
    if num%divisor == 0:
        print(divisor)
        num = num // divisor
    else:
        divisor += 1

'''
전형적인 소인수분해 문제.
시간은 1575ms로 오래 걸렸는데

import math

num = int(input())
divisor = 2
max_divisor = int(math.sqrt(num))

while divisor <= max_divisor:
    if num%divisor != 0:
        divisor = divisor + 1
    else:
        print(divisor)
        num = num//divisor
if num > 1:
    print(num)


의 코드 같은 경우는 72ms가 나왔다.
앞으로 소인수분해와 관련된 문제는 위와 같은 방법으로 푸는 것이 빠를 것 같다.
다만 아직 왜 뒤의 코드가 빠른지는 모르겠다...
'''