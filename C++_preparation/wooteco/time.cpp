#include <string>
#include <vector>
#include <iostream>

using namespace std;

string solution(vector<string> log)
{
    string answer = "";
    int tot = 0;
    for (int i = 0; i < log.size(); i += 2)
    {
        // string s = log[i];
        // string e = log[i+1];
        int starth = stoi(log[i].substr(0, 2)) * 60;
        int endh = stoi(log[i + 1].substr(0, 2)) * 60;
        int startm = stoi(log[i].substr(3, 2));
        int endm = stoi(log[i + 1].substr(3, 2));
        int time = endm - startm + endh - starth;

        if (time < 5)
            continue;
        else if (time < 105)
            tot += time;
        else
            tot += 105;
    }
    int hh = tot / 60;
    int mm = tot % 60;
    if (hh < 10)
    {
        answer += "0";
        answer += to_string(hh);
    }
    else if (10 <= hh && hh < 24)
    {
        answer += to_string(hh);
    }
    answer += ":";
    if (mm < 10)
    {
        answer += "0";
        answer += to_string(mm);
    }
    else
    {
        answer += to_string(mm);
    }
    return answer;
}