#include <bits/stdc++.h>
using namespace std;

const int maxN = 130;
int graph[maxN][maxN];
int blue = 0, white = 0;

void countingP(int x, int y, int size)
{
    int cnt[2] = {0, 0}; // 0 - 흰색, 1 - 파란색
    for (int i = x; i < x + size; i++)
    {
        for (int j = y; j < y + size; j++)
        {
            cnt[graph[i][j]]++;
        }
    }
    if (cnt[0] == 0)
        blue++;
    else if (cnt[1] == 0)
        white++;
    else
    {
        countingP(x, y, size / 2);
        countingP(x, y + size / 2, size / 2);
        countingP(x + size / 2, y, size / 2);
        countingP(x + size / 2, y + size / 2, size / 2);
    }
    return;
}
int main()
{

    ios::sync_with_stdio(0);
    cin.tie(0);
    int N;
    cin >> N;
    for (int i = 0; i < N; i++)
    {
        for (int j = 0; j < N; j++)
        {
            cin >> graph[i][j];
        }
    }

    countingP(0, 0, N);
    cout << white << "\n";
    cout << blue;

    return 0;
}