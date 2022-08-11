import sys

queue = list()

for _ in range(int(input())):
    command = list(map(str, sys.stdin.readline().split()))
    if command[0] == 'push':
        queue.append(int(command[1]))
    elif command[0] == 'pop':
        if queue:
            result = queue.pop(0)
            print(result)
        else:
            print(-1)
    elif command[0] == 'size':
        print(len(queue))
    elif command[0] == 'empty':
        print(int(not bool(queue)))
    elif command[0] == 'front':
        if queue:
            print(queue[0])
        else:
            print(-1)
    elif command[0] == 'back':
        if queue:
            print(queue[-1])
        else:
            print(-1)


'''
큐 구현 문제,
pop(0)의 시간복잡도가 O(n) 이긴 한데 n의 크기가 작아서 시간이 얼마 안 걸림.
'''