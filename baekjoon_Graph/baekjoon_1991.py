def front_search(n):
    if n != '.':
        print(n, end=" ")
        front_search(tree[n][0])
        front_search(tree[n][1])

def middle_search(n):
    if n != '.':
        middle_search(tree[n][0])
        print(n, end=" ")
        middle_search(tree[n][1])
    
def back_search(n):
    if n != '.':
        back_search(tree[n][0])
        back_search(tree[n][1])
        print(n, end= " ")

nodes = int(input())
tree = dict()

for _ in range(nodes):
    root, left, right = map(str, input().split())
    tree[root] = [left, right]

front_search('A')
print()
middle_search('A')
print()
back_search('A')

'''
되게 오래걸렸고 결국 풀이까지 봐버린 문제.
트리 자체가 첫 문제기도 했지만 탐색 알고리즘 짜는 과정에서 많은 시간이 걸렸다.
재귀를 사용하는건 알고 있었지만...
'''