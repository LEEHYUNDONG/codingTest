def solution(id_list, report, k):
    answer = []
    reportDic = {}
    for i in id_list:
        reportDic[i] = 0
    report = sorted(list(set(report)))
    for i in report:
        id1, id2 = i.split()
        reportDic[id2] += 1

    answerDic = {}
    for i in id_list:
        answerDic[i] = []
    for i in report:
        id1, id2 = i.split()
        if reportDic[id2] >= k:
            answerDic[id1].append(id2)

    for i in answerDic.keys():
        answer.append(len(answerDic[i]))

    return answer
