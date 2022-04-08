#include <bits/stdc++.h>
using namespace std;
int main()
{

    ios::sync_with_stdio(0);
    cin.tie(0);

    int N;
    cin >> N;
    vector<int> rope;
    int tmp;
    for (int i = 0; i < N; i++)
    {
        cin >> tmp;
        rope.push_back(tmp);
    }
    sort(rope.begin(), rope.end(), greater<int>());
    long long ans = 0;
    long long sum = 0;
    for (int i = 0; i < N; i++)
    {
        sum = rope[i] * (i + 1);
        if (ans < sum)
            ans = max(ans, sum);
    }
    cout << ans;

    return 0;
}