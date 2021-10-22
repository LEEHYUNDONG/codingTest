#include <iostream>
#include <vector>
using namespace std;

int main()
{
    int n, m;
    cin >> n >> m;
    vector<int> num;

    for (int i = 0; i < n; i++)
    {
        int tmp;
        cin >> tmp;
        num.push_back(tmp);
    }
    int res = 0;
    int l = 0;
    int r = 0;
    while (l <= r && l < n && r < n)
    {
        if (l - r + 1 > m)
        {
            if (num[l] < num[r])
                l++;
            else
                r++;
        }
        if (l == r || res == 0)
            res += num[l];
        if (num[l] < res && num[l] < num[r])
        {
            res -= num[l];
            l++;
        }
        else
        {
            r++;
            res += num[r];
        }
    }
    cout << res << endl;
    return 0;
}