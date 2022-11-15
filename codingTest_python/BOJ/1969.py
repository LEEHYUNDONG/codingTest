import sys
input = sys.stdin.readline

N, M = map(int, input().split())
lst = [input().strip() for _ in range(N)]
result = ''
count = 0
lst.sort()

for i in range(M):
    A = [0,0,0,0] # a,c,g,t
    for j in range(N):
        if lst[j][i] == 'A':
            A[0]+=1
        elif lst[j][i] == 'C':
            A[1]+=1
        elif lst[j][i] == 'G':
            A[2]+=1
        elif lst[j][i] == 'T':
            A[3]+=1
    idx = A.index(max(A))
    if idx == 0:
        result += 'A'
    elif idx==1:
        result += 'C'
    elif idx==2:
        result += 'G'
    elif idx==3:
        result += 'T'  
    count += N - max(A)

print(result)
print(count)