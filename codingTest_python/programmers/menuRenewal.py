from itertools import combinations
from collections import Counter


def solution(orders, course):
    answer = []
    for k in course:  # 조합 순서대로 2개, 3개 순
        candidates = []  # 각 조합별로 담아둘 후보들
        for menu in orders:  # 주문
            for listOfMenu in combinations(menu, k):  # 메뉴마다 조합
                res = ''.join(sorted(listOfMenu))
                candidates.append(res)
        
        sorted_candidates = Counter(candidates).most_common()
        answer += [menu for menu, cnt in sorted_candidates if cnt > 1 and cnt == sorted_candidates[0][1]]
    return sorted(answer)