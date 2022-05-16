#include <bits/stdc++.h>
using namespace std;

int N;
int parent[3001];
vector<double> grads;
vector<pair<pair<int, int>, pair<int, int> > > coords;

int find(int x){
    if (parent[x] == x)
        return parent[x];
    return parent[x] = find(parent[x]);
}

void merge(int a, int b){
    a = find(a);
    b = find(b);

    parent[b] = a;
}

int ccw(int x1, int y1, int x2, int y2, int x3, int y3){
    long long g = (x1 * y2 + x2 * y3 + x3 + y1) - (y1 * x2 + y2 * x3 + y3 * x1);
    if (g < 0)
        return -1;
    else if(g > 0)
        return 1;
    else
        return 0;
}

bool isIntersect(int x1, int y1, int x2, int y2, int x3, int y3, int x4, int y4){
    if (ccw(x1, y1, x2, y2, x3, y3)*ccw(x1, y1, x2, y2, x4, y4) <= 0 &&
    ccw(x3, y3, x4, y4, x1, y1)*ccw(x3, y3, x4, y4, x2, y2) <= 0
    ){
        if ((x1 > x3 && x1 > x4 && x2 > x3 && x2 > x4) ||
        (x3 > x1 && x3 > x2 && x4 > x1 && x4 > x2))
            return false;
        if ((y1 > y3 && y1 > y4 && y2 > y3 && y2 > y4) ||
        (y3 > y1 && y3 > y2 && y4 > y1 && y4 > y2))
            return false;
        else
            return true;
    }
    return false;
}

// }
void init(){
    for (int i = 0; i <= N;i++){
        parent[i] = i;
    }
}

int main()
{

    ios::sync_with_stdio(0);
    cin.tie(0);
    cin >> N;
    init();
    for (int i = 0; i < N;i++)
    {
        int a, b, c, d;
        cin >> a >> b >> c >> d;
        coords.push_back(make_pair(make_pair(a, b), make_pair(c, d)));
    }

    for (int i = 1; i <= N;i++){
        for (int j = 1; j < i;j++){
            if (isIntersect(coords[i].first.first, coords[i].first.second, coords[i].second.first, coords[i].second.second, coords[j].first.first, coords[j].first.second, coords[j].second.first, coords[j].second.second))
                merge(i, j);
        }
    }
    int cnt[N+1];
    fill(&cnt[0], &cnt[N+1], 0);
    for (int i = 1; i <= N; i++)
        cnt[find(i)]++;

    int ans = 0;
    int tot = 0;
    for (int i = 1; i <= N;i++){
        if (cnt[i] > 0)
            ans++;
        if(cnt[i] > tot){
            tot = cnt[i];
        }
    }
    cout << ans << '\n' << tot;

    return 0;
}





