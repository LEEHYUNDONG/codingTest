def solution(stack1, stack2, stack3):
    l = len(stack1) + len(stack2) + len(stack3)
    answer = ""
    stack = [stack1, stack2, stack3]
    tmp = []
    
    while stack[0] and stack[1] and stack[2]:
        tmp = [stack[0][-1], stack[1][-1], stack[2][-1]]
        maxV = max(tmp)
        idx = tmp.index(maxV)
        stack[idx].pop()        
        idx += 1
        answer += str(idx)

    while stack[0] and stack[1]:
        tmp = [stack[0], stack[1]]
        maxV = max(tmp)
        idx = tmp.index(maxV)     
        if idx == 0:
            stack[0].pop()   
            answer += '1'
        elif idx == 1:
            stack[1].pop()   
            answer += '2'

    while stack[0] and stack[2]:
        tmp = [stack[0], stack[2]]
        maxV = max(tmp)
        idx = tmp.index(maxV)
        
        if idx == 0:
            stack[0].pop()   
            answer += '1'
        elif idx == 1:
            stack[2].pop()   
            answer += '3'
    
    while stack[1] and stack[2]:
        tmp = [stack[1], stack[2]]
        maxV = max(tmp)
        idx = tmp.index(maxV)
        
        if idx == 0:
            stack[1].pop()   
            answer += '2'
        elif idx == 1:
            stack[2].pop()   
            answer += '3'
    
    while stack[0]:
        answer += '1'
        stack[0].pop()   
    while stack[1]:
        answer += '2'
        stack[1].pop()   
    while stack[2]:
        answer += '3'
        stack[2].pop()

    return answer
        

            
