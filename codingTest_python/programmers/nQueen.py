def solution(n):
    row = [0] * n

    def promising(x):
        for i in range(x):
            if row[x] == row[i]:
                return False
            if abs(row[x] - row[i]) == abs(x - i):
                return False
        return True

    def nQueens(x):
        answer = 0
        if x == n:
            return 1
        else:
            for i in range(n):
                row[x] = i
                if promising(x):
                    answer += nQueens(x+1)
        return answer

    answer = nQueens(0)
    return answer
