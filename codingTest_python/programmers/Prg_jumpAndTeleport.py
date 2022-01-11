# def solution(n):
#     ans = 0
#     dp = [0]*(n+1)
#     dp[1] = 1

#     for i in range(2, n+1):
#         dp[i] = min(dp[i//2] + (i % 2), dp[i-1]+1)

#     return dp[n]
# 처음에 dp로 풀다가 효율서에서 시간 초과와 메모리 초과가 뜸
# 생각해보니 10억 크기의 데이터가 들어올 수도 있기 때문이다.
# 그래서 아래와 같이 while문으로 dp식을 풀었더니 풀렸다.

def solution(n):
    ans = 0
    tmp = n
    while n:
        if n % 2 == 0:
            n /= 2
        else:
            ans += 1
            n -= 1
    return ans

# 순간이동을 하려면 한칸은 무조건 앞으로 가야한다. 그렇게 되면 2를 곱할 수 있게되는데,
# 탑다운 방식으로 푸니 1을 더하는게 아니라 빼줌 근데 건전지 1만큼 사용한거니까 ans+1을 해줌
# 그리고 나누어 떨어지면 2로 계속 나눠줄 수 있고 그외에는 나누어 떨어지는 수로 바꿔주고
# 그것을 반복하면 답을 구할 수 있다.