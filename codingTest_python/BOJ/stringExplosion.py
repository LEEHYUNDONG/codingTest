s1 = input()
tar = input()

def explode(s, tar):
    st = []
    for i in range(len(s)):
        st.append(s[i])
        if len(st) >= len(tar):
            tmp = ''.join(st[-len(tar):])
            if tmp == tar:
                length = 0
                while length < len(tar):
                    st.pop()
                    length += 1
    if len(st) == 0:
        return "FRULA"
    else:
        return ''.join(st)
    

print(explode(s1, tar))