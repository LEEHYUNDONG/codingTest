#include <bits/stdc++.h>
using namespace std;
int main()
{

    ios::sync_with_stdio(0);
    cin.tie(0);
    stack<pair<int, int>> st;
    int n;
    cin >> n;
    vector<int> ans;
    int towerh;
    for (int i = 0; i < n; i++)
    {
        cin >> towerh;
        if (st.empty())
        {
            ans.push_back(0);
            st.push(make_pair(towerh, i + 1));
        }
        else
        {
            if (st.top().first > towerh)
            {
                ans.push_back(st.top().second);
                st.push(make_pair(towerh, i + 1));
            }
            else
            {
                st.pop();
                while (!st.empty())
                {
                    if (st.top().first > towerh)
                    {
                        ans.push_back(st.top().second);
                        break;
                    }
                    st.pop();
                }
                if (st.empty())
                {
                    ans.push_back(0);
                }
                st.push(make_pair(towerh, i + 1));
            }
        }
    }
    for (auto a : ans)
        cout << a << ' ';
    return 0;
}