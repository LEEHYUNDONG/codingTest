#include <iostream>
#include <vector>

using namespace std;

// int graph[1001][1001] = {0};
vector<int> graph[1001];
bool visited[1001] = {false};
int ans = 0;

int dfs(int x)
{
    if (graph[x].size() == 0)
        return 1;
    for (int i = 0; i < graph[x].size(); i++)
    {
        if (visited[graph[x][i]])
            continue;
        visited[graph[x][i]] = true;
        dfs(graph[x][i]);
    }
    return 1;
}

int main()
{
    ios::sync_with_stdio(false);
    cin.tie(0);
    cout.tie(0);

    int v, e;
    cin >> v >> e;

    for (int i = 0; i < e; i++)
    {
        int s, en;
        cin >> s >> en;
        graph[s].push_back(en);
        graph[en].push_back(s);
    }

    for (int i = 1; i <= v; i++)
    {
        if (!visited[i])
        {
            visited[i] = true;
            ans += dfs(i);
        }
    }
    cout << ans << '\n';

    return 0;
}