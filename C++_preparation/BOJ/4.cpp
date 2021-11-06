#include <string>
#include <vector>
#include <iostream>
#include <algorithm>
#include <stack>

using namespace std;

vector<int> solution(string s)
{
    vector<int> answer;
    string tmp = "";
    int idx = 0;
    for (int i = 0; i < s.length(); i++)
    {
        if (s[i + 1] != s[i])
        {
            idx = i + 1;
            break;
        }
    }

    tmp += s.substr(0, idx);
    s.erase(s.begin(), s.begin() + idx);
    reverse(s.begin(), s.end());
    tmp += s;

    int cnt = 1;
    stack<char> st;
    st.push(tmp[0]);

    cout << tmp << '\n';
    for (int i = 1; i < tmp.length(); i++)
    {
        if (!st.empty() && st.top() == tmp[i])
            cnt++;
        else
        {
            answer.push_back(cnt);
            st.pop();
            st.push(tmp[i]);
            cnt = 1;
        }
    }
    answer.push_back(cnt);

    sort(answer.begin(), answer.end());

    return answer;
}