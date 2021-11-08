#include <iostream>
#include <stack>
#include <string>

using namespace std;

int main()
{
    string s;
    cin >> s;
    stack<int> st;
    string ans = "";
    int idx = 0;
    for (int i = 0; i < s.length(); i++)
    {
        idx = i;
        if (s[i + 1] == ')')
            break;
    }

    return 0;
}