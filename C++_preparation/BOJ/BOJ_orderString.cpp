#include <iostream>
#include <string>
#include <algorithm>
#include <vector>

using namespace std;
bool Compare(string a, string b)
{
    if (a.length() != b.length())
        return a.length() < b.length();
    else
        return a < b;
}
int main()
{
    int n;
    cin >> n;
    vector<string> s;
    for (int i = 0; i < n; i++)
    {
        string tmp;
        cin >> tmp;
        if (find(s.begin(), s.end(), tmp) == s.end())
            s.push_back(tmp);
    }

    sort(s.begin(), s.end(), Compare);
    for (auto a : s)
    {
        cout << a << '\n';
    }
    return 0;
}