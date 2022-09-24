from itertools import product

def solution(users, emoticons):
    answer = []
    discountRate = [0.6, 0.7, 0.8, 0.9] # 40%, 30%, 20%, 10%
    

    for comb in product(discountRate, repeat = len(emoticons)):
        comb = list(comb)
        
        serv, profit = 0, 0
        # emoji 비용 및 비율 
        emojiCost = []
        for i in range(len(emoticons)):
            emojiCost.append([(round(1-comb[i], 1))*100, round(emoticons[i]*comb[i], 1)])
        
        # user가 emoji를 구매
        for user in users:
            userRate, userLimit = user
            userProfit = 0
            service = False # flag for service
            for rate, cost in emojiCost:
                if rate < userRate:
                    continue
                userProfit += cost
                
            # 수익 계산
            profit += userProfit
            if userLimit <= userProfit:
                serv += 1
                profit -= userProfit
        
        answer.append([serv, profit])
                
    answer.sort(key = lambda x:(x[0], x[1]))
    
    

    return answer[-1]