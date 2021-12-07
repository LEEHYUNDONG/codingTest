#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;
int graph[101][101] = {0};

int direction[4][2] = {
    {0, -1},
    {0, 1},
    {1, 0},
    {-1, 0}};
vector<int> ans;
int tot = 0;
int d = 0;
int n, m, k;

int dfs(int x, int y, int depth)
{
    if (x < 0 || x >= n || y < 0 || y >= m || graph[x][y])
        return 0;
    d++;
    graph[x][y] = 1;
    for (int i = 0; i < 4; i++)
    {
        dfs(x + direction[i][0], y + direction[i][1], depth + 1);
    }
    return 1;
}
int main()
{
    ios::sync_with_stdio(false);
    cin.tie(0);
    cout.tie(0);

    cin >> n >> m >> k;
    for (int i = 0; i < k; i++)
    {
        int rc, cc, rrc, ccc;
        cin >> rc >> cc >> rrc >> ccc;
        for (int j = rc; j < rrc; j++)
        {
            for (int q = cc; q < ccc; q++)
            {
                graph[q][j] = 1;
            }
        }
    }

    for (int i = 0; i < n; i++)
    {
        for (int j = 0; j < m; j++)
        {
            if (graph[i][j] == 0)
            {
                tot += dfs(i, j, 0);
                ans.push_back(d);
                d = 0;
            }
        }
    }
    sort(ans.begin(), ans.end());
    cout << tot << '\n';
    for (auto a : ans)
        cout << a << " ";
    cout << '\n';

    return 0;
}