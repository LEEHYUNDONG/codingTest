import sys
input = sys.stdin.readline

n = int(input())
m = int(input())

p = "IOI" + "OI"*(n-1)
s = input().rstrip()
ind = 1
ans = 0
pat = 0

while ind < m-1:
    if s[ind-1] == 'I' and s[ind] == 'O' and s[ind+1] == 'I':
        pat += 1
        if pat == n:
            ans += 1
            pat -= 1
        ind += 1
    else:
        pat = 0
    ind += 1

print(ans)
