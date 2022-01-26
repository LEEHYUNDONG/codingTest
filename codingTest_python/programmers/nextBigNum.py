def solution(n):
    answer = 0
    numOfOne = list(str(bin(n)[2:])).count('1')

    for i in range(n+1, n*n):
        if bin(i)[2:].count('1') == numOfOne:
            return i
