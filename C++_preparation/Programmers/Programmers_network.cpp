#include <string>
#include <vector>
#include <memory.h>
#include <iostream>

using namespace std;
int dx[4] = {-1, 1, 0, 0};
int dy[4] = {0, 0, -1, 1};
bool visited[201];

int dfs(vector<vector<int> > graph, int x, int n)
{
    for (int i = 0; i < n; i++)
    {
        if (!visited[i] && graph[x][i])
        {
            visited[i] = true;
            dfs(graph, i, n);
        }
    }
    return 1;
}

int solution(int n, vector<vector<int> > computers)
{
    int answer = 0;
    memset(visited, false, sizeof(visited));

    for (int i = 0; i < n; i++)
    {
        if (!visited[i])
        {
            visited[i] = true;
            answer += dfs(computers, i, n);
        }
    }
    return answer;
}