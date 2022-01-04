def solution(s):
    answer = []
    dic = dict()
    num = ""
    ln = []
    for i in range(1, len(s)-1):
        if s[i] >= '0' and s[i] <= '9':
            num += s[i]
        elif s[i] == '}':
            if num != "":
                ln.append(num)
            num = ''
        elif s[i] == ',':
            if s[i+1] != "}":
                ln.append(num)
            if s[i-1] != '}':
                num = ''

    for a in ln:
        if a != '':
            if int(a) not in dic:
                dic[int(a)] = 1
            else:
                dic[int(a)] += 1

    dic = sorted(dic.items(), reverse=True, key=lambda x: x[1])
    answer = [a for a, b in dic]

    return answer
