#include <string>
#include <vector>
#include <iostream>
#include <cmath>

using namespace std;

int solution(string dartResult)
{
    int answer = 0;
    vector<int> top;
    int tmp;
    for (int i = 0; i < dartResult.length(); i++)
    {
        if (dartResult[i] >= '0' && dartResult[i] <= '9')
        {
            if (dartResult[i] == '1' && dartResult[i + 1] == '0')
            {
                tmp = 10;
                i++;
            }
            else
                tmp = (int)dartResult[i] - '0';
        }
        if (dartResult[i] == 'S')
        {
            top.push_back(tmp);
        }
        else if (dartResult[i] == 'D')
        {
            top.push_back(pow(tmp, 2));
        }
        else if (dartResult[i] == 'T')
        {
            top.push_back(pow(tmp, 3));
        }
        else if (dartResult[i] == '*')
        {
            int r = top.back();
            top.pop_back();
            r *= 2;
            top[top.size() - 1] *= 2;
            top.push_back(r);
        }
        else if (dartResult[i] == '#')
        {
            top[top.size() - 1] *= -1;
        }
    }
    for (auto a : top)
    {
        answer += a;
    }
    return answer;
}