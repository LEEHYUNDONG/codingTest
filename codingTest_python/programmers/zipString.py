def solution(msg):
    answer = []
    alphaDic = {}

    for i in range(26):
        alphaDic[chr(ord('A')+i)] = i+1

    idx, loc = 27, 0
    curr = msg[0]
    ss = ''
    while loc < len(msg)-1:
        tmp = ''
        for j in range(loc, len(msg)):
            tmp += msg[j]
            if tmp not in alphaDic.keys():
                alphaDic[tmp] = idx
                idx += 1
                break
            curr = tmp
            ss += curr

        if curr in alphaDic.keys():
            answer.append(alphaDic[curr])
            loc += len(curr)

    if loc == len(msg)-1 and ss != msg:
        answer.append(alphaDic[msg[loc]])

    return answer
