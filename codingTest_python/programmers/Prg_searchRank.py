def comp(q, inf):
    for k in range(4):
        if q[k] == '-':
            continue
        if q[k] != inf[k]:
            return False
    return True


def solution(info, query):
    answer = []
    q = []
    inf = [list(info[i].split()) for i in range(len(info))]
    for i in range(len(query)):
        q.append(query[i].replace("and", ""))
    q = [list(q[i].split()) for i in range(len(q))]
    cnt = 0

    for i in range(len(q)):
        cnt = 0
        for j in range(len(inf)):
            if int(q[i][-1]) <= int(inf[j][-1]):
                if comp(q[i], inf[j]):
                    cnt += 1
        answer.append(cnt)

    return answer
