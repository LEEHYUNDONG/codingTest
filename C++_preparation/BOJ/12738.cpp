#include <bits/stdc++.h>
using namespace std;
typedef long long ll;


ll N;
vector<ll> arr(1000010);
vector<ll> dp;


int main()
{
    ios::sync_with_stdio(0);
    cin.tie(0);
    cin >> N;
    for (int i = 0; i < N;i++)
        cin >> arr[i];

    for (int i = 0; i < N;i++){
        auto it = lower_bound(dp.begin(), dp.end(), arr[i]);
        if(dp.size() == 0||it == dp.end())
            dp.push_back(arr[i]);
        else
            dp[it - dp.begin()] = arr[i];
    }
    cout << dp.size();
    return 0;
}