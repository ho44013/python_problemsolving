'''
0부터 indexerror가 발생하지 않을 지점까지 i를 순회, 이때 i는 note에서 비교를 시작할 인덱스.
이후 fivot의 길이만큼 j를 순회, 중간에 다르다면 바로 break 하여 i+1부터 다시 비교 시작
만약 note[i:i+len(fivot)]이 fivot과 전부 같음을 j for loop로 파악하게 되면,
파악한 마지막 인덱스 즉, 중복이 되지 않게 find_index로 지정해주었고,
이후 i를 순회할 때 find_index보다 작다면 중복이 될 수 있으므로 배제해줌.
'''


note = str(input())
fivot = str(input())

# 처음에 0으로 했다가 i가 0일때 안 찾아버렸음...
find_index = -1 
ans = 0

for i in range(0, len(note)-len(fivot)+1):
    if i <= find_index:
        continue
    cnt = 0
    for j in range(i, i+len(fivot)):
        if note[j] == fivot[cnt]:
            cnt += 1
        else:
            break
        if cnt == len(fivot):
            ans += 1
            find_index = j
            cnt = 0

print(ans)

