# from collections import Counter


# def solution(numbers):
#     answer = []
#     for i in numbers:
#         for j in range(i+1, 2*i+1):
#             if bin((j ^ i)).count('1') <= 2:
#                 answer.append(j)
#                 break

#     return answer

def solution(numbers):
    answer = []

    for number in numbers:
        bin_number = list('0' + bin(number)[2:])
        idx = ''.join(bin_number).rfind('0')
        bin_number[idx] = '1'

        if number % 2 == 1:
            bin_number[idx+1] = '0'

        answer.append(int(''.join(bin_number), 2))

    return answer
# 1) 짝수의 경우
# 만약, 4라면 이진수로 100 입니다. 4보다 크면서 2개 이하로 다른 수를 찾으면 101 입니다.
# 즉, 가장 뒤에 있는 0을 1로 바꿔주면 됩니다.

# 2) 홀수의 경우
# 만약, 7이라면 이진수로 0111 (바꿀때 편의를 위해 앞에 0을 붙입니다)
# 먼저 짝수의 경우처럼 가장 뒤에 있는 0의 인덱스(idx)를 찾아 1로 바꿉니다. 그럼 1111 이 됩니다.
# bin_number[idx] = '1'
# 그런 다음 idx+1 의 인덱스 값을 0으로 바꿉니다. 그럼 1011이 되고 답이 됩니다.
# bin_number[idx+1] = '0'
