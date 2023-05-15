import sys
input = sys.stdin.readline

N, M = map(int, input().split())
wordDic = dict()

for i in range(N):
    w = input().rstrip()
    if len(w) < M:
        continue
    if w not in wordDic.keys():
        wordDic[w] = 0
    wordDic[w] += 1


tmp = sorted(wordDic.items(), key = lambda x : (-x[-1],-len(x[0]),x[0]))


for i in tmp:
    print(i[0])