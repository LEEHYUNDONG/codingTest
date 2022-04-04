#include <bits/stdc++.h>
using namespace std;

int main()
{
    ios::sync_with_stdio(0);
    cin.tie(0);
    string s;
    cin >> s;
    list<char> L;

    for (auto c : s)
        L.push_back(c);

    auto curr = L.end();

    int n;
    cin >> n;

    for (int i = 0; i < n; i++)
    {
        char op;
        cin >> op;
        if (op == 'P')
        {
            char ch;
            cin >> ch;
            L.insert(curr, ch);
        }
        else if (op == 'L')
        {
            if (curr != L.begin())
                curr--;
        }
        else if (op == 'D')
        {
            if (curr != L.end())
                curr++;
        }
        else if (op == 'B')
        {
            if (curr != L.begin())
            {
                curr--;
                curr = L.erase(curr);
            }
        }
    }
    for (auto c : L)
        cout << c;
    return 0;
}