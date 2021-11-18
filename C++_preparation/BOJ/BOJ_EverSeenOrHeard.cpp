#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
#include <unordered_map>

using namespace std;

int main()
{
    ios::sync_with_stdio(false);
    cin.tie(0);
    cout.tie(0);

    int n, m;
    cin >> n >> m;
    string name;
    unordered_map<string, int> s;
    vector<string> ans;
    for (int i = 0; i < n; i++)
    {
        cin >> name;
        s.insert({name, 1});
    }
    for (int j = 0; j < m; j++)
    {
        cin >> name;
        if (s[name] == 1)
            ans.push_back(name);
    }
    cout << ans.size() << endl;
    sort(ans.begin(), ans.end());
    for (auto a : ans)
        cout << a << endl;
    return 0;
}