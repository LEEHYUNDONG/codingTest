#include <string>
#include <vector>
#include <algorithm>
#include <iostream>

using namespace std;

vector<string> solution(vector<string> orders, vector<int> course)
{
    vector<string> answer;
    int cma = course[course.size() - 1];
    int cmi = course[0];

    for (int i = 0; i < orders.size(); i++)
    {
        string s = orders[i];
        int l = s.length();
        if (l < cmi || l > cma)
            continue;
        vector<int> cnt(l, 1);
        int flag = 1;
        for (int j = 0; j < l; j++)
        {
            for (int k = i + 1; k < orders.size(); k++)
            {
                string sc = orders[i + 1];
                for (int q = 0; q < sc.length(); q++)
                {
                    if (sc[q] == s[j])
                        cnt[j]++;
                }
                if (cnt[j] < cmi || cnt[j] > cma)
                {
                    flag = 0;
                    break;
                }
            }
        }
        if (flag == 1)
            answer.push_back(s);
    }

    sort(answer.begin(), answer.end());
    return answer;
}