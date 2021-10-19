from collections import deque
s = "aaaaaddfsfdaef"

index = 0
length = 0
cnt = 0
q = deque(list(s))
res = deque([])
# for i in range(len(s)-1):
#     if s[i] != s[i+1] and s[i] not in s[index:i]:
#         cnt += 1
#     elif s[i] in s[index:i+1]:
#         index = i
#         cnt = 0
#     length = max(cnt, length)

while q:
    tmp = q.popleft()
    if tmp not in res:
        res.append(tmp)
    elif tmp in res:
        # print(2)
        length = max(len(res), length)
        while tmp in res:
            res.popleft()
        res.append(tmp)

length = max(len(res), length)
print(length)


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        length = 0
        q = deque(list(s))
        res = deque([])
        while q:
            tmp = q.popleft()
            if tmp not in res:
                res.append(tmp)
            elif tmp in res:
                length = max(len(res), length)
                while tmp in res:
                    res.popleft()
                res.append(tmp)
        length = max(len(res), length)
        return length
