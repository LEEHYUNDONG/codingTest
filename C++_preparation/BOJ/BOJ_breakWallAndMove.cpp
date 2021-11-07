#include <iostream>
#include <vector>
#include <queue>
#include <memory.h>

using namespace std;

int visited[1001][1001][2];
int dist[1001][1001];

int main()
{
    int n, m;
    cin >> n >> m;
    int dx[4] = {0, 0, 1, -1};
    int dy[4] = {1, -1, 0, 0};
    queue<pair<pair<int, int>, pair<int, int> > > q;

    memset(visited, 0, sizeof(visited));
    // memset(dist, 1000001, sizeof(dist));

    vector<string> map(n);
    for (int i = 0; i < n; i++)
    {
        cin >> map[i];
    }

    visited[0][0][0] = 1;
    q.push({{0, 0}, {0, 1}});

    while (!q.empty())
    {
        int x = q.front().first.first, y = q.front().first.second;
        int block = q.front().second.first;
        int cnt = q.front().second.second;
        q.pop();
        if (x == n - 1 && y == m - 1)
        {
            cout << cnt << endl;
            return 0;
        }
        for (int i = 0; i < 4; i++)
        {
            int rx = x + dx[i], ry = y + dy[i];
            if (rx < 0 || rx >= n || ry < 0 || ry >= m)
                continue;
            if (map[rx][ry] == '1' && !block)
            {
                visited[rx][ry][block + 1] = 1;
                q.push({{rx, ry}, {block + 1, cnt + 1}});
            }
            else if (map[rx][ry] == '0' && visited[rx][ry][block] == 0)
            {
                visited[rx][ry][block] = 1;
                q.push({{rx, ry}, {block, cnt + 1}});
            }
        }
    }

    cout << -1 << '\n';
    return 0;
}