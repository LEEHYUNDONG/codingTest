#include <bits/stdc++.h>
using namespace std;

int ans = 0, N, M;
int visited[501];
vector<int> graph[501];


void bfs() {
    queue<int> q;
    q.push(1);
    visited[1] = 1;
    while (!q.empty()) {
        int x = q.front();
        q.pop();
        for (auto& next : graph[x]) {
            if (visited[next] || visited[x] >= 3) continue;
            q.push(next);
            visited[next] = visited[x] + 1;
            ans++;
        }
    }
}

int main()
{
    ios::sync_with_stdio(0);
    cin.tie(0);

    cin >> N;
    cin >> M;

    for (int i = 0; i < M;i++){
        int a, b;
        cin >> a >> b;
        graph[a].push_back(b);
        graph[b].push_back(a);
    }
    fill(&visited[0], &visited[500], 0);

    bfs();

    cout << ans;
    return 0;
}