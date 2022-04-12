n = int(input())

nlst = list(map(int, str(n)))
nlst.sort(reverse=True)

sumN = sum(nlst)
ans = ''
if (nlst[-1] == 0 and sumN % 3 == 0):
    for i in nlst:
        ans += str(i)
    print(int(ans))
else:
    print(-1)