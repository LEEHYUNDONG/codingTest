#include <bits/stdc++.h>
using namespace std;
int main()
{

    ios::sync_with_stdio(0);
    cin.tie(0);
    int n, l;
    cin >> n >> l;
    vector<pair<int, int>> puddle;
    for (int i = 0; i < n; i++)
    {
        int a, b;
        cin >> a >> b;
        puddle.push_back(make_pair(a, b));
    }
    sort(puddle.begin(), puddle.end());

    int ans = 0;
    int start, end, covered;
    int coveredEnd = 0;

    for (int i = 0; i < puddle.size(); i++)
    {
        start = puddle[i].first;
        end = puddle[i].second;
        if (end <= coveredEnd)
            continue;

        if (start > coveredEnd)
            coveredEnd = start;

        int covered = ((end - (coveredEnd + 1)) / l) + 1;
        ans += covered;
        coveredEnd += covered * l;

        // cout << coveredEnd << '\n';
    }
    cout << ans << '\n';
    return 0;
}