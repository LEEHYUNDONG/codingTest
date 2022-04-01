def solution(p):
    answer = ''

    def check(s):
        tmp = []
        for i in s:
            if i == '(':
                tmp.append(i)
                continue
            if len(tmp) == 0 and i == ')':
                return False
            if i == ')' and tmp[-1] == '(':
                tmp.pop()
        if len(tmp) == 0:
            return True
        return False

    def makeCorrect(w):
        if w == '':
            return ''
        u, v = '', ''
        cnt = 0
        for i in range(len(w)):
            if w[i] == '(':
                cnt += 1
            elif w[i] == ')':
                cnt -= 1
            if cnt == 0:
                u += w[:i+1]
                v += w[i+1:]
                break

        if check(u):  # u가 올바른 문자열
            return u + makeCorrect(v)
        else:  # u가 올바르지 않은 문자열
            tmp = '(' + makeCorrect(v) + ')'

            ttmp = ''
            for i in range(1, len(u)-1):
                if u[i] == '(':
                    ttmp += ')'
                else:
                    ttmp += '('

            tmp += ttmp
            return tmp

    answer = makeCorrect(p)

    return answer
