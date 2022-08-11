def move(current, direction):
    moving = {
        "R": [1,0],
        "L": [-1,0],
        "B": [0,-1],
        "T": [0,1],
        "RB": [1,-1],
        "RT": [1,1],
        "LB": [-1,-1],
        "LT": [-1,1]
    }
    # 현재 위치와 무빙의 위치를 합침. 이때 맵을 이탈하는 경우 원래대로 되돌림
    result = [i+j for i,j in zip(current, moving[direction])]
    if all([0<i and i<9 for i in result]):
        return result
    else:
        return current


row = ["A", "B", "C", "D", "E", "F", "G", "H"]

king, stone, count = map(str, input().split())
direction_king = [row.index(king[0])+1, int(king[1])]
direction_stone = [row.index(stone[0])+1, int(stone[1])]

for _ in range(int(count)):
    goal = str(input())
    # 이동하지 못하게 되는 경우 되돌아와야 함, 바로 직전의 킹의 위치 기억
    prev_king = direction_king
    direction_king = move(direction_king, goal)
    if direction_king == direction_stone:
        # 킹이 움직였는데 스톤이 있고, 스톤이 못 움직이는 경우: 바로 직전의 킹으로 되돌아감.
        # 스톤이 움직일 수 있는 경우 스톤도 옮김
        if direction_stone == move(direction_stone, goal):
            direction_king = prev_king
        else:
            direction_stone = move(direction_stone, goal)

result_king = [row[direction_king[0]-1], str(direction_king[1])]
result_stone = [row[direction_stone[0]-1], str(direction_stone[1])]

print(''.join(result_king))
print(''.join(result_stone))