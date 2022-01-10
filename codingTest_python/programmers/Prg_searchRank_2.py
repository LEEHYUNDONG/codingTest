from bisect import bisect_left
from itertools import combinations


def make_cases(sep_info):
    cases = []
    # 모든 경우를 만들어 주는 함수
    for k in range(5):
        # 인덱스 0-3까지 조합을 이용해서 -가 들어가야할 인덱스를 찾고
        for condition in combinations([0, 1, 2, 3], k):
            # 해달 배열을 문자열로 바꿔 키값을 만들어서 딕셔너리 값으로 넣어준다
            case = []
            for idx in range(4):
                if idx not in condition:
                    case.append(sep_info[idx])
                else:
                    case.append('-')
                cases.append(''.join(case))
    return cases


def solution(info, query):
    answer = []
    all_people = {}
    for i in info:
        sep_info = i.split()
        cases = make_cases(sep_info)
        for case in cases:
            if case not in all_people.keys():
                all_people[case] = [int(sep_info[4])]
            else:
                all_people[case].append(int(sep_info[4]))

    for key in all_people.keys():
        all_people[key].sort()

    for q in query:
        seperate_q = q.split(' and ')
        seperate_q.extend(seperate_q.pop().split())
        print(seperate_q)
        target = ''.join(seperate_q[:4])
        # for sq in seperate_q[:4]:
        #     target += sq

        if target in all_people.keys():
            answer.append(len(all_people[target]) - bisect_left(
                all_people[target], int(seperate_q[4])))
        else:
            answer.append(0)
    return answer
