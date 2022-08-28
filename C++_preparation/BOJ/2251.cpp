#include <bits/stdc++.h>
using namespace std;

int A, B, C;
bool visited[201][201][201];
vector<int> ans;

void bfs()
{
    queue<pair<pair<int, int>, int>> q;
    q.push({{0, 0}, C});

    while(!q.empty()){
        int a = q.front().first.first;
        int b = q.front().first.second;
        int c = q.front().second;
        q.pop();
        if(visited[a][b][c])
            continue;
        visited[a][b][c] = true;
        if (a == 0)
            ans.push_back(c);
        
        if(a+b > B)
            q.push({{a + b - B, B}, C});
        else
            q.push({{0, a + b}, c});
        if(a+c > C)
            q.push({{a + c - C, b}, C});
        else
            q.push({{0, b}, a+c});
        
        if(a+b > A)
            q.push({{A, b+a-A}, c});
        else
            q.push({{b+a, 0}, c});
        
        if(c+b > C)
            q.push({{a, b+c-C}, C});
        else
            q.push({{a,0}, b+c});
        
        if(a+c > A)
            q.push({{A, b},c+a-A});
        else
            q.push({{c+a, b}, 0});
        if(c+b>B)
            q.push({{a,B},c+b-B});
        else
            q.push({{a,b+c},0});

    }
}

int main()
{
    ios::sync_with_stdio(0);
    cin.tie(0);

    cin >> A >> B >> C;
    bfs();

    sort(ans.begin(), ans.end());

    for(auto a : ans)
        cout << a << " ";

    return 0;
}