n = int(input())
k = int(input())
s = input()
cnt = 0
ss = "IOI"
ss += "OI"*(n-1)

for i in range(k-len(ss)):
    if s[i] == 'O':
        continue
    if s[i] == 'I':
        flag = False
        if s[i:i+len(ss)] == ss:
            cnt += 1

print(cnt)
