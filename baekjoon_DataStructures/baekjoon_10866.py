import sys

deque = list()

for _ in range(int(input())):
    command = list(map(str, sys.stdin.readline().split()))
    if command[0] == 'push_front':
        deque.insert(0, int(command[1]))
    elif command[0] == 'push_back':
        deque.append(int(command[1]))
    elif command[0] == 'pop_front':
        if deque:
            result = deque.pop(0)
            print(result)
        else:
            print(-1)
    elif command[0] == 'pop_back':
        if deque:
            result = deque.pop()
            print(result)
        else:
            print(-1)
    elif command[0] == 'size':
        print(len(deque))
    elif command[0] == 'empty':
        print(int(not bool(deque)))
    elif command[0] == 'front':
        if deque:
            print(deque[0])
        else:
            print(-1)
    else:
        if deque:
            print(deque[-1])
        else:
            print(-1)

'''
데크 구현 문제.
'''