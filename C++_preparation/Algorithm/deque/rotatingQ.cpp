#include <bits/stdc++.h>
using namespace std;
int main()
{
    ios::sync_with_stdio(0);
    cin.tie(0);

    int n, m;
    cin >> n >> m;
    int tmp;
    int ans = 0;
    deque<int> dq;

    for (int i = 0; i < n; i++)
        dq.push_back(i + 1);

    for (int i = 0; i < m; i++)
    {
        cin >> tmp;
        int idx = find(dq.begin(), dq.end(), tmp) - dq.begin(); //

        while (tmp != dq.front())
        {
            if (idx < dq.size() - idx)
            {
                dq.push_back(dq.front());
                dq.pop_front();
            }
            else
            {
                dq.push_front(dq.back());
                dq.pop_back();
            }
            ans++;
        }
        dq.pop_front();
    }
    cout << ans;
    return 0;
}