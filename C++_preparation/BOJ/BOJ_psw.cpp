#include <iostream>
#include <unordered_map>
#include <vector>
using namespace std;

int main()
{
    int n, m;
    vector<string> ans;
    ios::sync_with_stdio(false);
    cin.tie(NULL);
    cin >> n >> m;
    unordered_map<string, string> pw;
    for (int i = 0; i < n; i++)
    {
        string t1, t2;
        cin >> t1 >> t2;
        pw.insert(make_pair(t1, t2));
    }
    for (int i = 0; i < m; i++)
    {
        string tmp;
        cin >> tmp;
        ans.push_back(pw[tmp]);
    }
    for (auto a : ans)
    {
        cout << a << endl;
    }
    return 0;
}