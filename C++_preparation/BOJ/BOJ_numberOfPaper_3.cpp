#include <iostream>

using namespace std;

int data[3001][3001];
int ans[3] = {0, 0, 0};

void cut(int x, int y, int size)
{
    bool flag = true;
    for (int i = x; i < size + x; i++)
    {
        for (int j = y; j < y + size; j++)
        {
            if (data[x][y] != data[i][j])
            {
                flag = false;
                break;
            }
        }
    }
    if (flag)
    {
        ans[data[x][y] + 1]++;
        return;
    }
    for (int i = x; i < x + size; i += size / 3)
    {
        for (int j = y; j < y + size; j += size / 3)
        {
            cut(i, j, size / 3);
        }
    }
}
int main()
{
    int n;
    cin >> n;
    for (int i = 0; i < n; i++)
    {
        for (int j = 0; j < n; j++)
        {
            cin >> data[i][j];
        }
    }
    cut(0, 0, n);

    for (auto a : ans)
        cout << a << '\n';

    return 0;
}