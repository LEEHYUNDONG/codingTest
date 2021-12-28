import sys
input = sys.stdin.readline

n = int(input())
cnt = 0
six = 666

while True:
    if '666' in str(six):
        print(six)
        cnt += 1
    if cnt == n:
        print(six)
        break
    six += 1
