#include <iostream>

using namespace std;
int dp[300];

int main()
{
    int data[300] = {0};
    int n;
    cin >> n;
    for (int i = 0; i < n; i++)
        cin >> data[i];
    dp[0] = data[0];
    dp[1] = max(data[1], data[0] + data[1]);
    dp[2] = max(dp[0] + data[2], data[1] + data[2]);

    for (int i = 3; i < n; i++)
    {
        dp[i] = max(dp[i - 3] + data[i] + data[i - 1], dp[i - 2] + data[i]);
    }
    return 0;
}