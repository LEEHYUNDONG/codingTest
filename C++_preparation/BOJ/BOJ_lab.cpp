#include <vector>
#include <iostream>
#include <memory.h>

using namespace std;

int map[9][9];
bool visited[9][9];
int dx[4] = {0, 0, -1, 1};
int dy[4] = {1, -1, 0, 0};
int n, m;
int answer = 0;
int cnt;

vector<pair<int, int> > loc;

void spread(int x, int y)
{
    if (visited[x][y])
        return;
    visited[x][y] = true;
    for (int i = 0; i < 4; i++)
    {
        int rx = x + dx[i];
        int ry = y + dy[i];

        if (0 <= rx && rx < n && 0 <= ry && ry < m && map[rx][ry] == 0)
        {
            if (map[x][y] == 2 && map[rx][ry] == 1)
                continue;
            else if (map[x][y] == 2 && map[rx][ry] == 0)
            {
                map[rx][ry] = 2;
                spread(rx, ry);
            }
        }
    }
    return;
}
void setWall(int x, int y, int depth)
{
    if (depth >= 3)
    {
        cnt = 0;
        memset(visited, false, sizeof(visited));
        int tmpM[9][9];
        copy(&map[0][0], &map[0][0] + 81, &tmpM[0][0]);

        for (int i = 0; i < loc.size(); i++)
        {
            spread(loc[i].first, loc[i].second);
        }

        for (int i = 0; i < n; i++)
        {
            for (int j = 0; j < m; j++)
            {

                if (map[i][j] == 0)
                    cnt++;
            }
        }
        copy(&tmpM[0][0], &tmpM[0][0] + 81, &map[0][0]);
        answer = max(answer, cnt);
        return;
    }
    for (int i = 0; i < n; i++)
    {
        for (int j = 0; j < m; j++)
        {
            if (map[i][j] == 0)
            {
                map[i][j] = 1;
                setWall(i, j, depth + 1);
                map[i][j] = 0;
            }
        }
    }
}
int main()
{

    cin >> n >> m;
    memset(visited, false, sizeof(visited));

    for (int i = 0; i < n; i++)
    {
        for (int j = 0; j < m; j++)
        {
            cin >> map[i][j];
            if (map[i][j] == 2)
                loc.push_back(make_pair(i, j));
        }
    }

    setWall(0, 0, 0);

    cout << answer << endl;
    return 0;
}