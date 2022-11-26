import datetime as dt

def check(stime):
    start = stime[0]
    for i in range(1, len(stime)):
        if stime[i] - start > 1:
            return False
        start = stime[i]
    return True

def solution(s, times):
    ss = list(map(int, s.split(':')))

    now = dt.datetime(ss[0], ss[1], ss[2], ss[3], ss[4], ss[5])
    # 저축 일자
    stime = [now.day]

    for time in times:
        dd, hh, mm, ss = list(map(int, time.split(':')))
        delta = dt.timedelta(days=dd, hours=hh, minutes=mm, seconds=ss)
        now += delta
        stime.append(now.day)
    

    stime.sort()
    print(stime)
        
    if check(stime):
        return [1, stime[-1] - stime[0]+1]

    return [0, stime[-1] - stime[0] + 1]