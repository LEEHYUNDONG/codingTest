#include <iostream>
#include <vector>
#include <memory.h>
#include <ordered_set>

using namespace std;
int l[50];
bool visited[50];
int t;
vector<int> tmp;
int cnt = 0;

void dfs(int i, int depth)
{
    if (tmp.size() == 6)
    {
        for (auto a : tmp)
            cout << a << " ";

        cnt++;
        cout << endl;
        return;
    }
    for (int j = 0; j < t; j++)
    {
        if (!visited[j] && depth < 6)
        {
            visited[j] = true;
            tmp.push_back(l[j]);
            dfs(j, depth + 1);
            tmp.pop_back();
            visited[j] = false;
        }
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
        memset(visited, false, sizeof(visited));
        dfs(0, 0);
        cout << "cnt :" << cnt << '\n';
    }
    return 0;
}