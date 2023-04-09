def solution(users, emoticons):
    answer = []
    rate = [10, 20, 30, 40]
    best_case = [0, 0]
    def dfs(depth, tmp):
        if depth == len(emoticons):
            tot_price, emo_plus = 0, 0 # 총금액, 이모티콘 플러스 가입자
            price = 0 # 사용자별 지불 금액
            for j in range(len(users)):
            # 유저 별 이모티콘 계산
                price = 0
                for k, emo in enumerate(emoticons):
                    
                    if tmp[k] >= users[j][0]:
                        price += emo*((100- tmp[k])/100)
                    else:
                        continue
                if price >= users[j][-1]:
                    emo_plus += 1
                else:
                    tot_price += price

            if best_case[0] < emo_plus or best_case[0] == emo_plus and best_case[-1] < tot_price:
                best_case[0] = emo_plus
                best_case[1] = tot_price
            return
        
        for i in range(4):
            tmp.append(rate[i])
            dfs(depth+1, tmp)
            tmp.pop()
    
    dfs(0, [])
            
    return best_case