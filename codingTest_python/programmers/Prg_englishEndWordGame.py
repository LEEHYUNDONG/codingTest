def solution(n, words):
    answer = []
    p, turn = 1, 1
    ans = set()
    ans.add((words[0]))
    flag = False

    for i in range(1, len(words)):
        if i % n == 0:
            turn += 1
        p = (i % n)+1
        answer = [p, turn]
        if (words[i]) in ans or (words[i][0] != words[i-1][-1]):
            flag = True
            break
        ans.add((words[i]))

    if flag:
        return answer
    else:
        return [0, 0]
