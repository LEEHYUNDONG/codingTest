#include <bits/stdc++.h>
using namespace std;
#define MOD 1000000000

//정수 0부터 N까지 K개 더해서 합이 N이 되는 경우의 수
int N, K;
int dp[201]; // [N][K]

int main()
{
    ios::sync_with_stdio(0);
    cin.tie(0);

    cin >> N >> K;

    fill(&dp[0], &dp[200], 0);
    dp[0] = 1;
    
    for (int i = 1; i <= K; i++)
    {
        for (int j = 1; j <= N;j++){
            dp[j] = (dp[j] + dp[j - 1]) % MOD;
        }
    }

    cout << dp[N];

    return 0;
}