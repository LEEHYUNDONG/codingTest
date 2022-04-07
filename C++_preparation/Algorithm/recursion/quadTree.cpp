#include <bits/stdc++.h>
using namespace std;

string ans;
string graph[128];

void project(int x, int y, int size)
{
    int cnt[2] = {0};
    int tmp;

    for (int i = x; i < x + size; i++)
    {
        for (int j = y; j < y + size; j++)
        {
            if (graph[i][j] == '0')
                cnt[0]++;
            else
                cnt[1]++;
        }
    }
    if (cnt[0] == 0)
        ans += "1";
    else if (cnt[1] == 0)
        ans += "0";
    else
    {
        ans += "(";
        project(x, y, size / 2);
        project(x, y + size / 2, size / 2);
        project(x + size / 2, y, size / 2);
        project(x + size / 2, y + size / 2, size / 2);
        ans += ")";
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
        cin >> graph[i];

    project(0, 0, N);
    cout << ans;

    return 0;
}