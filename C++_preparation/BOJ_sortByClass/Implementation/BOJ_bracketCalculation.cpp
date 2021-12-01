#include <iostream>
#include <stack>
#include <string>

using namespace std;

int main()
{
    string b;
    stack<char> st;
    stack<int> num;
    cin >> b;
    int tot = 0;

    for (int i = 0; i < b.length(); i++)
    {
        if (b[i] == '(')
        {
            st.push(b[i]);
            if (num.empty() || num.top() != 1)
                num.push(1);
        }
        else if (b[i] == '[')
        {
            st.push(b[i]);
            if (num.empty() || num.top() != 1)
                num.push(1);
        }
        else if (!st.empty() && b[i] == ')' && st.top() == '(')
        {
            st.pop();
            int tmp = num.top();
            num.pop();
            num.push(2 * tmp);
        }
        else if (!st.empty() && b[i] == ']' && st.top() == '[')
        {

            st.pop();
            int tmp = num.top();
            num.pop();
            num.push(3 * tmp);
        }
        else
        {
            while (!num.empty())
                num.pop();
            break;
        }
    }
    if (num.empty())
    {
        cout << 0 << '\n';
    }
    else
    {
        while (!num.empty())
        {
            cout << num.top() << '\n';
            tot += num.top();
            num.pop();
        }
        if (tot == 1)
            cout << tot - 1 << '\n';
        else
            cout << tot << '\n';
    }

    return 0;
}