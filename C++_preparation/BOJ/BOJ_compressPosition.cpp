#include <iostream>
#include <vector>
#include <unordered_map>
#include <algorithm>
using namespace std;

int main()
{
    int n;
    vector<int> pos;
    int a[1000000];
    int ans[1000001];
    ios::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);
    cin >> n;
    for (int i = 0; i < n; i++)
    {
        int t;
        cin >> t;
        if (find(pos.begin(), pos.end(), t) == pos.end())
            pos.push_back(t);
        a[i] = t;
    }
    sort(pos.begin(), pos.end());
    int cnt = 0;
    for (auto a : pos)
    {
        ans[a] = cnt;
        cnt++;
    }
    for (int i = 0; i < n; i++)
    {
        cout << ans[a[i]] << " ";
    }
    cout << '\n';

    return 0;_XLOCALE__TIME_H_
}