#include <string>
#include <vector>
#include <memory.h>
#include <iostream>
using namespace std;

bool visited[5][5];
bool flag;
int direction[4][2] = {
    {1, 0},
    {-1, 0},
    {0, 1},
    {0, -1}};

void dfs(vector<string> &place, int x, int y, int depth)
{
    if (depth > 2 || flag)
        return;
    if (depth > 0 && place[x][y] == 'P')
    {
        flag = true;
        return;
    }
    visited[x][y] = true;
    for (int i = 0; i < 4; i++)
    {
        int rx = direction[i][0] + x, ry = direction[i][1] + y;
        if (!(0 <= rx && rx < 5 && 0 <= ry && ry < 5) || visited[rx][ry] || place[rx][ry] == 'X')
            continue;
        dfs(place, rx, ry, depth + 1);
    }
}

vector<int> solution(vector<vector<string> > places)
{
    vector<int> answer;

    for (auto a : places)
    {
        vector<pair<int, int> > people;
        for (int i = 0; i < 5; i++)
        {
            for (int j = 0; j < 5; j++)
            {
                if (a[i][j] == 'P')
                {
                    people.push_back(make_pair(i, j));
                }
            }
        }
        if (!people.size())
        {
            answer.push_back(1);
            continue;
        }
        else
        {
            bool f = false;
            for (auto b : people)
            {
                flag = false;
                memset(visited, false, sizeof(visited));
                dfs(a, b.first, b.second, 0);
                if (flag)
                {
                    answer.push_back(0);
                    f = true;
                    break;
                }
            }
            if (!f)
                answer.push_back(1);
        }
    }
    return answer;
}