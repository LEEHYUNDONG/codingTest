#include <vector>
#include <queue>
#include <stdio.h>
#include <memory.h>
#define INT_MAX 1000001

using namespace std;

int visited[101][101];

int solution(vector<vector<int> > maps)
{
    int answer = 0;
    queue<pair<int, int> > q;
    int dx[4] = {0, 0, 1, -1};
    int dy[4] = {1, -1, 0, 0};
    int n = maps.size(), m = maps[0].size();

    memset(visited, 1000001, sizeof(visited));
    q.push(make_pair(0, 0));
    visited[0][0] = 1;

    while (!q.empty())
    {
        int x = q.front().first, y = q.front().second;
        q.pop();
        for (int i = 0; i < 4; i++)
        {
            int rx = x + dx[i], ry = y + dy[i];
            if (rx < 0 || rx >= n || ry < 0 || ry >= m)
                continue;
            if (maps[rx][ry] == 0)
                continue;

            if (visited[rx][ry] > visited[x][y] + 1)
            {
                q.push(make_pair(rx, ry));
                visited[rx][ry] = visited[x][y] + 1;
            }
        }
    }
    answer = visited[n - 1][m - 1];
    if (visited[n - 1][m - 1] < 1000001)
        return answer;
    else
        return -1;
}