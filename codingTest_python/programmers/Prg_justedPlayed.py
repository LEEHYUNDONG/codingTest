def translate_mel(played):
    return played.replace('C#', 'c').replace('E#', 'e').replace('G#', 'g').replace('F#', 'f').replace('D#', 'd').replace('A#', 'a')


def solution(m, musicinfos):
    answer = []
    melm = {'C#': 'c', 'D#': 'd', 'E#': 'e', 'F#': 'f', 'G#': 'g', 'A#': 'a'}
    for i in musicinfos:
        info = i.split(',')
        start_time, end_time = int(
            info[0][:2])*60 + int(info[0][3:]), int(info[1][:2])*60 + int(info[1][3:])
        mm, song, duration = info[3], info[2], end_time-start_time
        played = ''
        mm = translate_mel(mm)
        if len(mm) >= duration:
            played = mm[:duration]
        else:
            played = mm * (duration // len(mm)) + mm[:(duration % len(mm))]
        ml = played
        m = translate_mel(m)

        if m in ml:
            answer.append([song, duration])
    if len(answer):
        answer = sorted(answer, key=lambda x: x[1], reverse=True)
        return answer[0][0]

    return "(None)"
