#include <bits/stdc++.h>
using namespace std;
int main()
{

    ios::sync_with_stdio(0);
    cin.tie(0);
    stack<int> st;
    int n;
    cin >> n;
    int num;
    for (int i = 0; i < n; i++)
    {
        cin >> num;
        if (num == 0)
        {
            st.pop();
        }
        else
        {
            st.push(num);
        }
    }
    int ans = 0;
    while (!st.empty())
    {
        ans += st.top();
        st.pop();
    }
    cout << ans;
    return 0;
}