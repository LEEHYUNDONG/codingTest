import sys
sys.setrecursionlimit(10**6)
answer = 0
tmp = 0


def solution(numbers, target):

    def dfs(numbers, idx, tot, target):
        global answer

        if idx == len(numbers) and tot == target:

            answer += 1
            return

        if idx < len(numbers):
            dfs(numbers, idx+1, tot+numbers[idx], target)
            dfs(numbers, idx+1, tot-numbers[idx], target)

        return

    dfs(numbers, 0, 0, target)

    return answer
