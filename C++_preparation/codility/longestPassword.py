def solution(S):
    # write your code in Python 3.6
    
    S = S.split(' ')
    ans = -1
    for i in S:
        cntL, cntD = 0, 0
        for j in i:
            if j.isalpha():
                cntL += 1
            if j.isdigit():
                cntD += 1
        if cntL % 2 == 0 and cntD % 2 == 1 and cntD + cntL == len(i):
            ans = max(len(i), ans)

    return ans