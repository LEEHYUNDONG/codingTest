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
    int i = 0;
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
        while (word >> i)
        {
            string tmp = to_string(i);
            st.push(tmp);
        }
        while (!st.empty())
        {
            string tmp;
            tmp = st.top();
            st.pop();
            if (tmp.length() <= 1)
            {
                ans += tmp;
            }
            else
            {
                int x = int(tmp[tmp.length() - 1]);
                string tmp2 = "";

                for (int i = 0; i < tmp.length() - 1; i++)
                {
                    tmp2 += tmp[i];
                }
                for (i = 0; i < x; i++)
                {
                    ans += tmp2;
                }
            }
        }
        cout << ans.length() << endl;
    }

    return 0;
}