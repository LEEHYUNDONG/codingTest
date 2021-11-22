#include <iostream>
#include <queue>

using namespace std;

int main()
{
    ios::sync_with_stdio(false);
    cin.tie(0);
    cout.tie(0);

    queue<pair<pair<int, int>, int> > q;
    string graph[101];
    int dire[4][2] = {{0, 1}, {0, -1}, {-1, 0}, {1, 0}};

    q.push(make_pair(make_pair(0, 0), 1));
    graph[0][0] = 0;
    int n, m;
    cin >> n >> m;

    for (int i = 0; i < n; i++)
        cin >> graph[i];

    while (!q.empty())
    {
        int x = q.front().first.first;
        int y = q.front().first.second;
        int c = q.front().second;
        q.pop();
        if (x == n - 1 && y == m - 1)
        {
            cout << c << '\n';
            break;
        }
        for (int i = 0; i < 4; i++)
        {
            int rx = dire[i][0] + x;
            int ry = dire[i][1] + y;
            if (rx < 0 || rx >= n || ry < 0 || ry >= m)
                continue;
            if (graph[rx][ry] == '0')
                continue;
            q.push(make_pair(make_pair(rx, ry), c + 1));
            graph[rx][ry] = '0';
        }
    }
    return 0;
}