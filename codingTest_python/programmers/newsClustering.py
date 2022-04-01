def solution(str1, str2):
    answer = 0
    multi = 65536

    def findString(s):  # 문자열 찾기
        tmp = []
        for i in range(0, len(s)-1):
            stmp = s[i:i+2]
            if stmp.isalpha():
                tmp.append(s[i:i+2].upper())
        return tmp

    def makeDict(s):
        tmp = dict()
        for i in s:
            if i not in tmp.keys():
                tmp[i] = 1
                continue
            tmp[i] += 1
        return tmp

    s1 = findString(str1)
    s2 = findString(str2)

    if len(s1) == 0 and len(s2) == 0:
        return 1*multi

    s1Dict = makeDict(s1)
    s2Dict = makeDict(s2)

    uni = 0
    sec = 0
    for i in s1Dict.keys():

        if i in s2Dict.keys():
            sec += min(s1Dict[i], s2Dict[i])
            uni += max(s1Dict[i], s2Dict[i])
        else:
            uni += s1Dict[i]

    for i in s2Dict.keys():
        if i not in s1Dict.keys():
            uni += s2Dict[i]

    return int(sec/uni*multi)
