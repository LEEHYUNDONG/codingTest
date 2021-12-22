from itertools import combinations

def unique(relation, n):
    tmp =[''] * len(relation)
    for i in range(n):
        for j in range(len(relation)):
            tmp[j] += ' ' + relation[j][i]
            

 
def solution(relation):
    answer = 0
    print(len(relation))
    print(len(relation[0]))
    num = [i for i in range(len(relation[0]))]
    #for x, y in combinations(num, 2):
    #print(list(zip(*relation))[1])

 

    return answer


test = [["100","ryan","music","2"],["200","apeach","math","2"],["300","tube","computer","3"],
    ["400","con","computer","4"],["500","muzi","music","3"],["600","apeach","music","2"]]
print(solution(test))


   # for i in range(1, 3):
    #     sample = combinations(num, i)
    #     if i == 1:
    #         for j in sample:
    #             if check(list(zip(*relation))[j[0]]):
    #                 answer += 1
    #     if i == 2:
    #         for j in sample:
    #             if check( list(zip(*relation))[j[0]], zip(*relation[j[1]])):
    #                 answer += 1
        