#include <iostream>
#include <string>
#include <stack>
using namespace std;

int main()
{
    ios::sync_with_stdio(false);
    cin.tie(0);
    cout.tie(0);

    while (1)
    {
        string tmp = "";
        bool flag = true;
        stack<char> s;
        getline(cin, tmp);
        if (tmp == ".")
            break;
        else
        {
            for (int i = 0; i < tmp.length(); i++)
            {
                if (tmp[i] == '(' || tmp[i] == '[')
                {
                    s.push(tmp[i]);
                }
                else if (tmp[i] == ')' || tmp[i] == ']')
                {
                    if (s.empty())
                    {
                        flag = false;
                        break;
                    }
                    if (s.top() == '(' && tmp[i] == ')')
                    {
                        s.pop();
                        continue;
                    }
                    else if (s.top() == '[' && tmp[i] == ')')
                    {
                        flag = false;
                        break;
                    }
                    if (s.top() == '[' && tmp[i] == ']')
                    {
                        s.pop();
                        continue;
                    }
                    else if (s.top() == '(' && tmp[i] == ']')
                    {
                        flag = false;
                        break;
                    }
                }
            }
            if (flag == false || !s.empty())
            {
                cout << "no\n";
            }
            else if (s.empty())
            {
                cout << "yes\n";
            }
        }
    }
    return 0;
}