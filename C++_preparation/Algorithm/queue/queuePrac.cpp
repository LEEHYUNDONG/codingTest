#include <bits/stdc++.h>
using namespace std;
int main()
{

    ios::sync_with_stdio(0);
    cin.tie(0);
    queue<int> q;

    q.push(10);
    q.push(20);
    cout << q.size() << '\n';
    cout << q.front() << '\n';
    q.pop();
    cout << q.front() << '\n';
    return 0;
}