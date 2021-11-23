#include <iostream>

using namespace std;

int main()
{
    int n;
    int dp[50001];
    cin >> n;
    dp[1] = 1;
    for (int i = 2; i <= n; i++)
    {
        dp[i] = dp[i - 1] + 1;
        for (int j = 2; j * j <= i; j++)
        {
            dp[i] = min(dp[i - j * j] + 1, dp[i]);
        }
    }
    cout << dp[n] << '\n';
    return 0;
}