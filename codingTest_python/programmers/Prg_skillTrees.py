def solution(skill, skill_trees):
    answer = 0
    for i in range(len(skill_trees)):
        skill_trees[i] = list(skill_trees[i])

    for i in range(len(skill_trees)):
        for j in range(len(skill_trees[i])):
            if skill_trees[i][j] not in skill:
                skill_trees[i][j] = ''
        skill_trees[i] = ''.join(skill_trees[i])

        if skill_trees[i] == skill[:len(skill_trees[i])]:
            answer += 1

    return answer

## 다른 사람 코드

# def solution(skill, skill_trees):
#     answer = 0

#     for skills in skill_trees:
#         skill_list = list(skill)

#         for s in skills:
#             if s in skill:
#                 if s != skill_list.pop(0):
#                     break
#         else:
#             answer += 1

#     return answer
