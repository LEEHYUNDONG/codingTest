#include <vector>
#include <queue>
#include <iostream>
#include <memory.h>
using namespace std;

int solution(vector<vector<int> > maps)
{
    int answer = 1000001;
    int visited[101][101];
    int dx[4] = {0, 0, 1, -1};
    int dy[4] = {1, -1, 0, 0};
    int n = maps.size(), m = maps[0].size();
    queue<pair<int, int> > dq;
    memset(visited, 1000001, sizeof(visited));
    dq.push(make_pair(0, 0));
    visited[0][0] = 1;

    while (!dq.empty())
    {
        int x = dq.front().first;
        int y = dq.front().second;
        dq.pop();
        for (int i = 0; i < 4; i++)
        {
            int rx = dx[i] + x;
            int ry = dy[i] + y;
            if (rx < 0 || ry < 0 || rx >= n || ry >= m)
                continue;
            if (maps[rx][ry] == 0)
                continue;
            if (visited[rx][ry] > visited[x][y] + 1)
            {
                visited[rx][ry] = visited[x][y] + 1;
                dq.push(make_pair(rx, ry));
            }
        }
    }

    if (visited[n - 1][m - 1] < 1000001)
        return visited[n - 1][m - 1];
    else
        return -1;
}