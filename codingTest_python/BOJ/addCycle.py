N = int(input())

cnt = 1
new_num = N

while True:
    first = new_num//10
    second = new_num%10
    new_num = second*10 + (first+second)%10
    if new_num == N:
        print(cnt)
        break
    cnt+=1


