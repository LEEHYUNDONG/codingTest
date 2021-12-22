from collections import deque

def solution(record):
    answer = []
    name = dict()
    q = deque([])
    
    for i in range(len(record)):
        tmp = record[i].split(' ')
        if tmp[0] == 'Enter':
            q.append([tmp[1], 1])
            name[tmp[1]] = tmp[2]
        if tmp[0] == 'Leave':
            q.append([tmp[1], 2])
        if tmp[0] == 'Change':
            name[tmp[1]] = tmp[2]

    for i in range(len(q)):
        x, y = q.popleft()
        if y == 1:
            answer.append(name[x]+'님이 들어왔습니다.')
        if y == 2:
            answer.append(name[x]+'님이 나갔습니다.')

    return answer

test = ["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234",
        "Enter uid1234 Prodo","Change uid4567 Ryan"]
print(solution(test))