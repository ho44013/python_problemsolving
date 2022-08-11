def solution(numbers, hand):
    answer = ''
    keypad = {
        1: [0,3],
        2: [1,3],
        3: [2,3],
        4: [0,2],
        5: [1,2],
        6: [2,2],
        7: [0,1],
        8: [1,1],
        9: [2,1],
        0: [1,0]    
    }
    current_left, current_right = [0,0], [2,0]
    for target in numbers:
        if target in (1, 4, 7):
            answer += 'L'
            current_left = keypad[target]
        elif target in (3, 6, 9):
            answer += 'R'
            current_right = keypad[target]
        else:
            dist_left = abs((keypad[target])[0]-current_left[0])+abs((keypad[target])[1]-current_left[1])
            dist_right = abs((keypad[target])[0]-current_right[0])+abs((keypad[target])[1]-current_right[1])
            if dist_left > dist_right:
                answer += 'L'
                current_left = keypad[target]
            elif dist_left < dist_right:
                answer += 'R'
                current_right = keypad[target]
            else:
                if hand == "left":
                    answer += 'L'
                    current_left = keypad[target]
                else:
                    answer += 'R'
                    current_right = keypad[target]
    return answer