#include <iostream>
#include <vector>

using namespace std;
int graph[10][10];
int visited[1001] = {false};

int main()
{
    int n, m;
    cin >> n >> m;
    // for (int i = 0; i < n; i++)
    // {
    //     graph[i] = vector<int>();
    // }
    for (int i = 0; i < m; i++)
    {
        int x, y;
        cin >> x >> y;
        graph[x].push_back(y);
        graph[y].push_back(x);
    }
    for (auto a : graph)
    {
        for (auto b : a)
        {
            cout << b << " ";
        }
        cout << '\n';
    }

    return 0;
}