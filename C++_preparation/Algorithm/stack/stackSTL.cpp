#include <bits/stdc++.h>
using namespace std;
int main()
{

    ios::sync_with_stdio(0);
    cin.tie(0);
    stack<int> s;
    s.push(10);
    s.push(20);
    s.push(30);
    cout << s.top() << '\n';
    if (s.empty())
        cout << "empty" << '\n';
    else
        cout << "not empty" << '\n';
    s.pop();
    cout << s.top() << '\n';

    return 0;
}