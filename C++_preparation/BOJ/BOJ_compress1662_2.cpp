#include <iostream>
#include <sstream>
#include <stack>
#include <string>

using namespace std;

int main()
{
    string s;
    cin >> s;
    stack<string> st;
    stringstream word;
    int cnt = 0;
    for (int i = 0; i < s.length(); i++)
    {
        if (s[i] == '(' || s[i] == ')')
        {
            s[i] = ' ';
            cnt++;
        }
    }
    if (cnt == 0)
    {
        cout << s.length() << endl;
    }
    else
    {
        string ans = "";
        word.str(s);
        int r;
        int i;
        while (word >> i)
        {
            string tmp = to_string(i);
            st.push(tmp);
        }
        int flag = 0;
        ans = st.top();
        st.pop();
        while (!st.empty())
        {
            string tmp;
            tmp = st.top();
            st.pop();
            string tmp2 = "";
            string tmp3 = "";
            int x = int(tmp[tmp.length() - 1]) - '0';
            if (x == 0)
            {
                cout << "0" << endl;
                flag = 1;
                break;
            }
            for (int i = 0; i < x; i++)
            {
                tmp3 += ans;
            }
                for (int i = 0; i < tmp.length() - 1; i++)
                {
                    tmp2 += tmp[i];
                }

                ans = "";
                ans += tmp3 + tmp2;
        }
        if (flag == 0)
            cout << ans.length() << endl;
    }

    return 0;
}