#include <string>
#include <algorithm>
#include <iostream>
#include <unordered_map>

using namespace std;

int solution(string str1, string str2)
{
    int answer = 0, min = 0, max = 0;
    vector<string> s1;
    vector<string> s2;
    unordered_map<string, int> d;
    unordered_map<string, int> d2;
    int cnt = 0;
    int tcnt = 0;
    for (int i = 0; i < str1.length() - 1; i++)
    {
        if ((str1[i] >= 'A' && str1[i] <= 'Z') || (str1[i] >= 'a' && str1[i] <= 'z'))
        {
            string tmp = "";
            tmp += toupper(str1[i]);
            if ((str1[i + 1] >= 'A' && str1[i + 1] <= 'Z') || (str1[i + 1] >= 'a' && str1[i + 1] <= 'z'))
            {
                tmp += toupper(str1[i + 1]);
                s1.push_back(tmp);
                if (d.find(tmp) != d.end())
                    d[tmp]++;

                else
                    d[tmp] = 1;
            }
            else
                continue;
        }
    }

    for (int i = 0; i < str2.length() - 1; i++)
    {
        if ((str2[i] >= 'A' && str2[i] <= 'Z') || (str2[i] >= 'a' && str2[i] <= 'z'))
        {
            string tmp = "";
            tmp += toupper(str2[i]);
            if ((str2[i + 1] >= 'A' && str2[i + 1] <= 'Z') || (str2[i + 1] >= 'a' && str2[i + 1] <= 'z'))
            {
                tmp += toupper(str2[i + 1]);
                s2.push_back(tmp);
                if (d2.find(tmp) != d2.end())
                    d2[tmp]++;
                else
                    d2[tmp] = 1;
            }
            else
                continue;
        }
    }
    if (s1.empty() && s2.empty())
        return 65536;
    max = s1.size() + s2.size();

    if (s1.size() > s2.size())
    {
        for (int i = 0; i < s2.size(); i++)
        {
            auto itr = find(s1.begin(), s1.end(), s2[i]);
            if (itr != s1.end())
            {
                min++;
                s1.erase(itr);
            }
        }
    }
    else
    {
        for (int i = 0; i < s1.size(); i++)
        {
            auto itr = find(s2.begin(), s2.end(), s1[i]);
            if (itr != s2.end())
            {
                min++;
                s2.erase(itr);
            }
        }
    }

    max -= min;

    if (max == 0)
        return 65536;

    double tmp = (double)min / (double)max;

    return tmp * 65536;
}