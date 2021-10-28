#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main()
{
    int n, m;
    cin >> n >> m;
    // vector<vector<int> > card;
    vector<int> ans;
    for (int i = 0; i < n; i++)
    {
        int minimum = INT_MAX;
        for (int j = 0; j < m; j++)
        {
            int tmp;
            cin >> tmp;
            if (tmp < minimum)
            {
                minimum = tmp;
            }
            // card[i][j] = tmp;
        }
        ans.push_back(minimum);
    }
    int res = 0;
    for (int i = 0; i < ans.size(); i++)
    {
        res = max(ans[i], res);
    }
    cout << res << '\n';
    return 0;
}