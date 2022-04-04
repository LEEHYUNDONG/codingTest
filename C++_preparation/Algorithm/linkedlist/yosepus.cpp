#include <bits/stdc++.h>
using namespace std;
int main()
{
    ios::sync_with_stdio(0);
    cin.tie(0);

    int n, k;
    cin >> n >> k;
    vector<int> v, ans;

    for (int i = 1; i <= n; i++)
        v.push_back(i);

    for (int i = 0; ans.size() < n; i++)
    {
        if (i % k == k - 1)
            ans.push_back(v[i]);
        else
            v.push_back(v[i]);
    }
    cout << "<";
    for (int i = 0; i < n; i++)
    {
        if (i == n - 1)
            cout << ans[i];
        else
            cout << ans[i] << ", ";
    }
    cout << ">";
    cout << '\n';

    return 0;
}