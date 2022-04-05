#include <bits/stdc++.h>
using namespace std;
int main()
{

    ios::sync_with_stdio(0);
    cin.tie(0);
    int n, m;
    cin >> n >> m;
    int j;
    cin >> j;

    vector<int> apple;
    int ap;
    for (int i = 0; i < j; i++)
    {
        cin >> ap;
        apple.push_back(ap);
    }
    int ans = 0;
    int startBox, endBox;
    startBox = 1;
    endBox = m;

    for (int i = 0; i < apple.size(); i++)
    {
        int tmp;
        if (startBox <= apple[i] && apple[i] <= endBox)
            continue;
        else if (startBox > apple[i])
        {
            tmp = abs(startBox - apple[i]);
            ans += tmp;
            startBox -= tmp;
            endBox -= tmp;
        }
        else if (endBox < apple[i])
        {
            tmp = abs(endBox - apple[i]);
            ans += tmp;
            startBox += tmp;
            endBox += tmp;
        }
    }

    cout << ans;

    return 0;
}