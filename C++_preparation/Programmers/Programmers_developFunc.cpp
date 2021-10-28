#include <string>
#include <vector>
#include <iostream>
using namespace std;

vector<int> solution(vector<int> progresses, vector<int> speeds)
{
    vector<int> answer;
    int working = (100 - progresses[0]) / speeds[0];
    if ((100 - progresses[0]) % speeds[0] != 0)
        working += 1;

    answer.push_back(0);
    int ind = 0;
    int w = 0;
    for (int i = 0; i < speeds.size(); i++)
    {
        w = (100 - progresses[i]) / speeds[i];
        if ((100 - progresses[i]) % speeds[i] != 0)
        {
            w += 1;
        }
        if (working >= w)
        {
            answer[ind]++;
        }
        else
        {
            answer.push_back(1);
            ind++;
            working = w;
        }
    }
    return answer;
}