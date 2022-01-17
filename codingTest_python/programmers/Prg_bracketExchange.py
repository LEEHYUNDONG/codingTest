from collections import deque


def isBracket(s):
    st = []
    for i in s:
        if i == '(' or i == '{' or i == '[':
            st.append(i)
        else:
            if st and i == ')' and st[-1] == '(':
                st.pop()
            elif st and i == ']' and st[-1] == '[':
                st.pop()
            elif st and i == '}' and st[-1] == '{':
                st.pop()
            else:
                return False
    if len(st) > 0:
        return False
    return True


def solution(s):
    answer = 0
    sq = deque(list(s))
    for i in range(len(s)):
        if isBracket(''.join(sq)):
            answer += 1
        sq.rotate(-1)

    return answer
