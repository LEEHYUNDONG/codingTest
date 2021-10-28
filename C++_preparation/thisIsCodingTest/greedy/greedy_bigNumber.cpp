#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main()
{
    int n, m, k;
    cin >> n >> m >> k;
    vector<int> num;
    for (int i = 0; i < n; i++)
    {
        int tmp;
        cin >> tmp;
        num.push_back(tmp);
    }
    sort(num.begin(), num.end());
    int res = 0;
    for (int i = 0; i < m; i++)
    {
        if (i % k == 0 && i > 0)
            res += num[n - 2];
        else
            res += num[n - 1];
    }
    cout << res << '\n';
    return 0;
}