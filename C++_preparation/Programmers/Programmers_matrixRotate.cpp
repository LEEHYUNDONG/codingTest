#include <string>
#include <vector>
#include <iostream>

using namespace std;

vector<int> solution(int rows, int columns, vector<vector<int> > queries)
{
    vector<int> answer;
    vector<vector<int> > mat;
    int num = 1;
    for (int i = 0; i < rows; i++)
    {
        vector<int> tmp;
        for (int j = 0; j < columns; j++)
        {
            tmp.push_back(num++);
        }
        mat.push_back(tmp);
    }

    for (int i = 0; i < queries.size(); i++)
    {
        int res = 100001;
        int l = queries[i][0] - 1;
        int r = queries[i][1] - 1;
        int t = queries[i][2] - 1;
        int b = queries[i][3] - 1;
        int top = mat[l][r];

        for (int j = r + 1; j <= b; j++)
        {
            int tmp = mat[l][j];
            mat[l][j] = top;
            top = tmp;
            if (res > mat[l][j])
                res = mat[l][j];
        }
        for (int j = l + 1; j <= t; j++)
        {
            int tmp = mat[j][b];
            mat[j][b] = top;
            top = tmp;
            if (res > mat[j][b])
                res = mat[j][b];
        }
        for (int j = b - 1; j >= r; j--)
        {
            int tmp = mat[t][j];
            mat[t][j] = top;
            top = tmp;
            if (res > mat[t][j])
                res = mat[t][j];
        }
        for (int j = t - 1; j >= l; j--)
        {
            int tmp = mat[j][r];
            mat[j][r] = top;
            top = tmp;
            if (res > mat[j][r])
                res = mat[j][r];
        }
        // mat[l][r] = top;
        answer.push_back(res);
    }
    return answer;
}