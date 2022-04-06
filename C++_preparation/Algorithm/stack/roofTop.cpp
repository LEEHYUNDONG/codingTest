#include <bits/stdc++.h>
using namespace std;

typedef long long ll;

int main()
{

    ios::sync_with_stdio(0);
    cin.tie(0);
    stack<int> st;

    ll n;
    cin >> n;
    ll ans = 0;
    ll h;

    while (n--)
    {
        cin >> h;
        while (!st.empty() && st.top() <= h)
            st.pop();
        ans += st.size();
        st.push(h);
    }
    cout << ans;

    return 0;
}