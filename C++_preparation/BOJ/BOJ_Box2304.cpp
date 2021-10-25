#include <iostream>
#include <vector>
using namespace std;

int main()
{
    vector<pair<int, int> > v;
    int n;
    cin >> n;
    for (int i = 0; i < n; i++)
    {
        int x, y;
        cin >> x >> y;
        v.push_back(make_pair(x, y));
    }
    sort(v.begin(), v.end());
    int h = v[0].second;
    int ans = 0;
    int x = 0;
    // for (int i = 0; i < n; i++)
    // {
    //     if (h < v[i].second)
    //     {
    //         ans += (x - v[i].first) * h;
    //         x = v[i].first;
    //         h = v[i].second;
    //     }
    //     else if (h > v[i].second)
    //     {
    //         x = v[i].first;
    //     }
    // }
    int l = 0;
    int r = n - 1;
    int hl = v[0].second;
    int hr = v[1].second;

    while (l <= r)
    {
        int xl = v[l].first;
        int xr = v[r].first;
        if (hr == hl && l == r)
        {
            ans += v[r].second;
        }
        while (v[l].second <= hl)
        {
            l++;
        }
        while (v[r].second <= hr)
        {
            r--;
        }
        ans += (v[l].second - xl) * hl;
        ans += (v[r].second - xr) * hr;
        hl = v[l].second;
        hr = v[r].second;
    }
    cout << ans << endl;
    return 0;
}