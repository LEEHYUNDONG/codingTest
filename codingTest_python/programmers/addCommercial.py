def solution(play_time, adv_time, logs):
    answer = ''
    user_logs = []

    # 초 단위로 재생시간과 공익광고 시간 변경
    play_time = int(play_time[0:2])*3600 + \
        int(play_time[3:5])*60 + int(play_time[6:])
    adv_time = int(adv_time[0:2])*3600 + \
        int(adv_time[3:5])*60 + int(adv_time[6:])

    # 사용자 log를 초단위로 변경
    for l in logs:
        start, end = l.split('-')
        hh1, mm1, ss1 = start.split(':')
        hh2, mm2, ss2 = end.split(':')
        dur1, dur2 = int(hh1)*3600 + int(mm1)*60 + \
            int(ss1), int(hh2)*3600 + int(mm2)*60 + int(ss2)
        user_logs.append([dur1, dur2])

    user_logs.sort(key=lambda x: x[0])

    ans = 0  # 광고 시작 시간
    duration = 0  # 광고 누적시간 최대값

    for i in range(len(user_logs)):
        end_time = user_logs[i][0] + adv_time  # 광고 길이에 따른 끝 시간
        tmp = 0  # 광고 누적 광고 시간 계산
        for j in range(i, len(user_logs)):
            # 기준이 되는 시작 시간의 끝시간 보다 다른 사용자의 시작시간이 해당 구간에 들어있지 않으면 나가
            if end_time <= user_logs[j][0]:
                break
            elif user_logs[j][0] <= end_time <= user_logs[j][1]:
                tmp += (end_time - user_logs[j][0])
            elif user_logs[j][1] < end_time and user_logs[i][0] <= user_logs[j][1]:
                tmp += (user_logs[j][1]-user_logs[i][0])

        if tmp > duration:
            ans = user_logs[i][0]
            duration = tmp

        hour = '0' + str(ans//3600) if ans//3600 < 10 else str(ans//3600)
        ans = ans % 3600
        mins = '0' + str(ans//60) if ans//60 < 10 else str(ans//60)
        ans = ans % 60
        secs = '0' + str(ans) if ans < 10 else str(ans)

        return hour + ':' + mins + ':' + secs
