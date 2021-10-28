#include <iostream>
#define MAXN 100000000
using namespace std;

long long solution(int w, int h)
{
    long long answer = 1;
    long long dp[10000][10000] = {0};

    for (int i = 1; i <= h; i++)
    {
        for (int j = 0; j <= w; j++)
        {
            if (i == j)
            {
                dp[i][j] = i;
            }
        }
    }
    for (int i = 1; i <= w; i++)
    {
        dp[1][i] = i;
    }
    for (int j = 1; j <= h; j++)
    {
        dp[j][1] = j;
    }
    dp[2][1] = 2;
    dp[1][2] = 2;
    dp[3][2] = 4;
    dp[2][3] = 4;

    for (int i = 3; i <= h; i++)
    {
        for (int j = 3; j <= w; j++)
        {
            dp[i][j] = dp[i / 2][j / 2] + dp[i / 2][j / 2];
        }
    }

    answer = h * w - dp[h][w];

    return answer;
}