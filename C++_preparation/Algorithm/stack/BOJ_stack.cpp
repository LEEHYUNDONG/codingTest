#include <bits/stdc++.h>
using namespace std;
int main()
{

    ios::sync_with_stdio(0);
    cin.tie(0);
    stack<int> st;
    int n;
    cin >> n;

    for (int i = 0; i < n; i++)
    {
        string op;
        cin >> op;
        if (op == "push")
        {
            int num;
            cin >> num;
            st.push(num);
        }
        else if (op == "top")
        {
            if (!st.empty())
            {
                cout << st.top() << '\n';
            }
            else
            {
                cout << -1 << '\n';
            }
        }
        else if (op == "size")
        {
            cout << st.size() << '\n';
        }
        else if (op == "pop")
        {
            if (!st.empty())
            {
                cout << st.top() << '\n';
                st.pop();
            }
            else
            {
                cout << -1 << '\n';
            }
        }
        else if (op == "empty")
        {
            if (st.empty())
                cout << 1 << '\n';
            else
                cout << 0 << '\n';
        }
    }

    return 0;
}