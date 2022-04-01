answer = int(1e9)
def solution(begin, target, words):
    global answer
    visited = [False]*len(words)
    
    def diffLen(s1, s2):
        cnt = 0
        for i in range(min(len(s1), len(s2))):
            if s1[i] != s2[i]:
                cnt += 1
        
        return cnt
    
    def dfs(start, target, depth):
        global answer

        if start == target:
            answer = min(depth, answer)
            return
        
        for i in range(len(words)):
            if diffLen(start, words[i]) == 1 and not visited[i]:
                visited[i] = True
                print(start, words[i])
                dfs(words[i], target, depth+1)
                visited[i] = False
    
    
    dfs(begin, target, 0)
    
    if answer == int(1e9):
        return 0
            
    return answer