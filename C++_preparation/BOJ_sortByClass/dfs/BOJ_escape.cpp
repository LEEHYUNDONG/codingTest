#include <iostream>
#include <queue>

using namespace std;

char graph[51][51];
bool visited[51][51] = {false};

int main()
{
    int n, m;
    int startx, starty;
    int destx, desty;
    queue<pair<int, int>> water;
    queue<pair<pair<int, int>, int>> q;
    int direction[4][2] = {
        {-1, 0},
        {1, 0},
        {0, -1},
        {0, 1}};
    bool flag = true;
    cin >> n >> m;
    for (int i = 0; i < n; i++)
    {
        for (int j = 0; j < m; j++)
        {
            cin >> graph[i][j];
            if (graph[i][j] == 'S')
            {
                startx = i;
                starty = j;
            }
            else if (graph[i][j] == '*')
            {
                water.push(make_pair(i, j));
                visited[i][j] = true;
            }
        }
    }

    visited[startx][starty] = true;
    q.push(make_pair(make_pair(startx, starty), 0));
    while (!q.empty())
    {
        int x = q.front().first.first;
        int y = q.front().first.second;
        int c = q.front().second;
        q.pop();
        if (graph[x][y] == 'D')
        {
            cout << c << '\n';
            flag = false;
            break;
        }
        for (int i = 0; i < 4; i++)
        {
            int dx = direction[i][0] + x;
            int dy = direction[i][1] + y;
            if (dx < 0 || dx >= n || dy < 0 || dy >= m)
                continue;
            if (visited[dx][dy] || graph[dx][dy] == '*')
                continue;
            if (graph[dx][dy] == 'D')
            {
                cout << c + 1 << '\n';
                flag = false;
                break;
            }
            else if (graph[dx][dy] == '.')
            {
                q.push({{dx, dy}, c + 1});
                visited[dx][dy] = true;
            }
        }
        if (!flag)
            break;
        int wa = water.size();
        for (int j = 0; j < wa; j++)
        {
            int wx = water.front().first;
            int wy = water.front().second;
            water.pop();
            for (int i = 0; i < 4; i++)
            {
                int rx = wx + direction[i][0];
                int ry = wy + direction[i][1];
                if (rx < 0 || rx >= n || ry < 0 || ry >= m)
                    continue;
                if (graph[rx][ry] == '.')
                {
                    water.push({rx, ry});
                    visited[rx][ry] = true;
                    graph[rx][ry] = '*';
                }
            }
        }
    }
    if (flag)
        cout << "KAKTUS\n";
    return 0;
}