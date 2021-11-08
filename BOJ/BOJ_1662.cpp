#include <iostream>
#include <vector>
#include <stack>
#include <sstream>
#include <regex>

using namespace std;

int main()
{
    string s;
    cin >> s;

    string answer = "";
    stack<string> st;
    stack<int> sn;
    string tmp;
    stringstream ss;

    for (int i = 0; i < s.length(); i++)
    {
        if (s[i] >= '0' && s[i] <= '9')
            continue;
        else
            s[i] = ' ';
    }

    ss.str(s);
    int n;
    int start;

    while (ss >> n)
    {
        sn.push(n % 10);
        st.push(to_string(n / 10));
        start = n;
    }
    if (!sn.empty())
    {
        sn.pop();
        st.pop();
    }
    answer = to_string(start);
    if (st.empty())
    {
        cout << answer.length() << '\n';
    }
    else
    {
        while (!st.empty() || !sn.empty())
        {
            tmp = "";
            if (st.top() == "0")
            {
                sn.pop();
                st.pop();
                continue;
            }
            if (sn.top() == 1)
                answer += st.top();
            else if (sn.top() == 0)
            {
                answer = "";
                break;
            }
            else
            {
                for (int i = 0; i < sn.top(); i++)
                {
                    tmp += answer;
                }
                answer = tmp;
                answer += st.top();
            }
            sn.pop();
            st.pop();
        }
        cout << answer.length() << '\n';
    }
    return 0;
}