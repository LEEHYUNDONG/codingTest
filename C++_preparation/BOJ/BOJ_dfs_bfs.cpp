#include <iostream>
#include <queue>
#include <memory.h>

using namespace std;

int m, n, v;
int dx[4] = {0, 0, -1, 1};
int dy[4] = {-1, 1, 0, 0};

int graph[1001][1001];
bool visited[1001][1001];

void dfs(int i, int j)
{
}
int main()
{
    cin >> m >> n >> v;
    memset(graph, 0, sizeof(graph));
    memset(visited, false, sizeof(visited));
    for (int i = 0; i < n; i++)
    {
        cin >> a >> b;
        graph[a][b] = 1;
        graph[b][a] = 1;
    }
    return 0;
}