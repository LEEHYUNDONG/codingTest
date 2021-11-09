#include <iostream>
#include <vector>
#include <memory.h>
#include <algorithm>

using namespace std;

char graph[25][25];
bool visited[25][25];
int dx[4] = {1, -1, 0, 0};
int dy[4] = {0, 0, -1, 1};
int cnt = 0;

int dfs(int i, int j, int n)
{
    for (int k = 0; k < 4; k++)
    {
        int rx = dx[k] + i, ry = dy[k] + j;
        if (rx >= 0 && rx < n && ry >= 0 && ry < n && !visited[rx][ry] && graph[rx][ry] == '1')
        {
            visited[rx][ry] = true;
            dfs(rx, ry, n);
            cnt++;
        }
    }
    return 1;
}
int main()
{
    int ans = 0, n;
    vector<int> answer;
    cin >> n;
    memset(visited, false, sizeof(visited));

    for (int i = 0; i < n; i++)
    {
        for (int j = 0; j < n; j++)
        {
            cin >> graph[i][j];
        }
    }

    for (int i = 0; i < n; i++)
    {
        for (int j = 0; j < n; j++)
        {
            if (!visited[i][j] && graph[i][j] == '1')
            {
                visited[i][j] = true;
                cnt = 1;
                ans += dfs(i, j, n);
                answer.push_back(cnt);
            }
        }
    }
    sort(answer.begin(), answer.end());
    cout << ans << endl;
    for (auto a : answer)
        cout << a << endl;
    return 0;
}