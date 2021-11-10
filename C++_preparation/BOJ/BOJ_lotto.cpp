#include <iostream>
#include <vector>
#include <memory.h>
#include <algorithm>

using namespace std;
int l[50];
int ans[13];
int t;
vector<int> tmp;

void dfs(int start, int depth)
{
    if (depth == 6)
    {
        for (int i = 0; i < 6; i++)
            cout << ans[i] << ' ';
        cout << endl;
        return;
    }
    for (int j = start; j < t; j++)
    {
        ans[depth] = l[j];
        dfs(j + 1, depth + 1);
    }
}
int main()
{
    while (1)
    {
        cin >> t;
        if (t == 0)
            break;
        for (int i = 0; i < t; i++)
        {
            cin >> l[i];
        }
        dfs(0, 0);
        cout << '\n';
    }
    return 0;
}