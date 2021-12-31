import sys
input = sys.stdin.readline

n = int(input())
st = []
cur = 1
ans = []
flag = True

for i in range(n):
    num = int(input())
    while cur <= num:
        st.append(cur)
        cur += 1
        ans.append('+')
    if st[-1] == num:
        st.pop()
        ans.append('-')
    else:
        print("NO")
        flag = False
        break

if flag:
    for i in ans:
        print(i)
