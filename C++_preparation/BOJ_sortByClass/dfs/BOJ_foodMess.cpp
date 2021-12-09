#include <iostream>
#include <queue>
#include <algorithm>

using namespace std;

int n, m, k;
char graph[101][101];
bool visited[101][101] = {false};
int ans = 0;
int direction[4][2] = {
    {1, 0},
    {-1, 0},
    {0, 1},
    {0, -1}};

void dfs(int x, int y, int depth)
{
    if (x < 0 || x >= n || y < 0 || y >= m)
        return;
    if (ans < depth)
        ans = depth;
    if (graph[x][y] == '.' || visited[x][y])
        return;
    visited[x][y] = true;
    for (int i = 0; i < 4; i++)
    {
        dfs(x + direction[i][0], y + direction[i][1], depth + 1);
    }
    return;
}
int main()
{
    cin >> n >> m >> k;
    queue<pair<int, int>> q;
    for (int i = 0; i < n; i++)
    {
        for (int j = 0; j < m; j++)
        {
            graph[i][j] = '.';
        }
    }
    int r, c;
    for (int i = 0; i < k; i++)
    {
        cin >> r >> c;
        graph[r - 1][c - 1] = '#';
        q.push(make_pair(r - 1, c - 1));
    }

    while (!q.empty())
    {
        int x = q.front().first;
        int y = q.front().second;
        q.pop();
        if (!visited[x][y])
            dfs(x, y, 1);
    }

    cout << ans << '\n';
    return 0;
}