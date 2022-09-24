def solution(today, terms, privacies):
    answer = []
    
    def dateToDay(yy, mm, dd):
        return 28*12*yy + mm*28 + dd

    # terms dictionary
    termDic = dict()
    for term in terms:
        t, durr = term.split(' ')
        termDic[t] = int(durr)

    # 오늘 날짜 분리
    yy, mm, dd = map(int, today.split('.'))
    yy -= 2000
    totToday = dateToDay(yy, mm, dd)

    for i in range(len(privacies)):
        date, ptype = privacies[i].split(' ')
        ty, tm, td = map(int, date.split('.')) # 대상 날짜 계산
        ty -= 2000
        # calculate the term from today to target date
        totTarget = dateToDay(ty, tm + termDic[ptype], td)

        # print(term.days)
        
        if totTarget-1 < totToday:
            answer.append(i+1)


    return answer