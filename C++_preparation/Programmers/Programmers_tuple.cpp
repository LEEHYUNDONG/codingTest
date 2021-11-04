#include <string>
#include <vector>
#include <iostream>
#include <algorithm>

using namespace std;

vector<int> solution(string s)
{
    int st[101010] = {};
    vector<int> answer;
    string tmp;
    for (char i : s)
    {
        if (i - '0' >= 0 && i - '0' <= 9)
        {
            tmp += i;
        }
        else
        {
            if (tmp.length())
                st[stoi(tmp)]++, tmp.clear();
        }
    }

    vector<pair<int, int> > ans;
    for (int i = 0; i < 101010; i++)
    {
        if (st[i])
            ans.push_back(make_pair(st[i], i));
    }
    sort(ans.begin(), ans.end());
    reverse(ans.begin(), ans.end());
    for (auto a : ans)
        answer.push_back(a.second);

    return answer;
}