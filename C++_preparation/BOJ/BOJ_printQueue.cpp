#include <iostream>
#include <queue>
#include <algorithm>

using namespace std;

int main()
{
    ios::sync_with_stdio(false);
    cin.tie(0);
    cout.tie(0);

    int t, n;
    cin >> t;

    while (t--)
    {
        int search;
        priority_queue<pair<int, int> > q;
        cin >> n >> search;
        int p;
        for (int i = 0; i < n; i++)
        {
            cin >> p;
            q.push(make_pair(p, i));
        }

        for (int i = 0; i < n; i++)
        {
            auto a = q.top();
            q.pop();
            cout << a.second << endl;
            if (a.second == search)
            {
                cout << i + 1 << '\n';
                break;
            }
        }
    }
    return 0;
}