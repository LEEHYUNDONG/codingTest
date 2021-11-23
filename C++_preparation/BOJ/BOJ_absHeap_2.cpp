#include <iostream>
#include <queue>

using namespace std;

int main()
{
    ios::sync_with_stdio(false);
    cin.tie(0);
    cout.tie(0);

    priority_queue<pair<int, int> > q;
    int n, m;

    cin >> m;
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