#include <iostream>
#include <vector>
#include <queue>
#include <memory.h>

using namespace std;

int visited[1001][1001];
int dist[1001][1001];

int main()
{
    int n, m;
    cin >> n >> m;
    int dx[4] = {0, 0, -1, 1};
    int dy[4] = {1, -1, 0, 0};
    queue<pair<pair<int, int>, int> > q;
    memset(visited, 0, sizeof(visited));
    memset(dist, 1000001, sizeof(dist));

    vector<string> map(n);
    for (int i = 0; i < n; i++)
    {
        cin >> map[i];
    }

    visited[0][0] = 1;
    q.push({{0, 0}, 1});
    dist[0][0] = 1;

    while (!q.empty())
    {
        int x = q.front().first.first, y = q.front().first.second;
        int block = q.front().second;
        q.pop();
        if (x == n - 1 && y == m - 1)
        {
            cout << dist[n - 1][m - 1] << endl;
            return 0;
        }
        for (int i = 0; i < 4; i++)
        {
            int rx = x + dx[i], ry = y + dy[i];
            if (rx < 0 || rx >= n || ry < 0 || ry >= m)
                continue;
            if (map[rx][ry] == '1' && block)
            {

                q.push({{rx, ry}, 0});
                visited[rx][ry] = 1;
                dist[rx][ry] = dist[x][y] + 1;
            }
            if (map[rx][ry] == '0' && visited[rx][ry] == 0)
            {
                q.push({{rx, ry}, 0});
                visited[rx][ry] = 1;
                dist[rx][ry] = dist[x][y] + 1;
            }
        }
    }

    cout << -1 << '\n';
    return 0;
}