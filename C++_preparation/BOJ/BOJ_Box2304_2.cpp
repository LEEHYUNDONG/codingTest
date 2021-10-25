#include <iostream>
#include <vector>
using namespace std;

int main()
{
    vector<pair<int, int> > v;
    int n;
    cin >> n;
    int maxH = INT_MIN;
    int ind = 0;
    for (int i = 0; i < n; i++)
    {
        int x, y;
        cin >> x >> y;
        if (maxH < y)
        {
            ind = i;
            maxH = y;
        }
        v.push_back(make_pair(x, y));
    }
    sort(v.begin(), v.end());
    int ans = 0;
    int l = ind;
    int tmp = ind;
    int r = n - 1;
    while (l >= 0)
    {
        l--;
        if (v[l].second < maxH)
        {
            cout << v[l].first << " " << v[l].second << "\n";

            ans += v[l].second * abs(v[ind].first - v[l].first);
            maxH = v[l].second;
            ind = l;
        }
        else
        {
        }
    }
    ind = tmp;
    while (r--)
    {
        if (v[r].second > maxH)
        {
            ans += v[r].second * abs(v[ind].first - v[r].first);
            maxH = v[r].second;
            ind = r;
        }
    }
    cout << ans << "\n";

    return 0;
}