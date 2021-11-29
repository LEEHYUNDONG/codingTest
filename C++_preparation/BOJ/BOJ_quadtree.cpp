#include <iostream>

using namespace std;
string graph[65];
string ans = "";
void project(int x, int y, int size)
{
    char color = graph[x][y];

    for (int i = x; i < x + size; i++)
    {
        for (int j = y; j < y + size; j++)
        {
            if (graph[i][j] != color)
            {
                ans += '(';
                project(x, y, size / 2);
                project(x, y + size / 2, size / 2);
                project(x + size / 2, y, size / 2);
                project(x + size / 2, y + size / 2, size / 2);
                ans += ')';
                return;
            }
        }
    }
    ans += color;
}
int main()
{
    ios::sync_with_stdio(false);
    cin.tie(0);
    cout.tie(0);
    int n;

    cin >> n;
    for (int i = 0; i < n; i++)
        cin >> graph[i];
    project(0, 0, n);
    cout << ans << '\n';
    return 0;
}