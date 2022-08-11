from collections import Counter

ori = str(input())
word_list = Counter(sorted(list(ori)))
words = sorted(word_list.most_common(), key = lambda x: x[0])


already_odd = False
ans = ''
last = ''

for word, times in words:
    if times%2 == 1 and already_odd:
        print("I'm Sorry Hansoo")
        exit(0)
    elif times%2 == 1:
        already_odd = True
        last = word
    ans = ans + word*(times//2)

ans = ans + last + ans[::-1]
print(ans)



'''
주어진 글자의 순서를 섞어 펠린드롬 만드는 문제.
나는 각 문자의 개수를 세서 개수가 홀수인 알파벳이 두 종류면 펠린드롬이 안 만들어지기에
그걸 판별하는 if 문을 하나 만들었고,
나머지는 사전 순서대로 반토막을 만든 후, last(홀수가 한종류면 그건 가운데에) 라는 변수를 따로 만들어
반토막 + last(없으면 무시) + 반토막의 [::-1] 로 펠린드롬을 만들었따.

'''