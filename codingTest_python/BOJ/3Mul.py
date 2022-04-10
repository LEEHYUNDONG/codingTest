n = int(input())

res = [3, 6, 9]
x = n
ans = 0

while True:
    if 0 <= x < 10:
        break
    x = list(str(x))
    y = 0
    for i in x:
        y += int(i)
    x = y
    ans += 1

print(ans)
if x in res:
    print("YES")
else:
    print("NO")