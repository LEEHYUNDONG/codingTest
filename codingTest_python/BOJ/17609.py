import sys
input = sys.stdin.readline

N = int(input())

def check(word):
    l, r = 0, len(word)-1
    flag = False
    
    while l <= r:
        
        if word[l] == word[r]:
            l += 1
            r -= 1
        else:
            if word[l+1] == word[r] and word[l+2] == word[r-1] and not flag:
                l += 2
                r -= 1  
            elif word[l] == word[r-1] and  word[l+1] == word[r-2] and not flag:
                r -= 2
                l += 1
            else:
                return 2
            flag = True
    if flag:
        return 1
    return 0
# 4
# abcddadca
# aabcbcaa
# ababbabaa
# abca
test = [input().rstrip() for _ in range(N)]

for t in test:
    print(check(t))
        
        
