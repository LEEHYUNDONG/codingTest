def solution(n, t, m, timetable):
    shuttle = 0
    timet = []
    for i in timetable:
        hh, mm = i.split(':')
        timet.append(int(hh)*60 + int(mm))
    
    timet.sort()
    people = 0
    bus = [9*60 + t*i for i in range(n)]
        
    for ttime in bus:
        cnt = 0 # 버스에 타는 크루 수 
        while cnt < m and people < len(timet) and timet[people] <= ttime: 
            people += 1 
            cnt += 1 
            # 버스에 자리가 남았을 경우 
        if cnt < m:
            # 버스에 자리가 없는 경우 맨 마지막 크루보다 1분 먼저 도착 
        else: 
            shuttle = timet[people - 1] - 1 
                
    # 출력하는 부분
    if shuttle // 60 >= 10 and shuttle % 60 >= 10:
        return str(shuttle//60) + ':' + str(shuttle%60)
    elif shuttle // 60 >= 10 and shuttle % 60 <= 10:
        return str(shuttle//60) + ':' + '0' + str(shuttle%60)
    elif shuttle // 60 <= 10 and shuttle % 60 >= 10:
        return '0'+str(shuttle//60) + ':' + str(shuttle%60)
    else:
        return '0'+str(shuttle//60) + ':' + '0'+ str(shuttle%60)