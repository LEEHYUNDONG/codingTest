import sys
input = sys.stdin.readline

n = int(input())
arr = [int(input()) for _ in range(n)]
# 1
print(round(sum(arr)/n))

# 2
arr.sort()
print(arr[int((n-1)/2)])

#3
nd = {}
for i in arr:
    if i not in nd.keys():
        nd[i] = 0
    else:
        nd[i] += 1


mv = max(nd.values())
ans = []

for i in nd.keys():
    if nd[i] == mv:
        ans.append(i)

if len(ans) == 1:
    print(ans[0])
else:
    ans.sort()
    print(ans[1])

print(arr[-1]-arr[0])
