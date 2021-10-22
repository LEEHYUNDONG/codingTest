#include <stdio.h>
#include <vector>
#include <queue>
#include <iostream>
#define MAX_V 100
#define INF 99999999
using namespace std;

vector<pair<int, int> > adj[100];
vector<int> dijkstra(int start, int V)
{
    vector<int> dist(V, INF);
    priority_queue<pair<int, int> > q;
    q.push(make_pair(0, start));
    while (!q.empty())
    {
        int cost = -q.top().first;
        int from = q.top().second;
        q.pop();

        if (dist[from] < cost)
            continue;
        for (int i = 0; i < adj[from].size(); i++)
        {
            int to = adj[from][i].first;
            int edgec = cost + adj[from][i].second;
            if (edgec < dist[to])
            {
                dist[to] = edgec;
                q.push(make_pair(-edgec, to));
            }
        }
    }
    return dist;
}

int main(void)
{
    int e, v;
    cout << "Number of node and edges :";
    cin >> v >> e;

    for (int i = 0; i < e; i++)
    {
        int a, b, c;
        cout << "input two nodes and cost :";
        cin >> a >> b >> c;
        adj[a].push_back(make_pair(b, c));
        adj[b].push_back(make_pair(a, c));
    }
    cout << "-----dijkstra-----\n";
    vector<int> d = dijkstra(0, v);
    for (int i = 0; i < v; i++)
    {
        cout << d[i] << " ";
    }
    cout << endl;
    return 0;
}
