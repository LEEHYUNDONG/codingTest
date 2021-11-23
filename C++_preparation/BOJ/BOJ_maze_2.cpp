#include <iostream>
#include <queue>

using namespace std;

int main()
{
    queue<pair<pair<int, int>, int> > q;
    string graph[101];
    int direction[4][2] = {{0, 1}, {0, -1}, {1, 0}, {-1, 0}};
    int n, m;

    cin >> n >> m;
    for (int i = 0; i < n; i++)
        cin >> graph[i];

    q.push(make_pair(make_pair(0, 0), 1));
    graph[0][0] = '0';
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
            int rx = direction[i][0] + x;
            int ry = direction[i][1] + y;
            if (rx < 0 || rx >= n || ry < 0 || ry >= m)
                continue;
            if (graph[rx][ry] == '0')
                continue;
            q.push({{rx, ry}, c + 1});
            graph[rx][ry] = '0';
        }
    }
    return 0;
}