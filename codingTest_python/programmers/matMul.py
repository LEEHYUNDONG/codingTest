def solution(arr1, arr2):
    answer = [[0] * len(arr2[0]) for _ in range(len(arr1))]

    for i in range(len(arr1)):  # arr1 의 행단위
        for j in range(len(arr2)):  # arr1의 열단위, arr2으ㅣ 행단위
            for k in range(len(arr2[0])):
                answer[i][k] += arr1[i][j] * arr2[j][k]

    return answer
