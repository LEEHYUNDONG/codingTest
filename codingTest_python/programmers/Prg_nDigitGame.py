def solution(n, t, m, p):
    answer = ''
    numDic = {
        0: '0', 1: '1', 2: '2', 3: '3', 4: '4', 5: '5', 6: '6', 7: '7', 8: '8', 9: '9', 10: 'A', 11: 'B', 12: 'C', 13: 'D', 14: 'E', 15: 'F'
    }
    ans = '0'
    turn = 1
    for i in range(t*m):
        tmp = ''
        num = i
        if len(answer) == t:
            break
        while num > 0:
            tmp += numDic[num % n]
            num = num // n
        ans += tmp[::-1]

    # print(ans)
    for j in ans:
        if turn % m == p % m:
            answer += j
        if len(answer) == t:
            break
        turn += 1
    # print(answer)

    return answer
