def solution(id_list, k):
    answer = 0
    coupon_cust = dict()

    for custLst in id_list:
        # 고객당 하루에 최대 1장의 할인 쿠폰
        cust_set = set(custLst.split(' '))
        for cust in cust_set:
            if cust not in coupon_cust:
                coupon_cust[cust] = 0
            coupon_cust[cust] += 1
    
    for cust in coupon_cust.keys():
        if coupon_cust[cust] >= k:
            answer += k
        else:
            answer += coupon_cust[cust]
        


    return answer

["A A A A A A", "A A A A A A", "A A A A A A", "A B", "A A A A A A", "AA A A A A A"]
