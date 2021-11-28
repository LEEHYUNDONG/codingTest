#include <iostream>
#include <string>
#include <stack>

using namespace std;

int main()
{
    ios::sync_with_stdio(false);
    cin.tie(0);
    cout.tie(0);
    int n;
    cin >> n;
    string s = "";

    for (int i = 0; i < n; i++)
    {

        stack<char> st;
        cin >> s;
        for (int j = 0; j < s.length(); j++)
        {
            if (s[j] == '(')
                st.push(s[j]);
            else if (s[j] == ')')
            {
                if (st.empty())
                {
                    st.push(s[j]);
                    break;
                }
                if (st.top() == '(')
                {
                    st.pop();
                }
            }
        }
        if (st.empty())
        {
            cout << "YES\n";
        }
        else
        {
            cout << "NO\n";
        }
    }
    return 0;
}