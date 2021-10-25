#include <iostream>
#include <vector>
using namespace std;

int main()
{
    vector<pair<int, int> > v;
    int n;
    cin >> n;
    int maxh = INT_MIN;
    int ind = 0;
    // vector<int> vi(1001);
    for (int i = 0; i < n; i++)
    {
        int x, y;
        cin >> x >> y;
        v.push_back(make_pair(x, y));
    }
    sort(v.begin(), v.end());
    vector<int> vi(v[n - 1].first);

    for (int i = 0; i < n; i++)
    {
        vi[v[i].first] = v[i].second;
        if (v[i].second > maxh)
        {
            maxh = v[i].second;
            ind = i;
        }
    }

    int h = v[0].second;
    int ans = 0;
    for (int i = v[0].first; i < v[ind].first; i++)
    {
        h = max(h, vi[i]);
        ans += h;
    }
    int rh = v[n - 1].second;
    for (int i = v[n - 1].first; i > v[ind].first; i--)
    {
        h = max(h, vi[i]);
        ans += h;
    }
    ans += maxh;
    cout << ans << "\n";

    return 0;
}