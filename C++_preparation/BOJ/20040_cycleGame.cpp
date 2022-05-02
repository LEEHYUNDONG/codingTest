#include <bits/stdc++.h>
using namespace std;

int N, M;
int parent[500000];
vector<pair<int, int> > edges;

int find(int x){
    if (parent[x] == x)
        return parent[x];
    return parent[x] = find(parent[x]);
}

void merge(int a, int b){
    a = find(a);
    b = find(b);
    if (a < b)
        parent[b] = a;
    else
        parent[a] = b;
}
void init(){
    for (int i = 0; i < N;i++)
        parent[i] = i;
}
int main()
{

    ios::sync_with_stdio(0);
    cin.tie(0);
    int a, b;
    bool flag = false;
    cin >> N >> M;
    init();
    
    for (int i = 0; i < M; i++)
    {
        cin >> a >> b;
        edges.push_back({a, b});
    }
    for (int i = 0; i < M;i++){
        a = edges[i].first;
        b = edges[i].second;
        if (find(a) == find(b))
        {
            cout << (i+1);
            flag = true;
            break;
        }
        else
        {
            merge(a, b);
        }
    }
    if(!flag)
        cout << 0;

    return 0;
}