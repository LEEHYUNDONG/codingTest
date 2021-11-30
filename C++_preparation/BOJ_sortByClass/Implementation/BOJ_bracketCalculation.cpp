#include <iostream>
#include <stack>
#include <string>

using namespace std;

int main()
{
    string b;
    stack<char> st;
    stack<int> answer;
    cin >> b;
    int ans = 1;
    for (int i = 0; i < b.length(); i++)
    {
        if (b[i] == '(')
        {
            ans *= 2;
            st.push(b[i]);
        }
        else if (b[i] == '[')
        {
            ans *= 3;
            st.push(b[i]);
        }
        else if (b[i] == ')' && st.top() == '(')
        {
        }
    }
    return 0;
}