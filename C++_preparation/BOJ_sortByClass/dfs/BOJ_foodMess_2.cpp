#include <iostream>
#include <vector>
#include <algorithm>
#include <cassert>

using namespace std;

#define INT32_MAX 2147483647

bool tabemono[110][110];
bool visited[110][110];

int dx[4] = {-1, 0, 1, 0};
int dy[4] = {0, -1, 0, 1};
int dfs(int x, int y)
{
    if (visited[x][y] || !tabemono[x][y])
        return 0;
    visited[x][y] = true;
    int ans = 1;
    for (int i = 0; i < 4; i++)
    {
        ans += dfs(x + dx[i], y + dy[i]);
    }
    return ans;
}
int main()
{
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int n, m, k;
    cin >> n >> m >> k;
    while (k--)
    {
        int x, y;
        cin >> x >> y;
        tabemono[x][y] = true;
    }
    int ans = 0;
    for (int i = 1; i <= n; i++)
    {
        for (int j = 1; j <= m; j++)
        {
            ans = max(ans, dfs(i, j));
        }
    }
    cout << ans << endl;
}