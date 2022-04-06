#include <bits/stdc++.h>
using namespace std;
typedef long long ll;

int main()
{

    ios::sync_with_stdio(0);
    cin.tie(0);
    ll ans = 0;
    ll s;
    cin >> s;
    ll x = sqrt(2 * s);
    for (ll i = x; i >= 1; i--)
    {
        if (i * i + i <= 2 * s)
        {
            ans = i;
            break;
        }
    }
    cout << ans;
    return 0;
}