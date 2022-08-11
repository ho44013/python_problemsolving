num = sorted(list(str(input())), reverse=True)
num = list(map(int, num))

if sum(num) % 3 != 0 or num[-1] != 0:
    print(-1)
else:
    print(*num, sep='')

'''
수를 재배치해서 30의 배수가 되게 할 때 그때의 가장 큰 수를 찾는 문제.
30의 배수는 3과 10 각각을 약수로 가지므로 끝자리가 0이고 자릿수이 합이 3의 배수여야 함.
각 자리수를 크기순으로 정렬하고 조건에 따라 아니면 -1 출력. 맞으면 이미 정렬해뒀으므로 그대로 출력하면 됨!
'''