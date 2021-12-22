import sys
input = sys.stdin.readline
n = input().rstrip()
b = int(input())

l = list(n)
r = []
for s in range(b):
    x = input().rstrip()
    if x == 'L' and l:
        r.append(l.pop())
    elif x == 'D' and r:
        l.append(r.pop())
    elif x == 'B' and l:
        l.pop()
    else:
        if x[0] == 'P':
            l.append(x[2])
            
print(''.join(l+r[::-1]))