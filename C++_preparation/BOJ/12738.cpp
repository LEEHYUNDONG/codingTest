#include <bits/stdc++.h>
using namespace std;
typedef long long ll;

ll N;
vector<ll> arr;
vector<ll> dp;
vector<ll> f;

int main()
{
    ios::sync_with_stdio(0);
    cin.tie(0);
    cin >> N;
    ll size = 0;
    for (int i = 0; i < N; i++)
    {
        ll tmp;
        cin >> tmp;
        arr.push_back(tmp);
        auto it = lower_bound(dp.begin(), dp.end(), tmp);
        f.push_back(it-dp.begin());
        if (it == dp.end())
        {
            dp.push_back(tmp);
            size++;
        }
        else{
            dp[it-dp.begin()] = tmp;
            
        }
    }
    vector<ll> ans;
    for (int i = N - 1; i > -1; i--)
    {
        if (size < 1)
            break;
        if(f[i] == size-1){
            ans.push_back(arr[i]);
            size--;
        }

    }

    cout << ans.size() << '\n';
    while(!ans.empty()){
        cout << ans.back() << ' ';
        ans.pop_back();
    }
    return 0;
}
// 9
// 3 1 4 6 2 2 0 3 6