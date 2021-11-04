#include <vector>
#include <iostream>

using namespace std;
int dx[4] = {0, 0, 1, -1};
int dy[4] = {1, -1, 0, 0};
bool visited[101][101] = {false};
int ans = 10000;

void dfs(vector<vector<int> > maps, int n, int m, int x, int y, int depth)
{
    if (visited[x][y])
        return;
    if (x == n - 1 && y == m - 1)
    {
        ans = min(depth, ans);
        return;
    }
    visited[x][y] = true;
    for (int i = 0; i < 4; i++)
    {
        int rx = dx[i] + x, ry = dy[i] + y;
        if ((0 <= rx && rx < n && 0 <= ry && ry < m) && maps[rx][ry] == 1)
            dfs(maps, n, m, rx, ry, depth + 1);
    }
}
int solution(vector<vector<int> > maps)
{
    dfs(maps, maps.size(), maps[0].size(), 0, 0, 1);
    int answer = ans;
    if (answer == 10000)
        return -1;
    else
        return answer;
}