#include <iostream>
#include <queue>
#include <cmath>
using namespace std;

int main()
{
    ios::sync_with_stdio(false);
    cin.tie(0);
    cout.tie(0);

    int m, n;
    cin >> m;
    priority_queue<pair<int, int> > q;

    for (int i = 0; i < m; i++)
    {
        cin >> n;
        if (n == 0 && !q.empty())
        {
            cout << (q.top().first * q.top().second) << '\n';
            q.pop();
        }
        else if (n == 0 && q.empty())
            cout << 0 << '\n';
        if (n < 0)
            q.push(make_pair(n, 1));

        else if (n > 0)
            q.push(make_pair(-n, -1));
    }
    return 0;
}