# ㅇㅔ디터
import sys
input = sys.stdin.readline
word = list(input().rstrip())
n = int(input())
mv = 0
l = len(word)
idx = l-1

for i in range(l, l+n):
    tmp = sys.stdin.readline().rstrip()
    if tmp[0] == 'L':
        if idx < 0 :
            continue
        idx -= 1
    elif tmp[0] == 'D':
        if idx == len(word)-1:
            continue
        idx += 1
    elif tmp[0] == 'P':
        word.insert(idx+1, tmp[2])
        idx += 1
    elif tmp[0] == 'B':
        if idx < 0:
            continue
        del word[idx]
        idx -= 1

print(''.join(word))