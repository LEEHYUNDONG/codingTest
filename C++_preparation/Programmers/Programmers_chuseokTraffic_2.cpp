#include <string>
#include <vector>
#include <iostream>

using namespace std;

int solution(vector<string> lines)
{
    int answer = 0;
    vector<int> start, end;

    for (int i = 0; i < lines.size(); i++)
    {
        int ih, im, is, process;
        string h, m, s, ms;

        lines[i].pop_back();
        h = lines[i].substr(11, 2);
        m = lines[i].substr(14, 2);
        s = lines[i].substr(17, 2);
        ms = lines[i].substr(20, 3);
        process = stof(lines[i].substr(24, 5)) * 1000;

        ih = stoi(h) * 60 * 60 * 1000;
        im = stoi(m) * 60 * 1000;
        is = stoi(s) * 1000 + stoi(ms);

        start.push_back(ih + im + is - process + 1);
        end.push_back(ih + im + is);
    }
    for (int i = 0; i < lines.size(); i++)
    {
        int endT = end[i] + 1000;
        int cnt = 0;
        for (int j = i; j < lines.size(); j++)
        {
            if (start[j] < endT)
            {
                cnt++;
            }
        }
        if (answer < cnt)
            answer = cnt;
    }
    return answer;
}