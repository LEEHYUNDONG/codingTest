#include <bits/stdc++.h>
using namespace std;
int main()
{

    ios::sync_with_stdio(0);
    cin.tie(0);
    queue<int> q;
    int n;
    cin >> n;

    for (int i = 0; i < n; i++)
        q.push(i + 1);

    while (q.size() > 1)
    {
        q.pop();
        int tmp = q.front();
        q.pop();
        q.push(tmp);
    }
    cout << q.front();

    return 0;
}