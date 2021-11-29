#include <iostream>
#include <string>
#include <cmath>

using namespace std;

char num[10] = {'0', '1', '2', '3', '4', '5', '6', '7', '8', '9'};
char broken[10];
string ch;
long long ans = 100;
string a = "100";
long long n;
int cnt;

void dfs(string s, int depth)
{
    if (s.length() == ch.length() || s.length() == ch.length() + 1 || s.length() == ch.length() + 2)
    {
        for (int i = 0; i < n; i++)
        {
            for (int j = 0; j < s.length(); j++)
            {
                if (s[j] == broken[i])
                    return;
            }
        }
        if (abs(stoll(s) - stoll(ch)) < abs(stoll(a) - stoll(ch)))
        {
            a = s;
            ans = stoll(s);
            if (depth + abs(ans - stoll(ch)) < cnt)
                cnt = depth + abs(ans - stoll(ch));
        }
        return;
    }
    for (int i = 0; i < 10; i++)
        dfs(s + num[i], depth + 1);
}
int main()
{

    cin >> ch;
    cin >> n;
    for (int i = 0; i < n; i++)
        cin >> broken[i];

    cnt = abs(stoll(ch) - ans);
    dfs("", 0);

    cout << cnt << '\n';

    return 0;
}