#include <string>
#include <vector>
#include <iostream>
#include <cstring>

using namespace std;

int direction[4][2] = {
    {1, 0},
    {-1, 0},
    {0, 1},
    {0, -1}};
bool visited[5][5];
bool flag;

void dfs(vector<string> &place, int x, int y, int depth)
{
    if (depth > 2 || flag)
    {
        return;
    }
    if (depth > 0 && place[x][y] == 'P')
    {
        flag = true;
        return;
    }
    visited[x][y] = true;
    for (int i = 0; i < 4; i++)
    {
        int rx = direction[i][0] + x;
        int ry = direction[i][1] + y;
        if (!(0 <= rx && rx < 5 && 0 <= ry && ry < 5) || visited[rx][ry] || place[rx][ry] == 'X')
            continue;
        dfs(place, rx, ry, depth + 1);
    }
}

vector<int> solution(vector<vector<string> > places)
{
    vector<int> answer;

    for (int i = 0; i < places.size(); i++)
    {
        vector<pair<int, int> > spot;
        for (int j = 0; j < 5; j++)
        {
            for (int k = 0; k < 5; k++)
            {
                if (places[i][j][k] == 'P')
                {
                    spot.push_back(make_pair(j, k));
                }
            }
        }
        if (!spot.size())
        {
            answer.push_back(1);
            continue;
        }
        else
        {
            int t = 0;
            for (auto a : spot)
            {
                flag = false;
                memset(visited, false, sizeof(visited));
                dfs(places[i], a.first, a.second, 0);
                if (flag)
                {
                    answer.push_back(0);
                    t = 1;
                    break;
                }
            }
            if (t == 0)
                answer.push_back(1);
        }
    }
    return answer;
}