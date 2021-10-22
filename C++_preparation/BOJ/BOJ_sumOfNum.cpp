#include <iostream>
#include <vector>
using namespace std;

int main()
{

    // ios_base::sync_with_stdio;
    // cin.tie(0);
    // cout.tie(0);
    int n, m;
    cin >> n >> m;
    vector<int> num;

    for (int i = 0; i < n; i++)
    {
        int tmp;
        cin >> tmp;
        num.push_back(tmp);
    }
    int l = 0;
    int r = 0;
    int cnt = 0;
    int sum = 0;

    while (l <= r && r < n && l < n)
    {
        if (sum == 0 && l == r)
            sum += num[l];
        if (sum == m)
            cnt++;
        if (sum <= m)
        {
            ++r;
            sum += num[r];
        }
        if (sum > m)
        {
            sum -= num[l];
            if (l == r)
            {
                r++;
            }
            l++;
        }
    }

    cout << cnt << endl;

    return 0;
}