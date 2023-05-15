def solution(today, terms, privacies):
    answer = []
    yy, mm, dd = map(int, today.split("."))
    today_day = yy*12*28 + mm*28 + dd
    policy = dict()
    for t in terms:
        term, mm = t.split(' ')
        policy[term] = int(mm)
    
    
    for i, privacy in enumerate(privacies):
        date, term = privacy.split(' ')
        yy, mm, dd = map(int, date.split("."))
        
        
        mm += policy[term]
        if mm > 12:
            yy += mm//12
            mm = mm%12
        
        tot_day = yy*12*28 + mm*28 + dd
        if tot_day <= today_day:
            answer.append(i+1)
        
    return answer