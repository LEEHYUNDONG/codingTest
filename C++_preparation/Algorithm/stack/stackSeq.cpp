#include <bits/stdc++.h>
using namespace std;
int main()
{
    ios::sync_with_stdio(0);
    cin.tie(0);

    stack<int> st;
    int curr = 1;
    int num;
    vector<char> ans;
    bool flag = true;
    int n;
    cin >> n;

    for (int i = 0; i < n; i++)
    {
        cin >> num;
        while (curr <= num)
        {
            st.push(curr);
            curr++;
            ans.push_back('+');
        }
        if (st.top() == num)
        {
            st.pop();
            ans.push_back('-');
        }
        else
        {
            cout << "NO";
            flag = false;
            break;
        }
    }
    if (flag)
    {
        for (auto a : ans)
        {
            cout << a << '\n';
        }
    }

    return 0;
}