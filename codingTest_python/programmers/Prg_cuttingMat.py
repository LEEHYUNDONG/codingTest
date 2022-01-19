def solution(n, left, right):
    answer = []
    for i in range(left, right+1):
        # num = (i%n)+1
        # if i % n == 0 and i // n != 0:
        #     num += i//n
        answer.append(max(i//n, i % n) + 1)

    return answer
