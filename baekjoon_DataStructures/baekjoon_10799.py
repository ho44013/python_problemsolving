command = list(map(str, list(input())))
ans = 0
stack = []

for i in range(len(command)):
    if command[i] == '(':
        stack.append(command[i])
    else:
        if command[i-1] == '(':
            stack.pop()
            ans += len(stack)
        else:
            stack.pop()
            ans += 1

print(ans)


'''
입력되는 경우가 '(' 와 ')' 밖에 없음.
'('의 경우는 쇠막대기가 시작하거나, 레이저의 시작이므로 스택에 push 해주고,
')'의 경우는 쇠막대기가 끝나거나, 레이저의 종료인 경우다.
레이저인지 아닌지는 바로 전의 입력값을 통해 알 수 있다.
'''
