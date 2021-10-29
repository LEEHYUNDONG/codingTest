#include <iostream>
#include <string>
#include <stack>

using namespace std;

int solution(string s)
{
    if (s.length() % 2)
        return 0;
    stack<char> st;
    int answer = 0;
    st.push(s[0]);

    for (int i = 1; i < s.length(); i++)
    {
        if (!st.empty() && st.top() == s[i])
        {
            answer = 1;
            st.pop();
        }
        else
        {
            answer = 0;
            st.push(s[i]);
        }
    }

    return answer;
}