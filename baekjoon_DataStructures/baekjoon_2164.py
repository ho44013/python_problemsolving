from collections import deque

num = int(input())
cards = deque(list(range(1, num+1)))

while len(cards) != 1:
    cards.popleft()
    cards.append(cards.popleft())

print(cards[0])