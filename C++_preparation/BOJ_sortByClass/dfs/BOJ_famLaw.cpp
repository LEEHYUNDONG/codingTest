#include <iostream>
#include <vector>

using namespace std;

int n, m;
int st, ed;
int ans = -1;
vector<int> v[101];
bool visited[101] = {false};

int dfs(int x, int depth)
{
    if (x == ed)
    {
        ans = depth;
        return depth;
    }
    if (visited[x])
        return 0;
    visited[x] = true;
    for (int i = 0; i < v[x].size(); i++)
    {
        if (!visited[v[x][i]])
            dfs(v[x][i], depth + 1);
    }
    return ans;
}
int main()
{
    ios::sync_with_stdio(0);
    cin.tie(0);
    cout.tie(0);
    cin >> n;
    for (int i = 0; i <= n; i++)
    {
        vector<int> st;
        v[i] = st;
    }
    cin >> st >> ed;
    cin >> m;
    int x, y;
    for (int i = 0; i < m; i++)
    {
        cin >> x >> y;
        v[x].push_back(y);
        v[y].push_back(x);
    }

    cout << dfs(st, 0) << '\n';

    return 0;
}