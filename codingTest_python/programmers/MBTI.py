def solution(survey, choices):
    answer = ''
    '''
    1 - 7점
    '''
    score = {
        'R' : 0, 'T' : 0,
        'C' : 0, 'F' : 0,
        'J' : 0, 'M' : 0,
        'A' : 0, 'N' : 0
    }
    mbti = [
        ['R', 'T'],
        ['C', 'F'],
        ['J', 'M'],
        ['A', 'N']
    ]
    l = len(choices)
    
    for i in range(l):
        scr = choices[i] #점수 동의 여부에 따라 점수가 다르게 가지만 scr가 4미만인지 4초과인지가 중요
        if scr > 4:
            score[survey[i][-1]] += abs(scr-4)
        else:
            score[survey[i][0]] += abs(scr-4)
    
    for i in range(4):
        if score[mbti[i][0]] < score[mbti[i][-1]]:
            answer += mbti[i][-1]
        elif score[mbti[i][0]] >= score[mbti[i][-1]]:
            answer += mbti[i][0]
        
    
    return answer