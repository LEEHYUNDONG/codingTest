import sys

input = sys.stdin.readline
n = int(input())

word = []
res = []

for i in range(n):
    word.append([input().strip(), i])

word.sort()
maxL = -1

for i in range(n-1):
    if word[i][0][0] == word[i+1][0][0]:
        if word[i+1][0].startswith(word[i][0]) and maxL <= len(word[i]) or word:
            res.append([word[i], word[i+1], maxL])
            maxL = len(word[i][0])


res.sort(key = lambda x:x[-1], reverse=True)
res.sort(key = lambda x:x[0][1])

ans = [res[0][0], res[0][1]]

