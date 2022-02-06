a, b, c = map(int, input().split())

num  = a
def pow(a, b, c):
    num = a
    if b == 0:
        return 1
    tmp = pow(a, b//2, c)
    tmp = tmp * tmp % c
    if b % 2 == 0:
        return tmp
    return a*tmp%c
        
res = pow(a, b, c)
print(res)