# def solution(s):
#     answer = ''
#     flag = True
#     for i in range(len(s)):
#         if flag:  # 첫 번째 문자일때
#             if s[i].isalpha():  # 알파벳
#                 answer += s[i].upper()
#             else:  # 숫자나 공백
#                 answer += s[i]
#             flag = False
#         elif not flag:  # 첫 번째 문자이지 않을 때
#             if s[i].isalpha():  # 알파벳의 경우 소문자로 다 돌려놔~
#                 answer += s[i].lower()
#                 continue
#             elif s[i] == ' ':
#                 flag = True
#                 answer += s[i]
#             else:
#                 answer += s[i]

#     return answer

def solution(s):
    answer = []
    flag = True
    for i in s.split(' '):
        answer.append(i.capitalize())

    answer[-1].rstrip()
    return ' '.join(answer)