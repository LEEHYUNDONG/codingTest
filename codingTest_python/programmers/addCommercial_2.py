def solution(play_time, adv_time, logs):
    play_time = int(play_time[0:2])*3600 + \
        int(play_time[3:5])*60 + int(play_time[6:])
    adv_time = int(adv_time[0:2])*3600 + \
        int(adv_time[3:5])*60 + int(adv_time[6:])
    answer = ''
    all_time = [0 for i in range(play_time + 1)]

    # 초 단위로 재생시간과 공익광고 시간 변경

    # 사용자 log를 초단위로 변경
    for l in logs:
        start, end = l.split('-')
        hh1, mm1, ss1 = start.split(':')
        hh2, mm2, ss2 = end.split(':')
        dur1, dur2 = int(hh1)*3600 + int(mm1)*60 + \
            int(ss1), int(hh2)*3600 + int(mm2)*60 + int(ss2)
        all_time[dur1] += 1
        all_time[dur2] -= 1

    for i in range(1, len(all_time)):       # 3
        all_time[i] = all_time[i] + all_time[i - 1]

    for i in range(1, len(all_time)):       # 4
        all_time[i] = all_time[i] + all_time[i - 1]

    most_view = 0                           # 5
    duration = 0
    for i in range(adv_time - 1, play_time):
        if i >= adv_time:
            if most_view < all_time[i] - all_time[i - adv_time]:
                most_view = all_time[i] - all_time[i - adv_time]
                duration = i - adv_time + 1
        else:
            if most_view < all_time[i]:
                most_view = all_time[i]
                duration = i - adv_time + 1

    print(duration)

    hour = '0' + \
        str(duration//3600) if duration//3600 < 10 else str(duration//3600)
    duration = duration % 3600
    mins = '0' + str(duration//60) if duration//60 < 10 else str(duration//60)
    duration = duration % 60
    secs = '0' + str(duration) if duration < 10 else str(duration)

    return hour + ':' + mins + ':' + secs
