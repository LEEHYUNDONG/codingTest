A, P = map(int, input().split())
arr = [A]
while True:
    tmp = arr[-1]
    tot = 0
    ten = 10**len(str(tmp))
    while tmp:
        tot += (tmp//ten)**P
        tmp = tmp%ten
        ten = ten//10
    if tot in arr:
        print(len(arr[:arr.index(tot)]))
        break
    arr.append(tot)