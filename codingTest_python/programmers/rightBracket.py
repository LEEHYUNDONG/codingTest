def solution(s):
    answer = True
    st = []
    for i in s:
        if i == '(':
            st.append(i)
        elif len(st) > 0 and i == ')' and st[-1] == '(':
            st.pop()
        elif len(st) == 0:
            return False

    if len(st) >= 1:
        return False
    return True
