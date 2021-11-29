#include <iostream>
using namespace std;
int ans[2] = {0, 0};
int graph[129][129];

void colorChip(int x, int y, int size)
{
    int color = graph[x][y];
    for (int i = x; i < x + size; i++)
    {
        for (int j = y; j < y + size; j++)
        {
            if (graph[i][j] != color)
            {
                colorChip(x, y, size / 2);
                colorChip(x, y + size / 2, size / 2);
                colorChip(x + size / 2, y, size / 2);
                colorChip(x + size / 2, y + size / 2, size / 2);
                return;
            }
        }
    }
    ans[color]++;
}
int main()
{
    int n;
    cin >> n;
    for (int i = 0; i < n; i++)
    {
        for (int j = 0; j < n; j++)
        {
            cin >> graph[i][j];
        }
    }
    colorChip(0, 0, n);
    cout << ans[0] << '\n'
         << ans[1] << '\n';
    return 0;
}