nums = list(map(str, list(input())))
DP = [1 for _ in range(len(nums))]
last = nums[0]
if last == '0':
    print(0)
    exit(0)

for i in range(1, len(nums)):
    if nums[i] != '0':
        last += nums[i]
        if last[0] == '0':
            DP[i] = DP[i-3]
        elif int(last) > 26:
            DP[i] = DP[i-1]
        else:
            DP[i] = DP[i-1]+DP[i-2]
    else:
        if last in ('1', '2'):
            DP[i] = DP[i-2]
        else:
            DP[-1] = 0
            break
    last = nums[i]
    DP[i] = DP[i]%1000000

print(DP[-1])