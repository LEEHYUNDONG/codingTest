def solution(s):
    answer = []
    cnt0, cnt1 = 0, 0
    while True:
        if s == '1':
            break
        cnt0 += 1
        cnt1 += (len(s) - list(s).count('1'))
        s = '1'*(list(s).count('1'))
        s = bin(len(s))[2:]

    return [cnt0, cnt1]
