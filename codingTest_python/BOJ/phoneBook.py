import re
import sys
input = sys.stdin.readline

t = int(input())
ans = []

def solution(phone_book):
    answer = True
    phone_book.sort()
    for i in range(len(phone_book)-1):
        if len(phone_book[i]) < len(phone_book[i+1]):
            if phone_book[i + 1][:len(phone_book[i])] == phone_book[i]:
                answer = False
                break
    return answer

for _ in range(t):
    n = int(input())
    phone = [input().strip() for _ in range(n)]
    if solution(phone):
        ans.append('YES')
    else:
        ans.append('NO')

for i in ans:
    print(i)