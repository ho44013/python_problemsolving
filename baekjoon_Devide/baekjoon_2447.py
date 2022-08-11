def devide(size):
    if size == 1:
        return ['*']
    Stars = devide(size//3)
    L = []
    for i in Stars:
        L.append(i*3)
    for i in Stars:
        L.append(i+' '*(size//3)+i)
    for i in Stars:
        L.append(i*3)
    return L

length = int(input())
print(*devide(length), sep='\n')


'''
분할 여전히 어렵다! 공부 더 해봐야 될 것같다.
알고리즘 자체는 여타 분할문제와 비슷하지만 출력하는 부분에서 조금 힘들었던 것 같다.
'''