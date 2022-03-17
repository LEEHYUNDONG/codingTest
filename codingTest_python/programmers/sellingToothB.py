from collections import deque
def solution(enroll, referral, seller, amount):
    
    answer = []
    enrollDic = dict()
    graph = dict()
    n = len(referral)
    
    amount = [i*100 for i in amount]

    for i in range(len(enroll)):
        enrollDic[enroll[i]] = []
        if enroll[i] not in graph.keys():
            graph[enroll[i]] = []
            graph[enroll[i]].append(referral[i])
            continue
        graph[enroll[i]].append(referral[i])
    
    
    for i in range(len(seller)):
        q = seller[i]
        tmp = amount[i]
        enrollDic[q].append(tmp)
        
        while q != '-':
            tmp = tmp // 10
            if tmp == 0:
                break
            if tmp < 1:
                enrollDic[q].append(tmp)
            else:
                if graph[q][0] != '-':
                    enrollDic[graph[q][0]].append(tmp)
            q = graph[q][0]
    
    ans = []
    for i in enrollDic.keys():
        tmp = 0
        for j in range(len(enrollDic[i])):
            tmp += enrollDic[i][j] - (enrollDic[i][j]//10)
        ans.append(tmp)
    
    
    return ans