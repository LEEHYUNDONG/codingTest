#include <iostream>
#include <deque>
#include <algorithm>
using namespace std;

int size = 0;
int visited[10][10] = {0};
int direction[4][2] = {
    {1, 0},
    {-1, 0},
    {0, -1},
    {0, 1}};
int d = 0;

int dfs(int i, int j, int s, int cnt, int **matrix)
{
    if (i >= s || i < 0 || j < 0 || j >= s)
        return 0;
    if (!visited[i][j] && matrix[i][j] == 1)
    {
        visited[i][j] = 1;
        d++;
        for (int k = 0; k < 4; k++)
        {
            dfs(i + direction[k][0], j + direction[k][1], s, cnt + 1, matrix);
        }
        return 1;
    }
    return 0;
}
void solution(int sizeOfMatrix, int **matrix)
{
    deque<int> res;
    int ans = 0;
    for (int i = 0; i < sizeOfMatrix; i++)
    {
        for (int j = 0; j < sizeOfMatrix; j++)
        {
            if (!visited[i][j] && matrix[i][j])
            {
                d = 0;
                ans += dfs(i, j, sizeOfMatrix, 1, matrix);
                res.push_back(d);
            }
        }
    }
    cout << ans << endl;
    if (ans)
    {
        sort(res.begin(), res.end());
        for (int i = 0; i < ans; i++)
        {
            cout << res[i] << ' ';
        }
    }
}