#include <iostream>
#include <vector>
#include <stack>
#include <string>

using namespace std;

int main()
{
    string s;
    cin >> s;
    stack<int> st;
    stack<string> tt;
    int i = 0;
    string word = "";
    int cnt = 0;
    while (s[i] != '(')
    {
        if (s[i + 1] == '(')
            break;
        word += s[i];
        i++;
    }
    tt.push(word);

    for (int i = 0; i < s.length(); i++)
    {
        if (s[i] == '(')
        {
            string tmp = "";
            tmp += s[i - 1];

            string word = "";
            i++;

            while (s[i] != '(' || s[i] != ')')
            {
                if ((s[i + 1] == ')' || s[i + 1] == '(') && i + 1 < s.length())
                {
                    if (s[i + 1] == ')')
                        word += s[i];
                    break;
                }
                word += s[i];
                i++;
            }
            if (word != "")
            {
                tt.push(word);
            }
            // tt.push(word);
            st.push(stoi(tmp));
        }
        else
        {
            cnt += 1;
        }
    }
    if (cnt != s.length())
    {
        // string ans = "";
        // while ((!st.empty()) || (!tt.empty()))
        // {
        //     int x = st.top();
        //     st.pop();
        //     string tmp = tt.top();
        //     tt.pop();
        //     for (int i = 0; i < x; i++)
        //     {
        //         ans += tmp;
        //     }
        // }
        // cout << ans << endl;
        while (!tt.empty())
        {
            string tmp;
            tmp = tt.top();
            tt.pop();
            cout << tmp << endl;
        }
    }
    else
    {
        cout << s.length() << endl;
    }
    return 0;
}