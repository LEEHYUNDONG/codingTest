#include <string>
#include <vector>
#include <queue>
#include <iostream>

using namespace std;

vector<vector<int> > solution(int rows, int columns)
{
    vector<vector<int> > answer(rows, vector<int>(columns, 0));
    int dx[4] = {0, 0, 1, -1};
    int dy[4] = {1, -1, 0, 0};

    queue<pair<pair<int, int>, int> > q;
    q.push({{0, 0}, 1});

    answer[0][0] = 1;
    while (!q.empty())
    {
        int x = q.front().first.first, y = q.front().first.second;
        int num = q.front().second;
        q.pop();
        int cnt = 0;
        int flag = 0;
        for (int i = 0; i < rows; i++)
        {
            for (int j = 0; j < columns; j++)
            {
                if (answer[i][j] == 0)
                    flag = 1;
                else
                    cnt++;
            }
        }
        if (!flag)
            return answer;
        if (num % 2)
        { //홀수
            y += 1;
            if (y >= columns)
                y = 0;
        }
        else if (!(num % 2))
        {
            x += 1;
            if (x >= rows)
                x = 0;
        }
        if (x < 0 || x >= rows || y < 0 || y >= columns)
            continue;
        if (rows == columns && answer[x][y])
            continue;
        answer[x][y] = num + 1;
        q.push({{x, y}, num + 1});
    }

    return answer;
}